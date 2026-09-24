from pathlib import Path
from datetime import datetime
import random
import pandas as pd

FILE = Path("sales.csv")
COLUMNS = ["date", "product", "region", "revenue"]

PRODUCTS = ["iPhone", "iPad", "MacBook", "AirPods"]
REGIONS = ["East", "North", "South", "West"]


def update_dataset() -> None:
    if FILE.exists() and FILE.stat().st_size > 0:
        df = pd.read_csv(FILE)
    else:
        df = pd.DataFrame(columns=COLUMNS)

    new_rows = [
        {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "product": random.choice(PRODUCTS),
            "region": random.choice(REGIONS),
            "revenue": random.randint(5000, 50000),
        }
        for _ in range(50)
    ]

    updated = pd.concat(
        [df, pd.DataFrame(new_rows, columns=COLUMNS)],
        ignore_index=True,
    )

    updated.to_csv(FILE, index=False)
    print(f"Dataset updated: {len(new_rows)} new rows added.")


if __name__ == "__main__":
    update_dataset()
