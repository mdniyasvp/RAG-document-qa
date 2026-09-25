from pathlib import Path

from src.loader import load_pdf
from src.chunker import chunk_text
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore


class DocumentIndexer:

    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def index_pdf(self, file_path: str):

        # 1. Load PDF
        text = load_pdf(file_path)

        # 2. Create chunks
        chunks = chunk_text(text)

        if not chunks:
            raise ValueError(
                "No text could be extracted from the document."
            )

        # 3. Generate embeddings
        embeddings = self.embedding_model.encode(chunks)

        # 4. Create document name
        document_name = Path(file_path).stem

        # 5. Create unique IDs
        ids = [
            f"{document_name}_chunk_{i}"
            for i in range(len(chunks))
        ]

        # 6. Create metadata
        metadatas = [
            {
                "source": Path(file_path).name,
                "document": document_name,
                "chunk_index": i,
            }
            for i in range(len(chunks))
        ]

        # 7. Store everything in ChromaDB
        self.vector_store.add_documents(
            documents=chunks,
            embeddings=embeddings,
            ids=ids,
            metadatas=metadatas,
        )

        return len(chunks)