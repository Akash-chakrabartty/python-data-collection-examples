from pathlib import Path
import pandas as pd
import json

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

JSON_DIR = Path("json_files")
JSON_DIR.mkdir(exist_ok=True)

def collect_json_files():
    # jodi kono .json na thake, ekta sample create korbo
    if not any(JSON_DIR.glob("*.json")):
        sample_path = JSON_DIR / "sample.json"
        sample_data = {
            "id": 1,
            "name": "Akash",
            "course": "Machine Learning",
            "marks": 92
        }
        sample_path.write_text(json.dumps(sample_data, indent=2), encoding="utf-8")
        print("No .json files found, created sample.json inside json_files folder ✔️")

    records = []
    for path in JSON_DIR.glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"Skip {path.name}: {e}")
            continue

        if isinstance(data, dict):
            rec = {"file_name": path.name}
            rec.update(data)
            records.append(rec)
        else:
            records.append({"file_name": path.name, "data": json.dumps(data)})

    df = pd.DataFrame(records)
    df.to_csv(DATA_DIR / "json_data.csv", index=False)
    print("JSON Data Saved Successfully ✔️")

if __name__ == "__main__":
    collect_json_files()
