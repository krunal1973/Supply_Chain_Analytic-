import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("CUSTOMER ANALYSIS")

# Total Customers
total_customers = (
    df["Customer Id"]
    .nunique()
)

print(f"\nTotal Customers: {total_customers:,}")

# Customer Segments
customer_segments = (
    df["Customer Segment"]
    .value_counts()
)

print("\nCustomer Segments")
print(customer_segments)

# Top Customers By Revenue
top_customers_revenue = (
    df.groupby("Customer Id")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Customers By Revenue")
print(top_customers_revenue.head(10))

# Top Customers By Profit
top_customers_profit = (
    df.groupby("Customer Id")["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Customers By Profit")
print(top_customers_profit.head(10))

# Revenue By Segment
segment_revenue = (
    df.groupby("Customer Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue By Segment")
print(segment_revenue)

# Profit By Segment
segment_profit = (
    df.groupby("Customer Segment")["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProfit By Segment")
print(segment_profit)

# Customer Country Analysis
customer_country = (
    df.groupby("Customer Country")["Customer Id"]
    .nunique()
    .sort_values(ascending=False)
)

print("\nTop 10 Countries By Customers")
print(customer_country.head(10))