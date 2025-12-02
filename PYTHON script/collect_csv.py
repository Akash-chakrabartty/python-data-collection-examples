from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def collect_csv_or_excel():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = pd.read_csv(url)
    df.to_csv(DATA_DIR / "iris_sample.csv", index=False)
    print("CSV Saved Successfully ✔️")

if __name__ == "__main__":
    collect_csv_or_excel()
