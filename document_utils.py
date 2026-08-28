from io import BytesIO
from pypdf import PdfReader
from docx import Document


def extract_product_document_text(uploaded_file, max_chars=12000):
    if uploaded_file is None:
        return ""

    filename = uploaded_file.name.lower()
    file_bytes = uploaded_file.getvalue()

    try:
        if filename.endswith(".txt"):
            text = file_bytes.decode("utf-8", errors="ignore")

        elif filename.endswith(".pdf"):
            reader = PdfReader(BytesIO(file_bytes))
            pages = []

            for page in reader.pages:
                page_text = page.extract_text() or ""
                pages.append(page_text)

            text = "\n".join(pages)

        elif filename.endswith(".docx"):
            document = Document(BytesIO(file_bytes))
            paragraphs = [
                paragraph.text
                for paragraph in document.paragraphs
                if paragraph.text.strip()
            ]
            text = "\n".join(paragraphs)

        else:
            return "Unsupported document format."

        text = " ".join(text.split())

        if not text:
            return "No readable text was found in the uploaded product document."

        return text[:max_chars]

    except Exception as e:
        return f"Product document parsing failed: {e}"
