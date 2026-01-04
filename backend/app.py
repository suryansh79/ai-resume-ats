from flask import Flask, request, jsonify
from flask_cors import CORS
from services.resume_service import extract_resume_text

app = Flask(__name__)
CORS(app)

@app.route("/api/resume/upload", methods=["POST"])
def upload_resume():
    # Check if file is present
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    # Allow only PDF files
    if not file.filename.lower().endswith(".pdf"):
        return jsonify({"error": "Only PDF files are allowed"}), 400

    # Extract text from resume
    text = extract_resume_text(file)

    return jsonify({
        "message": "Resume uploaded successfully",
        "extracted_text_length": len(text)
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
