## v0.1.4 (2024-05-02)

### Added

- Introduced the RAGAS evaluation tool for assessing the performance of the RAG application, comparing the baseline with the MultiQueryRetriever strategy.
- Saved the RAGAS test set in csv for later evaluation and comparison.
- Updated `chainlit.md` Tech Touch section.

## v0.1.3 (2024-05-02)

### Added

- Rebranded the project to DeepPDF AI, focusing on interacting with PDF documents using AI.
- Introduced a comprehensive guide and technical details in `chainlit.md`.
- Added Docker support for easy deployment, including Dockerfile adjustments and user permissions setup.
- Updated `README.md` with installation, usage, and acknowledgements sections.
- Enhanced the application's backend with new imports and configurations in `app.py`.
- Updated `requirements.txt` to include `uvicorn` for ASGI support.

## v0.1.2 (2024-05-01)

### Added

- Introduced a Chainlit application for interactive chat-based query handling using LangChain, OpenAI, and Qdrant technologies.
- Implemented document loading, tokenization, document splitting, embedding, and vector storage functionalities.
- Added Dockerfile for containerized deployment of the Chainlit application.
- Included a welcome guide in `chainlit.md` and updated `requirements.txt` with precise versioning for dependencies.

## v0.1.1 (2024-05-01)

### Added

- Implemented MultiQueryRetriever strategy for improved context retrieval in the PDF RAG QA application.

## v0.1.0 (2024-05-01)

### Added

- Introduced a Jupyter notebook for PDF RAG QA application, including environment setup, data loading, chunking, embedding, vector storing, and response generation using langchain, qdrant-client, tiktoken, pymupdf, and OpenAI's GPT models.
