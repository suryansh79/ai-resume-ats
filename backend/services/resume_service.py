from utils.pdf_reader import read_pdf_text

def extract_resume_text(file):
    """
    Service layer responsible for extracting
    raw text from a resume PDF.
    """
    return read_pdf_text(file)
