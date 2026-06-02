import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("CATEGORY SALES CHART")

category_sales = (
    df.groupby("Category Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

category_sales.plot(kind="bar")

plt.title("Top 10 Categories By Sales")

plt.xlabel("Category")

plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    "../Visualizations/category_sales.png"
)

plt.show()