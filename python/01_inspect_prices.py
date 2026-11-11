from pathlib import Path

import pandas as pd

project_folder = Path(__file__).resolve().parents[1]
source_file = (
    project_folder / "raw_data" / "wfp_afghanistan_prices_export.csv"
)

prices = pd.read_csv(source_file, encoding="utf-8-sig")

prices["Price Date"] = pd.to_datetime(
    prices["Price Date"],
    format="%d/%m/%Y",
    errors="raise",
)

print(f"Total rows: {len(prices):,}")
print(f"Markets: {prices['Market Name'].nunique()}")
print(f"Commodities: {prices['Commodity'].nunique()}")

print("\nRows by data type:")
print(prices["Data Type"].value_counts())

print("\nDate coverage by data type:")
print(
    prices.groupby("Data Type")["Price Date"]
    .agg(["min", "max"])
)

print("\nUnits:")
print(prices["Unit"].value_counts())