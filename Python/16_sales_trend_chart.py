import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("SALES TREND CHART")

# Monthly Sales
monthly_sales = (
    df.groupby(
        ["Order_Year", "Order_Month"]
    )["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Period"] = (
    monthly_sales["Order_Year"].astype(str)
    + "-"
    + monthly_sales["Order_Month"].astype(str)
)

# Plot
plt.figure(figsize=(12,6))

plt.plot(
    monthly_sales["Period"],
    monthly_sales["Sales"]
)

plt.title("Monthly Sales Trend")

plt.xlabel("Period")

plt.ylabel("Sales")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig(
    "../Visualizations/sales_trend.png"
)

plt.show()