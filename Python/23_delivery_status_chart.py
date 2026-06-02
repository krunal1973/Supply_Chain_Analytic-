import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

print("DELIVERY STATUS CHART")

# Delivery Status
delivery_status = (
    df["Delivery Status"]
    .value_counts()
)

plt.figure(figsize=(8,6))

delivery_status.plot(kind="bar")

plt.title("Delivery Status Distribution")

plt.xlabel("Status")

plt.ylabel("Orders")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "../Visualizations/delivery_status.png"
)

plt.show()