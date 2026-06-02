import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("SHIPPING MODE ANALYSIS")

# Orders By Shipping Mode
orders_by_mode = (
    df.groupby("Shipping Mode")["Order Id"]
    .nunique()
    .sort_values(ascending=False)
)

print("\nOrders By Shipping Mode")
print(orders_by_mode)

# Revenue By Shipping Mode
revenue_by_mode = (
    df.groupby("Shipping Mode")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue By Shipping Mode")
print(revenue_by_mode)

# Profit By Shipping Mode
profit_by_mode = (
    df.groupby("Shipping Mode")["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProfit By Shipping Mode")
print(profit_by_mode)

# Average Delay By Shipping Mode
delay_by_mode = (
    df.groupby("Shipping Mode")["Shipping_Delay"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Delay By Shipping Mode")
print(delay_by_mode)

# Late Delivery Risk
late_risk = (
    df.groupby("Shipping Mode")["Late_delivery_risk"]
    .mean() * 100
)

print("\nLate Delivery Risk (%)")
print(late_risk.sort_values(ascending=False))