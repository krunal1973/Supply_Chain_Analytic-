import pandas as pd

df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("CUSTOMER SEGMENT ANALYSIS")

# Revenue By Segment
segment_sales = (
    df.groupby("Customer Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue By Segment")
print(segment_sales)

# Profit By Segment
segment_profit = (
    df.groupby("Customer Segment")["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProfit By Segment")
print(segment_profit)

# Customers By Segment
segment_customers = (
    df.groupby("Customer Segment")["Customer Id"]
    .nunique()
    .sort_values(ascending=False)
)

print("\nCustomers By Segment")
print(segment_customers)