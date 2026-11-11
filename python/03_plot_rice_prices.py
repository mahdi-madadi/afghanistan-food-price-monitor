from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

project = Path(__file__).resolve().parents[1]
source = project / "data_processed" / "food_prices_clean.csv"
output = project / "reports" / "rice_price_trends.png"

prices = pd.read_csv(source, parse_dates=["price_month"])

rice = prices.loc[
    prices["commodity"].eq("Rice (low quality)")
]

trends = rice.pivot(
    index="price_month",
    columns="market",
    values="price_afn_per_kg",
).sort_index()

fig, ax = plt.subplots(figsize=(11, 6))

for market in trends.columns:
    ax.plot(
        trends.index.to_pydatetime(),
        trends[market],
        label=market,
        linewidth=2,
    )

ax.set_xlim(trends.index.min(), trends.index.max())

ax.set_title("Rice prices across five Afghan markets, 2023–2025")
ax.set_xlabel("")
ax.set_ylabel("Retail price (AFN per kg)")
ax.set_ylim(bottom=0)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.grid(axis="y", alpha=0.25)
ax.legend(title="Market", loc="upper left", frameon=False)

fig.text(
    0.01, 0.01,
    "Source: WFP export | Rice (low quality) | Aggregated retail prices",
    fontsize=9,
)
fig.tight_layout(rect=[0, 0.04, 1, 1])

output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output, dpi=180)
plt.close(fig)

print(f"Chart saved to {output}")