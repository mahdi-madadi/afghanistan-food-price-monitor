# Power BI Measures

Table name: FoodPrices

## Validation

```DAX
Price Records = COUNTROWS(FoodPrices)
```

```DAX
Missing Monthly Comparisons =
COUNTBLANK(FoodPrices[monthly_change_rate])
```

```DAX
Missing Yearly Comparisons =
COUNTBLANK(FoodPrices[yearly_change_rate])
```

With all filters cleared, expected results are 540, 15, and 180.

## Price

```DAX
Average Price AFN per KG =
AVERAGE(FoodPrices[price_afn_per_kg])
```

Each trend-chart point represents one market, one commodity,
and one month. The commodity slicer uses single selection.

```DAX
Latest Price AFN per KG =
VAR LatestMonth =
    MAX(FoodPrices[price_month])
RETURN
    CALCULATE(
        [Average Price AFN per KG],
        FoodPrices[price_month] = LatestMonth
    )
```

## Price changes

```DAX
Latest Monthly Change % =
VAR LatestMonth =
    MAX(FoodPrices[price_month])
RETURN
    CALCULATE(
        AVERAGE(FoodPrices[monthly_change_rate]),
        FoodPrices[price_month] = LatestMonth
    )
```

```DAX
Latest Yearly Change % =
VAR LatestMonth =
    MAX(FoodPrices[price_month])
RETURN
    CALCULATE(
        AVERAGE(FoodPrices[yearly_change_rate]),
        FoodPrices[price_month] = LatestMonth
    )
```

Price measures display two decimal places.
Change measures use percentage formatting with two decimal places;
their source columns contain fractions.

Latest measures use the latest month available in the current
filter context. In the complete dataset, this is December 2025.
Comparison tables omit totals because averaging market prices or
market growth rates requires separate interpretation.