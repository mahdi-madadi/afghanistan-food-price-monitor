SELECT
    price_month,
    price_afn_per_kg,
    ROUND(monthly_change_pct, 2) AS monthly_change_pct,
    ROUND(yearly_change_pct, 2) AS yearly_change_pct
FROM afghanistan_food_prices.food_price_changes
WHERE market = 'Kabul'
  AND commodity = 'Rice (low quality)'
  AND price_month BETWEEN '2024-01-01' AND '2024-03-01'
ORDER BY price_month;