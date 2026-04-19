import pandas as pd
import numpy as np
import os

def generate_data():
    np.random.seed(42)

    os.makedirs("data/raw", exist_ok=True)

    dates = pd.date_range(start="2024-01-01", periods=200)
    categories = ["Food", "Travel", "Bills", "Shopping", "Entertainment"]

    data = {
        "Date": np.random.choice(dates, 200),
        "Category": np.random.choice(categories, 200),
        "Amount": np.random.randint(100, 5000, 200),
    }

    df = pd.DataFrame(data)
    df.to_csv("data/raw/expenses.csv", index=False)

    print("✅ Data Generated")

if __name__ == "__main__":
    generate_data()