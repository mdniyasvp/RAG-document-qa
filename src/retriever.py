from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore
import numpy as np
from src.query_rewriter import QueryRewriter

class Retriever:

    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()
        self.query_rewriter = QueryRewriter()

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
        max_distance: float | None = None,
        metadata_filter: dict | None = None,
    ):

        rewritten_query = self.query_rewriter.rewrite(query)

        query_embedding = self.embedding_model.encode([rewritten_query])[0]

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k,
            where=metadata_filter,
        )

        if max_distance is None:
            return results

        return self._filter_by_distance(
            results,
            max_distance,
        )

    @staticmethod
    def _filter_by_distance(
        results,
        max_distance: float,
    ):

        ids = results["ids"][0]
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        filtered_ids = []
        filtered_documents = []
        filtered_metadatas = []
        filtered_distances = []

        for (
            doc_id,
            document,
            metadata,
            distance,
        ) in zip(
            ids,
            documents,
            metadatas,
            distances,
        ):

            if distance <= max_distance:

                filtered_ids.append(doc_id)
                filtered_documents.append(document)
                filtered_metadatas.append(metadata)
                filtered_distances.append(distance)

        return {
            "ids": [filtered_ids],
            "documents": [filtered_documents],
            "metadatas": [filtered_metadatas],
            "distances": [filtered_distances],
        }

    @staticmethod
    def _cosine_similarity(a,b):
        denominator = np.linalg.norm(a) * np.linalg.norm(b)

        if denominator == 0:
            return 0.0

        return float(np.dot(a,b) / denominator)
    