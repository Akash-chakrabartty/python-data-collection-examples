from pathlib import Path
import pandas as pd
import time
import random

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def collect_sensor_data():
    rows = []

    # 100 ta fake sensor reading
    for i in range(100):
        rows.append({
            "reading_id": i + 1,
            "timestamp": time.time(),
            "temperature_c": round(random.uniform(20.0, 32.0), 2),
            "humidity_pct": round(random.uniform(40.0, 70.0), 2)
        })
        # real sensor hole ekhane time.sleep lagte parto
        time.sleep(0.01)   # choto delay, jeno timestamp change hoy

    df = pd.DataFrame(rows)
    df.to_csv(DATA_DIR / "sensor_data.csv", index=False)
    print("Sensor Data Saved Successfully ✔️")

if __name__ == "__main__":
    collect_sensor_data()
