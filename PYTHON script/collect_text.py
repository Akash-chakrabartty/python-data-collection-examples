from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

TEXT_DIR = Path("text_files")
TEXT_DIR.mkdir(exist_ok=True)

def collect_text_files():
    # jodi kono .txt file na thake, tahole ekta sample file create kore nebo
    if not any(TEXT_DIR.glob("*.txt")):
        sample_path = TEXT_DIR / "sample.txt"
        sample_path.write_text(
            "Hello Akash!\nThis is a sample text file created automatically.",
            encoding="utf-8"
        )
        print("No .txt files found, created sample.txt inside text_files folder ✔️")

    rows = []
    for path in TEXT_DIR.glob("*.txt"):
        content = path.read_text(encoding="utf-8", errors="ignore")
        rows.append({
            "file_name": path.name,
            "content": content
        })

    df = pd.DataFrame(rows)
    df.to_csv(DATA_DIR / "text_files.csv", index=False)
    print("Text Files Saved Successfully ✔️")

if __name__ == "__main__":
    collect_text_files()
