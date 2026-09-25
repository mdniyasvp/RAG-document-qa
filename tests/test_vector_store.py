from src.vector_store import VectorStore

store = VectorStore()
print("Number of documents:")
print(store.collection.count())