def retrieve_context(query, context_text=None):
    # Simplified placeholder: if extracted text from PDF, use it
    if context_text:
        return context_text[:2000]  # limit for prompt
    else:
        return "No additional context provided."
