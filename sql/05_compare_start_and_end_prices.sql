SELECT
    latest.market,
    latest.commodity,
    first.price_afn_per_kg AS january_2023_price,
    latest.price_afn_per_kg AS december_2025_price,
    ROUND(
        100.0 * (
            latest.price_afn_per_kg - first.price_afn_per_kg
        ) / first.price_afn_per_kg,
        2
    ) AS change_since_january_2023_pct
FROM monthly_food_prices AS latest
JOIN monthly_food_prices AS first
    ON latest.market = first.market
   AND latest.commodity = first.commodity
WHERE first.price_month = '2023-01-01'
  AND latest.price_month = '2025-12-01'
ORDER BY change_since_january_2023_pct DESC,
         latest.market,
         latest.commodity;