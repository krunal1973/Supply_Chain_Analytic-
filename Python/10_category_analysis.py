import pandas as pd

df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("CATEGORY ANALYSIS")

# Revenue By Category
category_sales = (
    df.groupby("Category Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue By Category")
print(category_sales)

# Profit By Category
category_profit = (
    df.groupby("Category Name")["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProfit By Category")
print(category_profit)

# Orders By Category
category_orders = (
    df.groupby("Category Name")["Order Id"]
    .nunique()
    .sort_values(ascending=False)
)

print("\nOrders By Category")
print(category_orders)