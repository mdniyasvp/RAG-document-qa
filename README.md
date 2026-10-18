# RAG Document QA

A Python project for experimenting with Retrieval-Augmented Generation (RAG) and document question answering.

## Features

- PDF text extraction using PyPDF
- Text chunking with configurable chunk size and overlap
- Semantic embeddings using Sentence Transformers
- Vector storage and similarity search with ChromaDB
- Query rewriting before retrieval
- Metadata-based filtering
- Optional distance-based filtering of retrieved results
- Keyword search and hybrid retrieval components
- Unit tests for text chunking

## Tech Stack

- Python 3.11+
- uv for dependency management
- Sentence Transformers
- ChromaDB
- LangChain Chroma
- PyPDF
- pytest

## Project Structure

```text
rag-document-qa/
├── src/
│   ├── chunker.py
│   ├── embeddings.py
│   ├── hybrid_retriever.py
│   ├── indexer.py
│   ├── keyword_search.py
│   ├── loader.py
│   ├── query_rewriter.py
│   ├── retriever.py
│   └── vector_store.py
├── tests/
├── data/
│   ├── documents/   # Local PDF documents; not committed
│   └── chroma/      # Local vector database; not committed
├── pyproject.toml
├── uv.lock
└── README.md
