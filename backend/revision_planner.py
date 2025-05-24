from openai import AzureOpenAI
from dotenv import load_dotenv
import os


# ✅ Define your Azure OpenAI client (if not already)
client = AzureOpenAI(
     api_key=os.getenv("AZURE_OPENAI_API_KEY"),
     api_version=os.getenv("AZURE_OPENAI_VERSION"),
     azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")


)

def get_revision_plan(query, context=None):
    context_snippet = context[:2000] if context else 'None'

    prompt = f"""
You are an Exam Coach AI. Create a focused 5-day revision plan for the topic.

Topic: {query}
Context: {context_snippet}

Break it into:
- Day 1: ...
- Day 2: ...
- Day 3: ...
- Day 4: ...
- Day 5: ...

Use bullet points or subtopics to guide the study plan. Be concise but complete.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )

    return response.choices[0].message.content.strip()
