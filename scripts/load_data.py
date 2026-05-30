import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv("data/bank-marketing-dirty.csv", sep=";")

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# Replace missing indicators
df.replace(["unknown", "N/A", ""], pd.NA, inplace=True)

# Remove duplicates
df = df.drop_duplicates()

# Fill numeric missing values
numeric_cols = df.select_dtypes(include=["number"]).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill text missing values
text_cols = df.select_dtypes(include=["object", "string"]).columns

for col in text_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Save cleaned CSV
df.to_csv("data/bank-marketing-clean.csv", index=False)

# PostgreSQL connection
engine = create_engine(
    "postgresql://admin:admin@localhost:5432/bankdb"
)

# Load data into PostgreSQL
df.to_sql(
    "bank_marketing",
    engine,
    if_exists="replace",
    index=False
)

print("\nData loaded into PostgreSQL successfully!")