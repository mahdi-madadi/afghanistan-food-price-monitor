SELECT
    market,
    commodity,
    price_month,
    previous_month_price,
    price_afn_per_kg,
    ROUND(monthly_change_pct, 2) AS monthly_change_pct
FROM afghanistan_food_prices.food_price_changes
WHERE market = 'Kandahar'
  AND commodity = 'Rice (low quality)'
  AND monthly_change_pct IS NOT NULL
ORDER BY ABS(monthly_change_pct) DESC,
         price_month
LIMIT 3;