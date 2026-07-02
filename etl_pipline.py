import pandas as pd
from sqlalchemy import create_engine
import urllib.parse
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# 1. EXTRACT
df = pd.read_csv('sales_data.csv')
print("Data extracted successfully.")

# 2. TRANSFORM
df.columns = df.columns.str.strip()
df.drop_duplicates(inplace=True)
df['Price'] = df['Price'].fillna(df['Price'].median())
df['Total_Revenue'] = df['Quantity'] * df['Price']

# 3. LOAD
# Get the password securely from the environment
password = os.getenv("DB_PASSWORD")
encoded_password = urllib.parse.quote_plus(password)

db_url = f'postgresql+psycopg2://postgres:{encoded_password}@localhost:5432/sales_db'
engine = create_engine(db_url)

try:
    df.to_sql('sales_records', engine, if_exists='replace', index=False)
    print("Success! Data loaded into PostgreSQL table 'sales_records'.")
except Exception as e:
    print(f"Database error: {e}")