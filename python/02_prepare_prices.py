from pathlib import Path

import pandas as pd

project = Path(__file__).resolve().parents[1]
source = project / "raw_data" / "wfp_afghanistan_prices_export.csv"
output = project / "data_processed" / "food_prices_clean.csv"

markets = ["Kabul", "Kandahar", "Hirat", "Nangarhar", "Balkh"]
commodities = [
    "Wheat flour (low quality)",
    "Rice (low quality)",
    "Oil (cooking)",
]

prices = pd.read_csv(source, encoding="utf-8-sig")
prices["Price Date"] = pd.to_datetime(
    prices["Price Date"], format="%d/%m/%Y", errors="raise"
)

selection = (
    prices["Country"].eq("Afghanistan")
    & prices["Data Type"].eq("Aggregated")
    & prices["Price Type"].eq("Retail")
    & prices["Currency"].eq("AFN")
    & prices["Unit"].eq("KG")
    & prices["Market Name"].isin(markets)
    & prices["Commodity"].isin(commodities)
    & prices["Price Date"].between("2023-01-01", "2025-12-31")
)

clean = prices.loc[
    selection,
    ["Market Name", "Commodity", "Price Date", "Price"],
].copy()

clean = clean.rename(columns={
    "Market Name": "market",
    "Commodity": "commodity",
    "Price Date": "price_month",
    "Price": "price_afn_per_kg",
})

# Use the first day to represent each monthly period.
clean["price_month"] = (
    clean["price_month"].dt.to_period("M").dt.to_timestamp()
)
clean["price_afn_per_kg"] = pd.to_numeric(
    clean["price_afn_per_kg"], errors="raise"
)

key = ["market", "commodity", "price_month"]

assert not clean.isna().any().any(), "Missing values found"
assert clean["price_afn_per_kg"].gt(0).all(), "Nonpositive prices found"
assert not clean.duplicated(key).any(), "Duplicate monthly records found"

expected = pd.MultiIndex.from_product(
    [
        markets,
        commodities,
        pd.date_range("2023-01-01", "2025-12-01", freq="MS"),
    ],
    names=key,
)
actual = pd.MultiIndex.from_frame(clean[key])
assert len(expected.difference(actual)) == 0, "Expected months are missing"
assert len(actual.difference(expected)) == 0, "Unexpected records found"
assert len(clean) == 540, "Unexpected row count"

clean = clean.sort_values(key)
output.parent.mkdir(parents=True, exist_ok=True)
clean.to_csv(
    output, index=False, date_format="%Y-%m-%d", float_format="%.6f"
)

print(f"Saved {len(clean):,} rows to {output.name}")
print(clean.groupby(["market", "commodity"]).size())