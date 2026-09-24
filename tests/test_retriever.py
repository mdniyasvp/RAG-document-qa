from src.retriever import Retriever

retriever = Retriever()
query = "What is the annual leave policy?"
results = retriever.retrieve(
    query= query,
    top_k=3,
)
print("\n QUERY:")
print(query)
print("\nRESULTS:")

for i, document in enumerate(results["documents"][0]):

    print(f"\n--- Result {i + 1} ---")

    print("ID:")
    print(results["ids"][0][i])

    print("\nDocument:")
    print(document)

    print("\nDistance:")
    print(results["distances"][0][i])

    print("\nMetadata:")
    print(results["metadatas"][0][i])