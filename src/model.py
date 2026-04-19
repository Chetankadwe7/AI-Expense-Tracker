import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predict():
    df = pd.read_csv("data/processed/cleaned_expenses.csv")

    monthly = df.groupby("Month")["Amount"].sum()

    X = monthly.index.values.reshape(-1, 1)
    y = monthly.values

    model = LinearRegression()
    model.fit(X, y)

    next_month = np.array([[max(monthly.index) + 1]])
    pred = model.predict(next_month)

    print(f"\n📈 Predicted Next Month Expense: ₹{pred[0]:.2f}")