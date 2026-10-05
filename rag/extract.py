from pathlib import Path
from pypdf import PdfReader

def extract(document_path) -> str:
    path = Path(document_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {document_path}")

    extension = path.suffix.lower()

    if extension == ".txt":
        with open(path, "r", encoding="utf-8") as file:
            return file.read()

    elif extension == ".pdf":
        reader = PdfReader(path)
        texts = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                texts.append(text)
        return "\n".join(texts)

    raise ValueError(f"Unsupported file type: {extension}")