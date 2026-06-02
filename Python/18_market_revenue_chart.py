import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("MARKET REVENUE CHART")

market_revenue = (
    df.groupby("Market")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12,6))

market_revenue.plot(kind="bar")

plt.title("Revenue By Market")

plt.xlabel("Market")

plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    "../Visualizations/market_revenue.png"
)

plt.show()
