CREATE OR REPLACE VIEW food_price_changes AS
WITH previous_prices AS (
    SELECT
        market,
        commodity,
        price_month,
        price_afn_per_kg,

        LAG(price_afn_per_kg, 1) OVER (
            PARTITION BY market, commodity
            ORDER BY price_month
        ) AS previous_month_price,

        LAG(price_afn_per_kg, 12) OVER (
            PARTITION BY market, commodity
            ORDER BY price_month
        ) AS previous_year_price

    FROM monthly_food_prices
)
SELECT
    *,
    100.0 * (price_afn_per_kg - previous_month_price)
        / NULLIF(previous_month_price, 0) AS monthly_change_pct,

    100.0 * (price_afn_per_kg - previous_year_price)
        / NULLIF(previous_year_price, 0) AS yearly_change_pct

FROM previous_prices;