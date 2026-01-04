from PyPDF2 import PdfReader

def read_pdf_text(file):
    
    reader = PdfReader(file)
    extracted_text = ""

    for page in reader.pages:
        extracted_text += page.extract_text() or ""

    return extracted_text.strip()
