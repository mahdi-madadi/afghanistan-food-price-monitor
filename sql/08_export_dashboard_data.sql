SELECT
    market,
    commodity,
    price_month,
    price_afn_per_kg,
    previous_month_price,
    previous_year_price,
    monthly_change_pct / 100.0 AS monthly_change_rate,
    yearly_change_pct / 100.0 AS yearly_change_rate
FROM afghanistan_food_prices.food_price_changes
ORDER BY market, commodity, price_month;