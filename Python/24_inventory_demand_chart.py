import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("INVENTORY DEMAND CHART")

# Product Demand
product_demand = (
    df.groupby("Product Name")
    ["Order Item Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

product_demand.plot(kind="bar")

plt.title("Top 10 Products By Demand")

plt.xlabel("Product")

plt.ylabel("Quantity")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig(
    "../Visualizations/inventory_demand.png"
)

plt.show()