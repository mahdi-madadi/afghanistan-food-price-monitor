CREATE DATABASE IF NOT EXISTS afghanistan_food_prices
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE afghanistan_food_prices;

CREATE TABLE monthly_food_prices (
    market VARCHAR(50) NOT NULL,
    commodity VARCHAR(80) NOT NULL,
    price_month DATE NOT NULL,
    price_afn_per_kg DECIMAL(12, 6) NOT NULL,

    PRIMARY KEY (market, commodity, price_month),

    CONSTRAINT chk_positive_food_price
        CHECK (price_afn_per_kg > 0)
);

SHOW COLUMNS FROM monthly_food_prices;