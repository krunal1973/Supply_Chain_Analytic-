import pandas as pd 


file_path= "../Data/Raw_Data/DataCoSupplyChainDataset.csv"

df=pd.read_csv(file_path, encoding="latin1", low_memory=False)

# Display the first few rows of the dataset
print("\nDataset Shape: ", df.shape)

print("\nFirst 10 columns: ", df.columns[:10].tolist())

print("\nData Types: ",df.dtypes)

print("\nMissind values: ", df.isnull().sum())

print("\nDuplicate rows: ",df.duplicated().sum())

print("\nSummary Usage (MB): ", round(df.memory_usage(deep=True).sum() / 1024**2,2))
