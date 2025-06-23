import re
import json
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer





def extract_json_from_output(output: str) -> dict:
    try:
        # 1. Try parsing directly (ideal case — yours!)
        return json.loads(output)
    except json.JSONDecodeError:
        pass  # try fallback

    try:
        # 2. Try to extract using backtick block (```json ... ```)
        json_block = re.search(r'```json\n(.*?)```', output, re.DOTALL)
        if json_block:
            return json.loads(json_block.group(1))

        # 3. Try generic JSON block (first `{...}` in output)
        json_text = re.search(r'(\{.*?\})', output, re.DOTALL).group(1)
        return json.loads(json_text)

    except Exception as e:
        print(f"⚠️ JSON extraction failed: {e}")
        return {"error": "Could not parse JSON"}




# ✅ Improve keywords using KeyBERT
def improve_keywords_from_text(clean_text: str, top_n=10) -> list:
    kw_model = KeyBERT(model=SentenceTransformer('all-MiniLM-L6-v2'))
    keywords = kw_model.extract_keywords(
        clean_text,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        top_n=top_n,
        use_maxsum=True,
        nr_candidates=20
    )
    return [kw for kw, _ in keywords]

# ✅ Combine everything into one helper
def parse_and_enhance(llm_output: str, clean_text: str) -> dict:
    parsed = extract_json_from_output(llm_output)
    parsed["keywords"] = improve_keywords_from_text(clean_text)
    return parsed
