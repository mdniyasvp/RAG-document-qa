import chromadb
class Vector_store:
    def __init__(self, path: str = "data/chroma"):
        self.client =chromadb.PersistentClient(
            path= path
        )
        self.collection = self.client.get_or_create_collection(
            name = "documents"
        )
    def add_documents(
            self,
            documents: list[str],
            embeddings,
            ids:list[str],
            metadatas: list[dict] | None = None,
    ):
        self.collection.add(
            documents = documents,
            embeddings= embeddings.tolist(),
            ids =ids,
            metadata = metadatas,
        )
    def search(
            self,
            query_embedding,
            top_k: int =3,
    ):
        return self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results= top_k,
        )