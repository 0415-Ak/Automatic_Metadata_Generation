# 📄 Auto Metadata & Summary Generator

A simple yet powerful document intelligence system that extracts structured metadata and generates a clean summary from `.pdf`, `.docx`, or `.txt` files using Natural Language Processing and Large Language Models (LLMs).

---

## 🎬 Overview

This project allows users to upload document files and receive:

- Extracted **metadata** (title, author, date, keywords, type)
- A **concise summary** of the full content
- An interactive and intuitive **Streamlit UI**

It uses **text preprocessing, chunking, vectorization**, and **LLM-based summarization**, with post-processing via KeyBERT to enhance extracted keywords.

---

## ✨ Features

- 📂 File support for `.pdf`, `.docx`, and `.txt`
- ✂️ Text cleaning and preprocessing
- 📑 Metadata extraction using Mistral LLM
- 🧠 Final summary generation across multiple chunks
- 🧷 Keyword extraction using KeyBERT
- 🌐 Streamlit web interface
- 💾 Downloadable output as JSON or text

---

## 📁 Project Structure

   ```  automatic-metadata-summary-generation/
│
├── app.py # Streamlit interface
├── requirements.txt
├── README.md
├── research/
│ └── Automated_Metadata_generation.ipynb
└── src/
├── extractor.py # File reading logic
├── preprocessor.py # Preprocessing text
├── summarizer.py # Chunking + merge summary
├── mistral_api.py # API calls to Mistral
├── prompts.py # Prompt templates
└── utils.py # Helpers, KeyBERT, JSON parsing
```

## 🛠️ Technologies Used

- **Python** – Core programming
- **LangChain** – Chunking and text handling
- **KeyBERT** – Keyword extraction
- **Sentence Transformers** – Embedding model for KeyBERT
- **Streamlit** – Web app interface
- **Mistral API** – LLM for summary + metadata
- **spaCy / NLTK** – NLP preprocessing
- **pdfplumber / python-docx** – File parsing

---

## 📊 Dataset / Input

- Any user-uploaded `.pdf`, `.docx`, or `.txt` file
- Content: Can include research papers, reports, resumes, proposals, etc.
- The document is processed, summarized, and metadata extracted in one go

---

## 🚀 Installation & Setup


# Clone the repository
git clone https://github.com/YOUR_USERNAME/auto-metadata-summary.git
cd auto-metadata-summary

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the Streamlit application
streamlit run app.py


## 📝 License
This project is licensed under the MIT License.


## 👤 Author

-Akshat Jain
-🎓 B.Tech - Mechanical Engineering, IIT Roorkee
-📧 akshat_j1@me.iitr.ac.in
-🌐 GitHub: @0415-Ak
