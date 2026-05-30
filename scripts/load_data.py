import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv("data/bank-marketing-dirty.csv", sep=";")

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# Replace dirty values with NULL
df.replace(
    ["unknown", "UNKNOWN", "Unknown", "N/A", "?", ""],
    pd.NA,
    inplace=True
)

# Remove duplicates
df = df.drop_duplicates()

# Normalize text columns
text_cols = df.select_dtypes(include=["object", "string"]).columns

for col in text_cols:
    df[col] = (
        df[col]
        .astype("string")
        .str.strip()
        .str.lower()
    )

# Force numeric columns
numeric_columns = [
    "age",
    "balance",
    "day",
    "duration",
    "campaign",
    "pdays",
    "previous"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Fill numeric missing values
for col in numeric_columns:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

# Fill text missing values
text_cols = df.select_dtypes(include=["object", "string"]).columns

for col in text_cols:
    if not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

# Save cleaned dataset
df.to_csv("data/bank-marketing-clean.csv", index=False)

# PostgreSQL connection
engine = create_engine(
    "postgresql://admin:admin@localhost:5432/bankdb"
)

# Load into PostgreSQL
df.to_sql(
    "bank_marketing",
    engine,
    if_exists="replace",
    index=False
)

print("\nCleaned dataset saved successfully!")
print("Data loaded into PostgreSQL successfully!")