
from openai import AzureOpenAI
from dotenv import load_dotenv
import os


client = AzureOpenAI(
         api_key=os.getenv("AZURE_OPENAI_API_KEY"),
         api_version=os.getenv,
         azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# ✅ Updated Quiz Generator
def generate_quiz(query, context=None):
    context_snippet = context[:2000] if context else 'None'

    prompt = f"""
You are a Quiz Master AI. Generate 5 multiple-choice questions from the topic and study material.

Topic: {query}
Context: {context_snippet}

For each question, provide: 
- One question
- Four options (A, B, C, D) on new diffrent lines
- The correct answer on a new line

Format:
Q. ... (next line)
A. ...(next line)
B. ...(next line)
C. ...(next line)
D. ...(next line)
Answer: ...(next line)
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
