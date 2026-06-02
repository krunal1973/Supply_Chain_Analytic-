import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("DELIVERY PERFORMANCE ANALYSIS")

# Delivery Status
delivery_status = (
    df["Delivery Status"]
    .value_counts()
)

print("\nDelivery Status")
print(delivery_status)

# Shipping Mode
shipping_mode = (
    df["Shipping Mode"]
    .value_counts()
)

print("\nShipping Mode")
print(shipping_mode)

# Shipping Delay Summary
print("\nShipping Delay Summary")
print(df["Shipping_Delay"].describe())

# Late Delivery Risk
late_delivery_pct = (
    df["Late_delivery_risk"]
    .mean() * 100
)

print(
    f"\nLate Delivery Risk: "
    f"{late_delivery_pct:.2f}%"
)

# Average Delay by Region
region_delay = (
    df.groupby("Order Region")["Shipping_Delay"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Regions by Average Delay")
print(region_delay)

# Average Delay by Market
market_delay = (
    df.groupby("Market")["Shipping_Delay"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Delay by Market")
print(market_delay)