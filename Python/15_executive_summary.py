import pandas as pd

df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("EXECUTIVE SUMMARY")

# Revenue
total_revenue = df["Sales"].sum()

# Profit
total_profit = df["Order Profit Per Order"].sum()

# Orders
total_orders = df["Order Id"].nunique()

# Customers
total_customers = df["Customer Id"].nunique()

# Average Order Value
avg_order_value = (
    total_revenue / total_orders
)

print(f"\nRevenue : ₹{total_revenue:,.2f}")
print(f"Profit : ₹{total_profit:,.2f}")
print(f"Orders : {total_orders:,}")
print(f"Customers : {total_customers:,}")
print(f"Average Order Value : ₹{avg_order_value:,.2f}")