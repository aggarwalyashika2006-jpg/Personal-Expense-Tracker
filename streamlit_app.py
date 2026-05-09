import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import os

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# =====================================================
# CREATE REQUIRED FOLDERS
# =====================================================

folders = ["data", "outputs", "reports"]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# =====================================================
# DATABASE CONNECTION
# =====================================================

conn = sqlite3.connect(
    "expense_tracker.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Date TEXT,
    Category TEXT,
    Amount REAL,
    Payment_Method TEXT,
    Description TEXT
)
""")

conn.commit()

# =====================================================
# AUTO CATEGORY FUNCTION
# =====================================================

def auto_categorize(description):

    description = str(description).lower()

    if any(word in description for word in
           ["pizza", "food", "restaurant", "burger", "cafe"]):
        return "Food"

    elif any(word in description for word in
             ["uber", "bus", "metro", "taxi", "train"]):
        return "Travel"

    elif any(word in description for word in
             ["movie", "netflix", "gaming"]):
        return "Entertainment"

    elif any(word in description for word in
             ["amazon", "shopping", "clothes"]):
        return "Shopping"

    elif any(word in description for word in
             ["electricity", "bill", "water", "rent"]):
        return "Bills"

    else:
        return "Others"

# =====================================================
# SIDEBAR MENU
# =====================================================

st.sidebar.title("💰 Expense Tracker")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Expense",
        "Upload CSV",
        "View Expenses",
        "Reports"
    ]
)

# =====================================================
# DASHBOARD
# =====================================================

if menu == "Dashboard":

    st.title("📊 Personal Expense Tracker Dashboard")

    df = pd.read_sql(
        "SELECT * FROM expenses",
        conn
    )

    if df.empty:
        st.warning("No expense data available.")
        st.stop()

    # FIXED DATE CONVERSION
    df["Date"] = pd.to_datetime(
        df["Date"],
        format="mixed",
        errors="coerce"
    )

    # REMOVE INVALID DATES
    df.dropna(subset=["Date"], inplace=True)

    # =====================================================
    # SIDEBAR FILTERS
    # =====================================================

    st.sidebar.subheader("Filters")

    category_filter = st.sidebar.multiselect(
        "Select Category",
        options=df["Category"].unique(),
        default=df["Category"].unique()
    )

    payment_filter = st.sidebar.multiselect(
        "Select Payment Method",
        options=df["Payment_Method"].unique(),
        default=df["Payment_Method"].unique()
    )

    filtered_df = df[
        (df["Category"].isin(category_filter)) &
        (df["Payment_Method"].isin(payment_filter))
    ]

    if filtered_df.empty:
        st.warning("No matching data found.")
        st.stop()

    # =====================================================
    # METRICS
    # =====================================================

    total_spending = filtered_df["Amount"].sum()

    average_spending = filtered_df["Amount"].mean()

    highest_category = (
        filtered_df.groupby("Category")["Amount"]
        .sum()
        .idxmax()
    )

    total_transactions = len(filtered_df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Spending",
        f"₹{total_spending:.2f}"
    )

    col2.metric(
        "Average Expense",
        f"₹{average_spending:.2f}"
    )

    col3.metric(
        "Highest Category",
        highest_category
    )

    col4.metric(
        "Transactions",
        total_transactions
    )

    st.divider()

    # =====================================================
    # CATEGORY-WISE SPENDING
    # =====================================================

    st.subheader("📌 Category-wise Spending")

    category_expense = (
        filtered_df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    fig1, ax1 = plt.subplots(figsize=(8, 5))

    sns.barplot(
        x=category_expense.index,
        y=category_expense.values,
        ax=ax1
    )

    plt.xticks(rotation=45)

    plt.ylabel("Amount")

    st.pyplot(fig1)

    fig1.savefig(
        "outputs/category_bar_chart.png"
    )

    # =====================================================
    # MONTHLY TREND
    # =====================================================

    st.subheader("📈 Monthly Spending Trend")

    filtered_df["Month"] = (
        filtered_df["Date"]
        .dt.to_period("M")
        .astype(str)
    )

    monthly_expense = (
        filtered_df.groupby("Month")["Amount"]
        .sum()
    )

    fig2, ax2 = plt.subplots(figsize=(10, 5))

    monthly_expense.plot(
        kind="line",
        marker="o",
        ax=ax2
    )

    plt.ylabel("Amount")

    st.pyplot(fig2)

    fig2.savefig(
        "outputs/monthly_trend.png"
    )

    # =====================================================
    # PAYMENT METHOD ANALYSIS
    # =====================================================

    st.subheader("💳 Payment Method Analysis")

    payment_analysis = (
        filtered_df.groupby("Payment_Method")["Amount"]
        .sum()
    )

    fig3, ax3 = plt.subplots(figsize=(6, 6))

    payment_analysis.plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax3
    )

    plt.ylabel("")

    st.pyplot(fig3)

    fig3.savefig(
        "outputs/payment_method_pie.png"
    )

    # =====================================================
    # DAILY SPENDING TREND
    # =====================================================

    st.subheader("📅 Daily Spending Trend")

    daily_spending = (
        filtered_df.groupby("Date")["Amount"]
        .sum()
    )

    fig4, ax4 = plt.subplots(figsize=(10, 5))

    daily_spending.plot(
        kind="line",
        ax=ax4
    )

    plt.ylabel("Amount")

    st.pyplot(fig4)

    fig4.savefig(
        "outputs/daily_spending_trend.png"
    )

    # =====================================================
    # DATA TABLE
    # =====================================================

    st.subheader("📄 Expense Data")

    st.dataframe(filtered_df)

# =====================================================
# ADD EXPENSE
# =====================================================

elif menu == "Add Expense":

    st.title("➕ Add New Expense")

    with st.form("expense_form"):

        expense_date = st.date_input(
            "Select Date"
        )

        amount = st.number_input(
            "Enter Amount",
            min_value=1.0
        )

        payment_method = st.selectbox(
            "Payment Method",
            ["Cash", "UPI", "Card"]
        )

        description = st.text_input(
            "Expense Description"
        )

        submitted = st.form_submit_button(
            "Add Expense"
        )

        if submitted:

            category = auto_categorize(description)

            cursor.execute("""
            INSERT INTO expenses
            (Date, Category, Amount, Payment_Method, Description)
            VALUES (?, ?, ?, ?, ?)
            """, (
                str(expense_date),
                category,
                amount,
                payment_method,
                description
            ))

            conn.commit()

            st.success(
                "Expense Added Successfully!"
            )

            st.info(
                f"Auto Categorized as: {category}"
            )

# =====================================================
# CSV UPLOAD
# =====================================================

elif menu == "Upload CSV":

    st.title("📂 Upload Expense CSV")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("Dataset Preview")

        st.dataframe(df.head())

        required_columns = [
            "Date",
            "Amount",
            "Payment_Method",
            "Description"
        ]

        if all(col in df.columns for col in required_columns):

            # FIX DATE FORMAT
            df["Date"] = pd.to_datetime(
                df["Date"],
                format="mixed",
                errors="coerce"
            )

            # REMOVE INVALID DATES
            df.dropna(subset=["Date"], inplace=True)

            # CONVERT BACK TO STRING
            df["Date"] = df["Date"].astype(str)

            # AUTO CATEGORY
            df["Category"] = df["Description"].apply(
                auto_categorize
            )

            # STORE IN DATABASE
            df.to_sql(
                "expenses",
                conn,
                if_exists="append",
                index=False
            )

            st.success(
                "CSV Uploaded Successfully!"
            )

        else:

            st.error("""
            CSV must contain:
            Date, Amount,
            Payment_Method, Description
            """)

# =====================================================
# VIEW EXPENSES
# =====================================================

elif menu == "View Expenses":

    st.title("📋 View Expenses")

    df = pd.read_sql(
        "SELECT * FROM expenses ORDER BY Date DESC",
        conn
    )

    if df.empty:

        st.warning(
            "No expense records found."
        )

    else:

        st.dataframe(df)

        st.subheader("Expense Summary")

        st.write(
            f"Total Transactions: {len(df)}"
        )

        st.write(
            f"Total Spending: ₹{df['Amount'].sum():.2f}"
        )

# =====================================================
# REPORTS
# =====================================================

elif menu == "Reports":

    st.title("📑 Expense Reports")

    df = pd.read_sql(
        "SELECT * FROM expenses",
        conn
    )

    if df.empty:

        st.warning("No data available.")

    else:

        # FIXED DATE CONVERSION
        df["Date"] = pd.to_datetime(
            df["Date"],
            format="mixed",
            errors="coerce"
        )

        # REMOVE INVALID DATES
        df.dropna(subset=["Date"], inplace=True)

        # CREATE MONTH COLUMN
        df["Month"] = (
            df["Date"]
            .dt.to_period("M")
            .astype(str)
        )

        # MONTHLY REPORT
        monthly_report = (
            df.groupby(
                ["Month", "Category"]
            )["Amount"]
            .sum()
            .reset_index()
        )

        st.subheader(
            "Monthly Expense Report"
        )

        st.dataframe(monthly_report)

        # SAVE REPORT
        report_path = (
            "reports/monthly_expense_report.csv"
        )

        monthly_report.to_csv(
            report_path,
            index=False
        )

        st.success(
            "Report Generated Successfully!"
        )

        # DOWNLOAD BUTTON
        with open(report_path, "rb") as file:

            st.download_button(
                label="⬇ Download Report",
                data=file,
                file_name="monthly_expense_report.csv",
                mime="text/csv"
            )

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "Personal Expense Tracker with Data Visualization using Python, SQLite, Pandas, and Streamlit"
)