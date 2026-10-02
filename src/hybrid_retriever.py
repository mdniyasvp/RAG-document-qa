from src.keyword_search import KeywordSearch

class HybridRetriever:
    def __init__(self, retriever):
        self.retriever = retriever
        self.keyword_search = KeywordSearch()

    @staticmethod
    def distance_to_score(distance: float) -> float:
        return 1 / (1 + distance)

    def search(
        self,
        query: str,
        top_k: int = 3,
        candidate_k: int = 10,
        alpha: float = 0.7,
        ):
        results = self.retriever.retrieve(
            query=query,
            top_k=candidate_k,
        )

        documents = results["documents"][0]
        ids = results["ids"][0]
        distances = results["distances"][0]
        metadatas = results["metadatas"][0]

        scored_results = []

        for document_id, document, distance, metadata in zip(
            ids,
            documents,
            distances,
            metadatas,
        ):

            vector_score = self.distance_to_score(distance)

            keyword_score = self.keyword_search.score(
                query,
                document,
            )

            hybrid_score = (
                alpha * vector_score
                + (1 - alpha) * keyword_score
            )

            scored_results.append(
                {
                    "id": document_id,
                    "document": document,
                    "distance": distance,
                    "metadata": metadata,
                    "vector_score": vector_score,
                    "keyword_score": keyword_score,
                    "hybrid_score": hybrid_score,
                }
            )

        scored_results.sort(
            key=lambda result: result["hybrid_score"],
            reverse=True,
        )

        return scored_results[:top_k]

    