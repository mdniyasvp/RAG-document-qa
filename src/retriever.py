from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore

class Retriever:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
    ):
        query_embedding = self.embedding_model.encode(
            [query]
        )[0]

        results = self.vector_store.search(
            query_embedding = query_embedding,
            top_k =top_k,
        )
        return results