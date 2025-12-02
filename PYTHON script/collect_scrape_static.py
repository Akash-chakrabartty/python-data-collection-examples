from pathlib import Path
import pandas as pd
import requests
from bs4 import BeautifulSoup

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def scrape_static_website():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    rows = []
    for q in soup.select(".quote"):
        text = q.find("span", class_="text").get_text(strip=True)
        author = q.find("small", class_="author").get_text(strip=True)
        rows.append({"quote": text, "author": author})

    df = pd.DataFrame(rows)
    df.to_csv(DATA_DIR / "quotes_static.csv", index=False)
    print("Static Scraping Saved Successfully ✔️")

if __name__ == "__main__":
    scrape_static_website()
