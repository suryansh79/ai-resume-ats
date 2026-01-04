from PyPDF2 import PdfReader

def read_pdf_text(file):
    """
    Reads and extracts text from a PDF file.
    """
    reader = PdfReader(file)
    extracted_text = ""

    for page in reader.pages:
        extracted_text += page.extract_text() or ""

    return extracted_text.strip()
