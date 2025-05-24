from flask import Flask, request, jsonify
from agents import run_multi_agent_pipeline
from extract_pdf import extract_text_from_pdf
from rag_pipeline import retrieve_context
from quiz_engine import generate_quiz
from revision_planner import get_revision_plan
from agents import explanation_agent  # or just define it in same file
from flask import Flask, request, jsonify
from agents import run_multi_agent_pipeline
from extract_pdf import extract_text_from_pdf
import tempfile



app = Flask(__name__)

@app.route("/api/query", methods=["POST"])
def handle_query():
    query = request.form.get("query")
    file = request.files.get("file")
    context = None

    # Extract PDF content if file exists
    if file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            file.save(temp_pdf.name)
            context = extract_text_from_pdf(temp_pdf.name)

    # Now run the agent pipeline with or without context
    answer = run_multi_agent_pipeline(query, context_text=context)

    return jsonify({"answer": answer})



if __name__ == "__main__":
   
    app.run(debug=True)


