# 🔹 Prompt to process a single text chunk
PROMPT_TEMPLATE = """
You are an intelligent assistant designed to understand documents and extract structured information from them.

Your task is to:
1. Extract the following metadata:
   - Title (if mentioned)
   - Author (if available)
   - Date of publication or document creation (if available)
   - Keywords or topics covered
   - Type of document (choose from: research paper, legal notice, resume, report, book chapter, article, business proposal, letter, others)
2. Generate a concise summary of the content (3-5 sentences).

Read the content below and return your answer in this JSON format:
{{
  "title": "",
  "author": "",
  "date": "",
  "keywords": [],
  "document_type": "",
  "summary": ""
}}

Content:
\"\"\"{content_chunk}\"\"\"
"""

# 🔹 Prompt to combine all summaries into final metadata + summary
FINAL_PROMPT_TEMPLATE = """
You are a smart assistant. Below are multiple partial summaries of a document, generated from different parts.

Your task is to combine them into a **single metadata + summary JSON**, like this:
{{
  "title": "",
  "author": "",
  "date": "",
  "keywords": [],
  "document_type": "",
  "summary": ""
}}

⚠️ Very Important Instructions:
-🛑 Do NOT concatenate titles or authors. Choose only one most relevant value.
- ❌ DO NOT include any markdown formatting (no ```json or backticks)
- ❌ DO NOT add any explanations, notes, or comments
- ✅ ONLY return a valid JSON object, with all keys present
- ✅ "keywords" must be a list of strings
- ✅ The output must be machine-readable using json.loads()
- ✅ Give the summary around 500 to 1000 characters 

Summaries:
\"\"\"{combined_summaries}\"\"\"
"""

