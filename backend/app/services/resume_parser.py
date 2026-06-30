from pathlib import Path

from docx import Document
from pypdf import PdfReader


def extract_resume_text(file_path: str):
    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_pdf(file_path)

    if extension == ".docx":
        return extract_docx(file_path)

    return ""


def extract_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_docx(file_path):
    doc = Document(file_path)

    return "\n".join(
        p.text for p in doc.paragraphs
    )