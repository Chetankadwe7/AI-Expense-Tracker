import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data/processed/cleaned_expenses.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Title
st.title("💰 AI Expense Tracker Pro")

# Total Spend
total = df["Amount"].sum()
st.metric("💸 Total Spend", total)

# Filter
category = st.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[df["Category"].isin(category)]

# Bar Chart
st.subheader("📊 Category-wise Spend")
st.bar_chart(filtered_df.groupby("Category")["Amount"].sum())

# Line Chart
st.subheader("📈 Monthly Trend")
monthly = filtered_df.groupby(filtered_df["Date"].dt.month)["Amount"].sum()
st.line_chart(monthly)

# Alert
if total > 50000:
    st.error("⚠️ Budget Exceeded")
else:
    st.success("✅ Budget Safe")

# Data
if st.checkbox("Show Data"):
    st.dataframe(filtered_df)