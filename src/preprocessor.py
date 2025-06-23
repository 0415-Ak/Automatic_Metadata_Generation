import re

def lightly_clean_text(text):
    """
    Performs light cleaning on the input text:
    - Replaces non-breaking spaces with normal space
    - Removes extra whitespaces and newlines
    """
    text = text.replace('\xa0', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
