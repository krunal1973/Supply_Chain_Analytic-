import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("SUPPLY CHAIN KPI ANALYSIS")

# Revenue
total_revenue = df["Sales"].sum()

# Profit
total_profit = df["Order Profit Per Order"].sum()

# Orders
total_orders = df["Order Id"].nunique()

# Customers
total_customers = df["Customer Id"].nunique()

# Average Order Value
avg_order_value = total_revenue / total_orders

# Profit Margin
profit_margin = (
    total_profit / total_revenue
) * 100

# Delivery Performance
late_delivery_pct = (
    df["Late_delivery_risk"].mean()
) * 100

on_time_delivery_pct = (
    100 - late_delivery_pct
)

# KPI Output
print(f"\nTotal Revenue: ₹{total_revenue:,.2f}")

print(f"Total Profit: ₹{total_profit:,.2f}")

print(f"Total Orders: {total_orders:,}")

print(f"Total Customers: {total_customers:,}")

print(f"Average Order Value: ₹{avg_order_value:,.2f}")

print(f"Profit Margin: {profit_margin:.2f}%")

print(f"On-Time Delivery: {on_time_delivery_pct:.2f}%")

print(f"Late Delivery: {late_delivery_pct:.2f}%")