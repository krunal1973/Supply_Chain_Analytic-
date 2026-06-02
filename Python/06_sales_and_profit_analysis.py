import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("SALES AND PROFIT ANALYSIS")

# Category Sales
category_sales = (
    df.groupby("Category Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Categories By Sales")
print(category_sales.head(10))

# Category Profit
category_profit = (
    df.groupby("Category Name")["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Categories By Profit")
print(category_profit.head(10))

# Top Products By Revenue
top_products_revenue = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Products By Revenue")
print(top_products_revenue.head(10))

# Top Products By Profit
top_products_profit = (
    df.groupby("Product Name")["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Products By Profit")
print(top_products_profit.head(10))

# Loss Making Products
loss_products = (
    df.groupby("Product Name")["Order Profit Per Order"]
    .sum()
    .sort_values()
)

print("\nTop 10 Loss Making Products")
print(loss_products.head(10))

# Profit Margin By Category
profit_margin = (
    df.groupby("Category Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Order Profit Per Order", "sum")
    )
)

profit_margin["Profit_Margin_%"] = (
    profit_margin["Profit"]
    / profit_margin["Sales"]
) * 100

profit_margin = profit_margin.sort_values(
    by="Profit_Margin_%",
    ascending=False
)

print("\nTop Categories By Profit Margin")
print(
    profit_margin[
        ["Profit_Margin_%"]
    ].head(10)
)