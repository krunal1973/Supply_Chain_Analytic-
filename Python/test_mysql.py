from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = "Krun@l#1973"

engine = create_engine(
    f"mysql+pymysql://root:{quote_plus(password)}@localhost:3306/supply_chain_db"
)

with engine.connect() as conn:
    print("Connected Successfully")