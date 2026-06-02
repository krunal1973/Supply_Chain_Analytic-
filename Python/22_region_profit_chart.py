import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("REGION PROFIT CHART")

# Region Profit
region_profit = (
    df.groupby("Order Region")
    ["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

region_profit.plot(kind="bar")

plt.title("Top 10 Regions By Profit")

plt.xlabel("Region")

plt.ylabel("Profit")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "../Visualizations/region_profit.png"
)

plt.show()