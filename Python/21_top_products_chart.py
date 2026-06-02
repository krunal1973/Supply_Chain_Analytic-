import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("TOP PRODUCTS CHART")

# Top Products
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

top_products.plot(kind="bar")

plt.title("Top 10 Products By Revenue")

plt.xlabel("Product")

plt.ylabel("Revenue")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig(
    "../Visualizations/top_products.png"
)

plt.show()