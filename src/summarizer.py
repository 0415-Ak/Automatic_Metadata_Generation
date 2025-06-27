import os
import sys

# Add the path to the 'src' directory
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


from src.llm_call import call_chunk_summary, call_combined_summary

def generate_all_chunk_summaries(chunks: list) -> list:
    """
    Generates summaries for each text chunk.
    """
    results = []
    for i, chunk in enumerate(chunks):
        print(f"\n📦 Generating summary for Chunk {i+1}/{len(chunks)}")
        summary = call_chunk_summary(chunk)
        results.append(summary)
    return results

def merge_summaries(chunk_summaries: list) -> str:
    """
    Merges all chunk summaries into final metadata + summary output.
    """
    return call_combined_summary(chunk_summaries)