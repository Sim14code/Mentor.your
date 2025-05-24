from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import os
endpoint = os.getenv("AZURE_DOCUMENT_ANALYSIS_ENDPOINT")
key = os.getenv("AZURE_DOCUMENT_ANALYSIS_KEY")
client = DocumentAnalysisClient(endpoint, AzureKeyCredential(key))

def extract_text_from_pdf(file):
    poller = client.begin_analyze_document("prebuilt-layout", document=file)
    result = poller.result()
    all_text = ""
    for page in result.pages:
        for line in page.lines:
            all_text += line.content + "\n"
    return all_text
