import json

JOBS_FILE_PATH = "data/jobs.json"


def load_jobs():
   
    with open(JOBS_FILE_PATH, "r") as file:
        return json.load(file)


def match_resume_to_job(resume_skills, job_role):
    
    jobs = load_jobs()

    if job_role not in jobs:
        raise ValueError("Job role not found")

    job = jobs[job_role]

    required_skills = set(job["required_skills"])
    optional_skills = set(job["optional_skills"])
    resume_skills = set(resume_skills)

    matched_required = resume_skills & required_skills
    matched_optional = resume_skills & optional_skills
    missing_required = required_skills - resume_skills

    match_percentage = round(
        (len(matched_required) / len(required_skills)) * 100, 2
    )

    return {
        "job_role": job_role,
        "match_percentage": match_percentage,
        "matched_required_skills": sorted(list(matched_required)),
        "matched_optional_skills": sorted(list(matched_optional)),
        "missing_required_skills": sorted(list(missing_required))
    }
