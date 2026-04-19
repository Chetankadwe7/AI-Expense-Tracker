import pandas as pd
import os

def clean_data():
    os.makedirs("data/processed", exist_ok=True)

    df = pd.read_csv("data/raw/expenses.csv")

    df = df.drop_duplicates()
    df["Date"] = pd.to_datetime(df["Date"])
    df["Amount"] = pd.to_numeric(df["Amount"])

    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day

    df.to_csv("data/processed/cleaned_expenses.csv", index=False)

    print("✅ Data Cleaned")

if __name__ == "__main__":
    clean_data()