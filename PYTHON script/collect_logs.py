from pathlib import Path
import pandas as pd
import re

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

LOG_DIR = Path("log_files")
LOG_DIR.mkdir(exist_ok=True)

def collect_log_files():
    # If no log files exist, create a sample log file
    sample_log = LOG_DIR / "app.log"
    if not any(LOG_DIR.glob("*.log")):
        sample_text = """
[INFO] App started successfully
[DEBUG] Loading configuration
[ERROR] Failed to load module X
[WARN] Low memory detected
[INFO] User logged in
"""
        sample_log.write_text(sample_text.strip(), encoding="utf-8")
        print("No .log files found → Created sample app.log ✔️")

    # Regex pattern to extract log level and message
    pattern = re.compile(r"\[(INFO|ERROR|WARN|DEBUG)\]\s*(.*)")

    rows = []
    for file in LOG_DIR.glob("*.log"):
        for line in file.read_text(encoding="utf-8").splitlines():
            match = pattern.search(line)
            if match:
                rows.append({
                    "file_name": file.name,
                    "level": match.group(1),
                    "message": match.group(2)
                })

    df = pd.DataFrame(rows)
    df.to_csv(DATA_DIR / "log_data.csv", index=False)
    print("Log Data Saved Successfully ✔️")

if __name__ == "__main__":
    collect_log_files()
