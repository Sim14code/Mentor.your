
from dotenv import load_dotenv
from rag_pipeline import retrieve_context
from quiz_engine import generate_quiz
from revision_planner import get_revision_plan
from openai import AzureOpenAI
import tiktoken
import time
import os

# Setup client
client = AzureOpenAI(
     api_key=os.getenv("AZURE_OPENAI_API_KEY"),
     api_version=os.getenv("AZURE_OPENAI_VERSION"),
     azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Generic explanation
def explanation_agent(query, context):
    prompt = f"""
You are a Study Mentor. Use the following material to answer the question.
Context: {context[:2000] if context else "None"}
Question: {query}
Answer:"""

    encoding = tiktoken.encoding_for_model("gpt-4")
    print("📏 Tokens:", len(encoding.encode(prompt)))

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

# PDF-aware pipeline
def run_multi_agent_pipeline(query, context_text=None):
    if "quiz" in query.lower():
        return generate_quiz(query, context_text)
    elif "revise" in query.lower():
        return get_revision_plan(query, context_text)
    else:
        return explanation_agent(query, context_text)
