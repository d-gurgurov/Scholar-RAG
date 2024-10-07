from scholar_scraper import get_scholar_recommendations
from rag_implementation import setup_rag, get_paper_description

from tqdm import tqdm
from datetime import datetime
import warnings

# Silence specific deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")
warnings.filterwarnings("ignore", category=FutureWarning, module="transformers")

import json

# Function to load cookies from a JSON file
def load_cookies(file_path):
    with open(file_path, 'r') as f:
        cookies = json.load(f)
    return cookies

def main():
    print(f"\nScholar Update Run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # Get Google Scholar cookies
    cookies = load_cookies('/Users/daniilgurgurov/Desktop/projects/cookies.json')

    print("Fetching and analyzing recent papers from Google Scholar...")
    print("=" * 80)

    # Fetch recent papers
    papers = get_scholar_recommendations(cookies)

    # Setup RAG
    db, chain = setup_rag(papers)

    # Generate descriptions
    for paper in tqdm(papers, desc="Processing Papers", unit="paper"):
        description = get_paper_description(db, chain, paper)
        print(f"Title: {paper['title']}")
        print(f"Description: {description}")
        print("-----------------------------------------------")

if __name__ == "__main__":
    main()