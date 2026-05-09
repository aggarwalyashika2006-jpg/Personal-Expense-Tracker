import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from datetime import datetime
import os

# Create folders
folders = ["data", "outputs", "reports"]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# -----------------------------
# CREATE SYNTHETIC DATASET
# -----------------------------

data = {
    "Date": pd.date_range(start="2025-01-01", periods=100),
    "Category": np.random.choice(
        ["Food", "Travel", "Shopping", "Bills", "Entertainment"],
        100
    ),
    "Amount": np.random.randint(100, 5000, 100),
    "Payment_Method": np.random.choice(
        ["Cash", "UPI", "Card"],
        100
    ),
    "Description": np.random.choice(
        ["Lunch", "Bus", "Amazon", "Electricity", "Movie"],
        100
    )
}

df = pd.DataFrame(data)

# Save CSV
csv_path = "data/expenses.csv"
df.to_csv(csv_path, index=False)

print("Synthetic dataset created.")

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv(csv_path)

print("\nDataset Preview:")
print(df.head())

# -----------------------------
# DATA CLEANING
# -----------------------------

df.drop_duplicates(inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

df.dropna(inplace=True)

# -----------------------------
# SQLITE DATABASE
# -----------------------------

conn = sqlite3.connect("expense_tracker.db")

df.to_sql("expenses", conn, if_exists="replace", index=False)

print("\nData stored in SQLite database.")

# -----------------------------
# CATEGORY-WISE ANALYSIS
# -----------------------------

category_expense = df.groupby("Category")["Amount"].sum()

print("\nCategory-wise Spending:")
print(category_expense)

# -----------------------------
# MONTHLY ANALYSIS
# -----------------------------

df["Month"] = df["Date"].dt.to_period("M")

monthly_expense = df.groupby("Month")["Amount"].sum()

print("\nMonthly Spending:")
print(monthly_expense)

# -----------------------------
# PAYMENT METHOD ANALYSIS
# -----------------------------

payment_analysis = df.groupby("Payment_Method")["Amount"].sum()

print("\nPayment Method Analysis:")
print(payment_analysis)

# -----------------------------
# HIGHEST SPENDING CATEGORY
# -----------------------------

highest_category = category_expense.idxmax()

print(f"\nHighest Spending Category: {highest_category}")

# -----------------------------
# AVERAGE DAILY SPENDING
# -----------------------------

daily_spending = df.groupby("Date")["Amount"].sum()

average_daily = daily_spending.mean()

print(f"\nAverage Daily Spending: ₹{average_daily:.2f}")

# -----------------------------
# VISUALIZATIONS
# -----------------------------

sns.set(style="whitegrid")

# CATEGORY BAR CHART
plt.figure(figsize=(8, 5))
category_expense.plot(kind="bar")
plt.title("Category-wise Spending")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("outputs/category_bar_chart.png")
plt.close()

# MONTHLY LINE CHART
plt.figure(figsize=(8, 5))
monthly_expense.plot(kind="line", marker="o")
plt.title("Monthly Spending Trend")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("outputs/monthly_trend.png")
plt.close()

# PAYMENT METHOD PIE CHART
plt.figure(figsize=(6, 6))
payment_analysis.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Payment Method Distribution")
plt.tight_layout()
plt.savefig("outputs/payment_method_pie.png")
plt.close()

# DAILY SPENDING TREND
plt.figure(figsize=(10, 5))
daily_spending.plot(kind="line")
plt.title("Daily Spending Trend")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("outputs/daily_spending_trend.png")
plt.close()

print("\nCharts saved in outputs folder.")

# -----------------------------
# REPORT GENERATION
# -----------------------------

report = {
    "Highest Spending Category": [highest_category],
    "Average Daily Spending": [average_daily],
    "Total Spending": [df["Amount"].sum()]
}

report_df = pd.DataFrame(report)

report_df.to_csv("reports/monthly_report.csv", index=False)

print("\nMonthly report generated.")

print("\nPROJECT EXECUTION COMPLETED.")