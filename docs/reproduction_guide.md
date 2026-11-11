# Reproduction Guide

## Requirements
- Python with pandas and matplotlib
- MySQL 8.0 or later
- Microsoft Excel
- Power BI Desktop

Run Python commands from the project’s root folder.

## 1. Prepare the source data
Place the original WFP export at:
raw_data/wfp_afghanistan_prices_export.csv

The analysis uses aggregated retail prices in AFN/kg for:
- Balkh, Hirat, Kabul, Kandahar, and Nangarhar.
- Rice (low quality), Wheat flour (low quality), and Oil (cooking).
- January 2023–December 2025.

Forecast records are excluded.

## 2. Run Python preparation
Run in this order:

python python/01_inspect_prices.py
python python/02_prepare_prices.py
python python/03_plot_rice_prices.py

Expected clean dataset:
data_processed/food_prices_clean.csv

Expected size: 540 rows.
Expected chart: reports/rice_price_trends.png

## 3. Load and analyze in MySQL
Run sql/01_create_database_and_table.sql.

Import food_prices_clean.csv into monthly_food_prices using
MySQL Workbench’s Table Data Import Wizard. Import only once
into an empty table.

Run scripts 02 through 07 in numerical order.

Expected checks:
- 540 rows.
- 5 markets, 3 commodities, 36 months.
- 15 missing monthly comparisons.
- 180 missing yearly comparisons.

Script 04 supplies selected results for comparison with Excel.

## 4. Export dashboard data
Run sql/08_export_dashboard_data.sql.

Export the complete 540-row result, including column headers, as:
data_processed/food_price_dashboard.csv

The monthly_change_rate and yearly_change_rate fields contain
fractions suitable for percentage formatting.

## 5. Validate in Excel
Open excel/Food_Price_Validation.xlsx.

Review the previous-month and previous-year lookup formulas
and the corresponding percentage changes.

Selected results should match SQL and Power BI.

## 6. Refresh Power BI
Open powerbi/Afghanistan_Food_Price_Monitor.pbix.

In Power Query, update the CSV source path to the local location
of food_price_dashboard.csv, then refresh.

With filters cleared, the Data Checks page should show:
- Price Records: 540.
- Missing Monthly Comparisons: 15.
- Missing Yearly Comparisons: 180.

On the overview, select Rice (low quality) and all markets.
For December 2025, verify:
- Kabul price: 82.50 AFN/kg.
- Kandahar price: 52.50 AFN/kg.
- Kandahar monthly change: 35.78%.
- Kandahar yearly change: 34.50%.

## 7. Review outputs
Check the dashboard screenshot and exported report PDF in reports/.

Results describe selected markets and commodities and do not
represent national inflation.