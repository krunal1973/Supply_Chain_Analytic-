import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "../Data/Processed_Data/supply_chain_clean.csv",
    low_memory=False
)

# Data Quality Report
print("DATA QUALITY REPORT")

# shape 
print("\nDataset Shape")
print(df.shape)

# missing values
missing = pd.DataFrame({
    "Missing_Count": df.isnull().sum(),
    "Missing_Percent": round(
        (df.isnull().sum() / len(df)) * 100,
        2
    )
})

missing = missing[missing["Missing_Count"] > 0]

print("\nMissing Values")
print(missing.sort_values(
    by="Missing_Percent",
    ascending=False
))
 
# data range 
print("\nOrder Date Range")

print(
    df["order date (DateOrders)"].min(),
    "to",
    df["order date (DateOrders)"].max()
)

# unique customers
print("\nUnique Customers")

print(df["Customer Id"].nunique())

# unique products
print("\nUnique Products")

print(df["Product Card Id"].nunique()) 

# unique categories
print("\nUnique Categories")

print(df["Category Name"].nunique())

# Shipping Delay Stats
print("\nShipping Delay Summary")

print(df["Shipping_Delay"].describe()) 

# Sales Summary 
print("\nSales Summary")

print(df["Sales"].describe())

print("\nReport Complete") 