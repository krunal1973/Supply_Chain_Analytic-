import pandas as pd

df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("INVENTORY DEMAND ANALYSIS")

# Product Demand
product_demand = (
    df.groupby("Product Name")
    ["Order Item Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 20 Products By Demand")
print(product_demand.head(20))

# Category Demand
category_demand = (
    df.groupby("Category Name")
    ["Order Item Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nDemand By Category")
print(category_demand)