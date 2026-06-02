import pandas as pd 
import os 

file_path= "../Data/Raw_Data/DataCoSupplyChainDataset.csv"

df=pd.read_csv(file_path, encoding="latin1", low_memory=False)
print("Original Shape: ",df.shape)

# Dpor useless columns
drop_cols= [ 
    "Customer Email",
    "Customer Password",
    "Product Description",
    "Product Image"
]
df.drop(columns=drop_cols, inplace=True)

# fix missing values 
df["Customer Lname"] = df["Customer Lname"].fillna("Unknown")

df["Customer Zipcode"] = (
    df["Customer Zipcode"]
    .fillna(df["Customer Zipcode"].median())
)

# convert dates 
df["order date (DateOrders)"] = pd.to_datetime(
    df["order date (DateOrders)"],
    errors="coerce"
)

df["shipping date (DateOrders)"] = pd.to_datetime(
    df["shipping date (DateOrders)"],
    errors="coerce"
)

# create date features 
df["Order_Year"] = df["order date (DateOrders)"].dt.year

df["Order_Month"] = df["order date (DateOrders)"].dt.month

df["Order_Day"] = df["order date (DateOrders)"].dt.day

df["Order_Quarter"] = df["order date (DateOrders)"].dt.quarter

# shipping delay
df["Shipping_Delay"] = (
    df["Days for shipping (real)"]
    - df["Days for shipment (scheduled)"]
)

# save cleaned dataset 
output_folder = "../Data/Processed_Data"

os.makedirs(output_folder, exist_ok=True)

output_file = (
    "../Data/Processed_Data/supply_chain_clean.csv"
)

df.to_csv(output_file, index=False)

print("\nCleaned Shape:", df.shape)

print("\nSaved Successfully")
print(output_file)