from src.data_generator import generate_data
from src.preprocessing import clean_data
from src.analysis import analyze
from src.model import predict
from src.utils import budget_alert
import pandas as pd

generate_data()
clean_data()
analyze()
predict()

df = pd.read_csv("data/processed/cleaned_expenses.csv")
total = df["Amount"].sum()

print("\n", budget_alert(total))