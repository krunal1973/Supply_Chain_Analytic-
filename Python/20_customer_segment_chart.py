import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("CUSTOMER SEGMENT CHART")

segment_sales = (
    df.groupby("Customer Segment")["Sales"]
    .sum()
)

plt.figure(figsize=(8,6))

segment_sales.plot(kind="pie")

plt.ylabel("")

plt.title("Revenue By Customer Segment")

plt.tight_layout()

plt.savefig(
    "../Visualizations/customer_segment.png"
)

plt.show()
