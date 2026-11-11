USE afghanistan_food_prices;

SELECT
    COUNT(*) AS price_records,
    COUNT(DISTINCT market) AS markets,
    COUNT(DISTINCT commodity) AS commodities,
    COUNT(DISTINCT price_month) AS months,
    MIN(price_month) AS first_month,
    MAX(price_month) AS last_month
FROM monthly_food_prices;