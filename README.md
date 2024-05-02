# DeepPDF AI

DeepPDF AI is a specialized application designed to process and interact with PDF documents using advanced AI techniques. It leverages the power of large language models to provide insightful answers to queries based on the contents of the documents. This README outlines the project structure and provides instructions on how to build and run the application.

## Installation

To run DeepPDF AI, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Docker installed.
3. Build the Docker image:
   ```bash
   docker build -t deeppdf-ai .
   ```
4. Run the Docker container:
   ```bash
   docker run -p 7860:7860 deeppdf-ai
   ```

## Usage

Once the application is running, you can interact with it through a ChainLit interface at `http://localhost:7860/` by sending queries related to the PDF documents it has processed. Example questions include:

- "What was the total value of 'Cash and cash equivalents' as of December 31, 2023?"
- "Who are Meta's 'Directors' (i.e., members of the Board of Directors)?"

## Acknowledgements

This project uses technologies including LangChain, OpenAI's GPT models, and Qdrant for vector storage. Thanks to all open-source contributors and organizations that make these tools available.
