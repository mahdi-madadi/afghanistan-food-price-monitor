# Data Dictionary

File: data_processed/food_price_dashboard.csv

One row represents one market, one commodity, and one month.
Unique key: market + commodity + price_month.
Total rows: 540.

| Column | Meaning |
|---|---|
| market | Market name as supplied in the WFP export |
| commodity | Commodity name as supplied in the WFP export |
| price_month | Month represented by the observation, stored as the first day of that month |
| price_afn_per_kg | Aggregated retail price in Afghan afghanis per kilogram |
| previous_month_price | Price for the same market and commodity in the previous calendar month |
| previous_year_price | Price for the same market and commodity in the same month of the previous year |
| monthly_change_rate | Current price divided by previous-month price, minus 1 |
| yearly_change_rate | Current price divided by previous-year price, minus 1 |

## Scope
- January 2023–December 2025.
- Balkh, Hirat, Kabul, Kandahar, and Nangarhar.
- Rice (low quality), Wheat flour (low quality), and Oil (cooking).
- Aggregated records only; forecast records excluded.
- Retail prices, AFN currency, KG unit.

## Missing values
The first month has no previous-month comparison:
15 missing monthly comparisons.

The first 12 months have no previous-year comparison:
180 missing yearly comparisons.

These values remain missing rather than being replaced with zero.

## Percentage conventions
Dashboard CSV columns ending in _rate contain fractions:
0.10 means a 10% increase.

SQL view columns ending in _pct contain percentage-point numbers:
10.00 means a 10% increase.

## Date preparation
Original observation dates were normalized to the first day of
their month. This date identifies the reporting month; it does
not indicate that the price was collected on that day.