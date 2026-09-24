from src.chunker import chunk_text


text = """
Employees receive 24 annual leave days per year.
Leave requests must be submitted through the HR portal.
Employees should contact HR for special circumstances.
"""


chunks = chunk_text(
    text,
    chunk_size=100,
    chunk_overlap=20,
)


print(f"Number of chunks: {len(chunks)}")


for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i} ---")
    print(chunk)