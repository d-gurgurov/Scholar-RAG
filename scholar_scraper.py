import requests
from bs4 import BeautifulSoup
import random

def get_scholar_recommendations(cookies):
    url = "https://scholar.google.com/scholar?sciupd=1&hl=en&as_sdt=0,5"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://scholar.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
        }
    response = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    papers = []
    for result in soup.select('.gs_ora'):
        title = result.select_one('.gs_ora_tt').text
        abstract = result.select_one('.gs_ora_detail').text
        link = result.select_one('.gs_ora_links a')['href']
        papers.append({
            "title": title,
            "abstract": abstract,
            "link": link
        })
    
    return random.sample(papers, min(5, len(papers)))