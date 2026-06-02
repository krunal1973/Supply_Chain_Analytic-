import pandas as pd

df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("PRODUCT ANALYSIS")

# Top Products By Revenue
top_revenue = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Products By Revenue")
print(top_revenue.head(10))

# Top Products By Profit
top_profit = (
    df.groupby("Product Name")["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Products By Profit")
print(top_profit.head(10))

# Loss Making Products
loss_products = (
    df.groupby("Product Name")["Order Profit Per Order"]
    .sum()
    .sort_values()
)

print("\nTop 10 Loss Making Products")
print(loss_products.head(10)) 