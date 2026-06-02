import pandas as pd

df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("MONTHLY SALES TREND")

# Monthly Revenue
monthly_sales = (
    df.groupby(
        ["Order_Year", "Order_Month"]
    )["Sales"]
    .sum()
)

print("\nMonthly Revenue")
print(monthly_sales)

# Monthly Profit
monthly_profit = (
    df.groupby(
        ["Order_Year", "Order_Month"]
    )["Order Profit Per Order"]
    .sum()
)

print("\nMonthly Profit")
print(monthly_profit)