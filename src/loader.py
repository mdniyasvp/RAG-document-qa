from pathlib import Path
from pypdf import PdfReader

def load_pdf(file_path: str) -> str:
    """Extract text from pdf file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"filenotfound: {file_path}")

    reader = PdfReader(path)

    pages= []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return"\n".join(pages)