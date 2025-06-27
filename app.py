import os
import json
import sys
import streamlit as st
from io import StringIO

# Add the path to the 'src' directory
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.extract_text import extract_text_from_file
from src.preprocessor import lightly_clean_text
from src.chunker import split_text_into_chunks
from src.summarizer import generate_all_chunk_summaries, merge_summaries
from src.utils import parse_and_enhance

from dotenv import load_dotenv
load_dotenv()

# =============================
# 🎯 Streamlit App UI
# =============================
st.set_page_config(page_title="📄 AutoMetadata Generator", layout="wide")
st.title("📄 Automated Metadata & Summary Generator")
st.markdown("Upload your PDF, DOCX, or TXT file to extract metadata and a summary.")

# File Upload
uploaded_file = st.file_uploader("Choose a file (.pdf, .docx, .txt)", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    with st.spinner("⏳ Reading and processing file..."):
        # Save and read uploaded file
        ext = uploaded_file.name.split('.')[-1]
        temp_file_path = f"temp_uploaded_file.{ext}"
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.read())

        raw_text = extract_text_from_file(temp_file_path)
        clean_text = lightly_clean_text(raw_text)
        chunks = split_text_into_chunks(clean_text)

    # Trigger summary generation
    if st.button("🚀 Generate Metadata & Summary"):
        with st.spinner("🧠 Generating summary..."):
            chunk_summaries = generate_all_chunk_summaries(chunks)
            final_output = merge_summaries(chunk_summaries)
            parsed = parse_and_enhance(final_output, clean_text)

        # ============================
        # ✅ Final Output Display
        # ============================
        st.subheader("📌 Metadata")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**📘 Title:** {parsed.get('title', 'N/A')}")
            st.markdown(f"**✍️ Author:** {parsed.get('author', 'N/A')}")
            st.markdown(f"**📅 Date:** {parsed.get('date', 'N/A')}")
        with col2:
            st.markdown(f"**📂 Document Type:** {parsed.get('document_type', 'N/A')}")
            st.markdown("**🏷️ Keywords:**")
            st.markdown(", ".join(parsed.get("keywords", [])))

        st.subheader("🧾 Summary")
        st.text_area("Summary", parsed.get("summary", "No summary available."), height=100)

        # ✅ Download Button
        st.download_button(
            label="💾 Download Metadata as JSON",
            data=json.dumps(parsed, indent=2),
            file_name="metadata_summary.json",
            mime="application/json"
        )
