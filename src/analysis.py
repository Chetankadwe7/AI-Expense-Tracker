import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze():
    df = pd.read_csv("data/processed/cleaned_expenses.csv")

    total_spend = df["Amount"].sum()
    category_spend = df.groupby("Category")["Amount"].sum()

    print("\n📊 Total Spend:", total_spend)
    print("\n📊 Category-wise Spend:\n", category_spend)

    os.makedirs("outputs/charts", exist_ok=True)
    os.makedirs("outputs/reports", exist_ok=True)

    # Bar Chart
    plt.figure(figsize=(8,5))
    category_spend.plot(kind='bar')
    plt.title("Category-wise Spending")
    plt.tight_layout()
    plt.savefig("outputs/charts/category_chart.png")
    plt.close()

    # Pie Chart
    plt.figure()
    category_spend.plot(kind='pie', autopct='%1.1f%%')
    plt.ylabel("")
    plt.title("Expense Distribution")
    plt.savefig("outputs/charts/pie_chart.png")
    plt.close()

    # Report
    with open("outputs/reports/summary.txt", "w") as f:
        f.write(f"Total Spend: {total_spend}\n\n")
        f.write("Category-wise Spend:\n")
        f.write(str(category_spend))

    print("✅ Charts & report saved")