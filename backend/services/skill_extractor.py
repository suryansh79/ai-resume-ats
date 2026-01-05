import json
import re

SKILLS_FILE_PATH = "data/skills.json"


def load_skills():
    
    with open(SKILLS_FILE_PATH, "r") as file:
        return json.load(file)


def extract_skills_from_text(text):
    
    skills_data = load_skills()
    extracted_skills = set()

    
    text = text.lower()

    for category in skills_data:
        for skill in skills_data[category]:
            pattern = r"\b" + re.escape(skill) + r"\b"
            if re.search(pattern, text):
                extracted_skills.add(skill)

    return sorted(list(extracted_skills))
