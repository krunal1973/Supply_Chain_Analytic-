import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("SHIPPING MODE CHART")

shipping_mode = (
    df["Shipping Mode"]
    .value_counts()
)

plt.figure(figsize=(8,6))

shipping_mode.plot(kind="bar")

plt.title("Orders By Shipping Mode")

plt.xlabel("Shipping Mode")

plt.ylabel("Orders")

plt.tight_layout()

plt.savefig(
    "../Visualizations/shipping_mode.png"
)

plt.show()