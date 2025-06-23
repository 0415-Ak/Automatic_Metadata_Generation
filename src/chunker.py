from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text_into_chunks(text, chunk_size=1500, chunk_overlap=100):
    """
    Splits the input text into overlapping chunks using RecursiveCharacterTextSplitter.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)