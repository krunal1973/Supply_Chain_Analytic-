import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("MARKET AND REGION ANALYSIS")

# Revenue By Market
market_revenue = (
    df.groupby("Market")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue By Market")
print(market_revenue)

# Profit By Market
market_profit = (
    df.groupby("Market")["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProfit By Market")
print(market_profit)

# Revenue By Region
region_revenue = (
    df.groupby("Order Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Regions By Revenue")
print(region_revenue.head(10))

# Profit By Region
region_profit = (
    df.groupby("Order Region")["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Regions By Profit")
print(region_profit.head(10))

# Revenue By Country
country_revenue = (
    df.groupby("Order Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Countries By Revenue")
print(country_revenue.head(10))

# Profit By Country
country_profit = (
    df.groupby("Order Country")["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Countries By Profit")
print(country_profit.head(10))

# Market Summary
market_summary = (
    df.groupby("Market")
    .agg(
        Revenue=("Sales", "sum"),
        Profit=("Order Profit Per Order", "sum"),
        Orders=("Order Id", "nunique")
    )
    .sort_values(
        by="Revenue",
        ascending=False
    )
)

print("\nMarket Summary")
print(market_summary)