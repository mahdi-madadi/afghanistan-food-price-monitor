SELECT
    market,
    commodity,
    COUNT(monthly_change_pct) AS monthly_comparisons,
    ROUND(AVG(ABS(monthly_change_pct)), 2)
        AS average_absolute_monthly_change_pct,
    ROUND(MAX(ABS(monthly_change_pct)), 2)
        AS largest_absolute_monthly_change_pct
FROM afghanistan_food_prices.food_price_changes
GROUP BY market, commodity
ORDER BY AVG(ABS(monthly_change_pct)) DESC,
         market,
         commodity
LIMIT 5;