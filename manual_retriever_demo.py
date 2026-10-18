from src.retriever import Retriever

retriever = Retriever()
#query = "names of peoples who are inthe advisory board?"
query = "What is the annual leave policy?"
#query = "What is the capital of japapn?"
results = retriever.retrieve(
    query= query,
    top_k=4,
    max_distance= 1.4,
    metadata_filter={
        "document": "Company-Policy-and-Procedure"
    },
)
print("\n QUERY:")
print(query)
print("\nRESULTS:")
print("Original query:", query)
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
