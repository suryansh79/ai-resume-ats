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

    # Weighted scoring
    required_score = len(matched_required) / len(required_skills) if required_skills else 0
    optional_score = len(matched_optional) / len(optional_skills) if optional_skills else 0

    final_score = round((required_score * 0.8 + optional_score * 0.2) * 100, 2)

    # Hiring signal
    if final_score >= 75:
        verdict = "Strong Match"
    elif final_score >= 50:
        verdict = "Moderate Match"
    else:
        verdict = "Weak Match"

    return {
        "job_role": job_role,
        "match_percentage": final_score,
        "verdict": verdict,
        "matched_required_skills": sorted(matched_required),
        "matched_optional_skills": sorted(matched_optional),
        "missing_required_skills": sorted(missing_required)
    }
def rank_resume_against_all_jobs(resume_skills):
    jobs = load_jobs()
    results = []

    for job_role in jobs.keys():
        match = match_resume_to_job(resume_skills, job_role)
        results.append(match)

    # Sort by highest match percentage
    results.sort(key=lambda x: x["match_percentage"], reverse=True)

    return results

