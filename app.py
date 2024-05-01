import os
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Qdrant
from langchain_core.prompts import ChatPromptTemplate
from langchain.retrievers import MultiQueryRetriever
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
from operator import itemgetter
import chainlit as cl
from chainlit.playground.providers import ChatOpenAI

# Load environment variables
load_dotenv()

# Configuration for OpenAI
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
openai_chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Load the document
docs = PyMuPDFLoader("https://d18rn0p25nwr6d.cloudfront.net/CIK-0001326801/c7318154-f6ae-4866-89fa-f0c589f2ee3d.pdf").load()

# Tokenization function
def tiktoken_len(text):
    tokens = tiktoken.encoding_for_model("gpt-3.5-turbo").encode(text)
    return len(tokens)

# Splitting documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50, length_function=tiktoken_len)

split_chunks = text_splitter.split_documents(docs)

# Initalize the embedding model
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

# Create a Qdrant vector store
qdrant_vectorstore = Qdrant.from_documents(split_chunks, embedding_model, location=":memory:", collection_name="Meta 10-k Fillings")

# Create a retriever from the vector store
qdrant_retriever = qdrant_vectorstore.as_retriever()

# Define the RAG prompt

RAG_PROMPT = """
CONTEXT:
{context}

QUERY:
{question}

Answer the query if the context is related to it; otherwise, answer: 'Sorry, the context is unrelated to the query, I can't answer.'
"""
rag_prompt = ChatPromptTemplate.from_template(RAG_PROMPT)

multiquery_retriever = MultiQueryRetriever.from_llm(retriever=qdrant_retriever, llm=openai_chat_model)

# ChainLit setup for chat interaction
@cl.on_chat_start
async def start_chat():
    settings = {
        "model": "gpt-3.5-turbo",
        "temperature": 0,
        "max_tokens": 500,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }
    cl.user_session.set("settings", settings)

@cl.on_message
async def main(message: cl.Message):

    question = message.content
    response = handle_query(question)  # Utilize LangChain functionality to process the question

    msg = cl.Message(content=response)
    await msg.send()

# Define how the queries will be handled using LangChain
def handle_query(question):
    retrieval_augmented_qa_chain = (
        {"context": itemgetter("question") | multiquery_retriever, "question": itemgetter("question")}
        | RunnablePassthrough.assign(context=itemgetter("context"))
        | {"response": rag_prompt | openai_chat_model, "context": itemgetter("context")}
    )
    response = retrieval_augmented_qa_chain.invoke({"question": question})
    return response["response"].content
