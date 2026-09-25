from src.indexer import DocumentIndexer

indexer = DocumentIndexer()

count = indexer.index_pdf(
    "data/documents/Company-Policy-and-Procedure.pdf"
)

print(f"Indexed {count} chunks.")