from src.embeddings import EmbeddingModel
model = EmbeddingModel()
texts = [
    "Employees receive 24 annual leave days.",
    "Workers get 24 vacation days every year.",
    "the company provides free parking."
]

embeddings = model.encode(texts)
print(embeddings.shape)