from pathlib import Path
import pandas as pd
import requests

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def collect_from_rest_api():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # jodi error thake tahole exception dibe
    data = response.json()

    df = pd.DataFrame(data)
    df.to_csv(DATA_DIR / "posts_api.csv", index=False)
    print("API Data Saved Successfully ✔️")

if __name__ == "__main__":
    collect_from_rest_api()
