from src.retriever import Retriever
from src.hybrid_retriever import HybridRetriever


retriever = Retriever()

hybrid_retriever = HybridRetriever(
    retriever=retriever
)


query = "What is the annual leave policy?"


results = hybrid_retriever.search(
    query=query,
    top_k=3,
    candidate_k=10,
    alpha=0.7,
)


print("\nQUERY:")
print(query)

print("\nHYBRID RESULTS:")

for i, result in enumerate(results):

    print(f"\n--- Result {i + 1} ---")

    print("ID:")
    print(result["id"])

    print("\nDocument:")
    print(result["document"])

    print("\nDistance:")
    print(result["distance"])

    print("\nVector score:")
    print(result["vector_score"])

    print("\nKeyword score:")
    print(result["keyword_score"])

    print("\nHybrid score:")
    print(result["hybrid_score"])

    print("\nMetadata:")
    print(result["metadata"])