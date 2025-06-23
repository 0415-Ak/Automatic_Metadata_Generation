import os
import pdfplumber
from docx import Document


def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.pdf':
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
    elif ext == '.docx':
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
    elif ext == '.txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        raise ValueError("Unsupported file type")

    return text