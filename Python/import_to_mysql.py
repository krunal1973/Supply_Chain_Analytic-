import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = "Krun@l#1973"

engine = create_engine(
    f"mysql+pymysql://root:{quote_plus(password)}@localhost:3306/supply_chain_db"
)

print("Reading CSV...")

df = pd.read_csv(
    r"D:\DataAnalytics\Projects\Supply Chain Analytics\Data\Processed_Data\supply_chain_clean.csv"
)

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("Importing to MySQL...")

df.to_sql(
    name="supply_chain",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=5000
)

print("Import Completed Successfully!")