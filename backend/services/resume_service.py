from utils.pdf_reader import read_pdf_text
from services.skill_extractor import extract_skills_from_text

def analyze_resume(file):
    text = read_pdf_text(file)
    skills = extract_skills_from_text(text)

    return {
        "raw_text": text,
        "skills": skills
    }
