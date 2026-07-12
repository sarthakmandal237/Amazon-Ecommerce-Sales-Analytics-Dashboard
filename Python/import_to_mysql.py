import pandas as pd
from sqlalchemy import create_engine

# Load the cleaned dataset
df = pd.read_csv("../Dataset/amazon_sales_clean.csv")

# MySQL Connection
username = "root"
password = "Sarthak123!"
host = "localhost"
database = "amazon_sales"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

try:
    # Import DataFrame into MySQL
    df.to_sql(
        name="sales",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("===================================")
    print(" Data Imported Successfully!")
    print(" Table Name : sales")
    print(" Total Rows :", len(df))
    print("===================================")

except Exception as e:
    print("Import Failed!")
    print(e)