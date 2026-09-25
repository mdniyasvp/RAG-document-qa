from src.loader import load_pdf

text = load_pdf("data/documents/Company-Policy-and-Procedure.pdf")
print(text[:2000])