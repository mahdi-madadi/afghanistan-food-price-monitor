# Afghanistan Food Price Monitor

## Business question
How did prices of selected staple foods change across five Afghan
markets between January 2023 and December 2025?

## Data
Source: WFP Afghanistan price export, downloaded 11 November 2026.

Scope:
- Markets: Balkh, Hirat, Kabul, Kandahar, and Nangarhar.
- Commodities: low-quality rice, low-quality wheat flour, and cooking oil.
- Aggregated retail prices in AFN/kg.
- 540 observations covering 36 months.
- Forecast records excluded.

## Tools and workflow
- Python: inspect, filter, validate, and visualize the data.
- MySQL: store monthly prices and calculate monthly and yearly changes.
- Excel: independently validate selected SQL calculations.
- Power BI: build an interactive dashboard with commodity and market filters.

## Key findings
- Rice prices increased 25.41% in Kandahar and 18.97% in Kabul
  between January 2023 and December 2025.
- In December 2025, rice prices ranged from 45.00 AFN/kg in
  Nangarhar to 82.50 AFN/kg in Kabul.
- Kandahar rice prices increased 35.78% in the final month,
  highlighting the importance of examining the full time series.
- Wheat flour prices declined 40.30% in Balkh over the study period.

## Quality checks
- Unique market–commodity–month combinations.
- Complete coverage: 5 markets × 3 commodities × 36 months.
- Positive prices and no missing required fields.
- Expected missing comparisons: 15 monthly and 180 yearly.
- Selected calculations matched across SQL, Excel, and Power BI.
- Dashboard filters and exported PDF checked.

## Limitations
The analysis covers selected markets and commodities. It does not
measure national inflation or household affordability, and it does
not establish the causes of price changes.