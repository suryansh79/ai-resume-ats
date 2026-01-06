from flask import Flask, request, jsonify
from flask_cors import CORS
from services.resume_service import analyze_resume
from services.job_matcher import match_resume_to_job


app = Flask(__name__)
CORS(app)

# Day 1: Upload-only endpoint
@app.route("/api/resume/upload", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    if not file.filename.lower().endswith(".pdf"):
        return jsonify({"error": "Only PDF files are allowed"}), 400

    result = analyze_resume(file)

    return jsonify({
        "message": "Resume uploaded successfully",
        "extracted_text_length": len(result["raw_text"])
    }), 200


# Day 2: Resume analysis endpoint (SKILLS)
@app.route("/api/resume/analyze", methods=["POST"])
def analyze_resume_api():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    if not file.filename.lower().endswith(".pdf"):
        return jsonify({"error": "Only PDF files are allowed"}), 400

    result = analyze_resume(file)

    return jsonify({
        "message": "Resume analyzed successfully",
        "skills": result["skills"]
    }), 200

@app.route("/api/jobs/match", methods=["POST"])
def match_job_api():
    if "resume" not in request.files:
        return jsonify({"error": "No resume uploaded"}), 400

    job_role = request.form.get("job_role")

    if not job_role:
        return jsonify({"error": "Job role is required"}), 400

    file = request.files["resume"]

    if not file.filename.lower().endswith(".pdf"):
        return jsonify({"error": "Only PDF files are allowed"}), 400

   
    resume_result = analyze_resume(file)
    resume_skills = resume_result["skills"]

   
    match_result = match_resume_to_job(resume_skills, job_role)

    return jsonify({
        "message": "Job matching completed",
        "resume_skills": resume_skills,
        "job_match": match_result
    }), 200


if __name__ == "__main__":
    app.run(debug=True)


