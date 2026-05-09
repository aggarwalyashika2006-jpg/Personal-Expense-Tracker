# 💰 Personal Expense Tracker with Data Visualization

A Python-based Personal Expense Tracker built using Streamlit, Pandas, SQLite, Matplotlib, and Seaborn that helps users record, analyze, visualize, and manage their daily expenses efficiently.

---

# 🚀 Live Demo

🌐 Demo Link:  
[Personal Expense Tracker Demo](https://personal-expense-tracker-d4xm4e3hobwx9upgjy6dji.streamlit.app/?utm_source=chatgpt.com)

---

# 📌 Project Overview

Managing personal finances manually can be difficult and time-consuming. This project provides an easy-to-use expense tracking system where users can:

- Add daily expenses
- Upload expense CSV files
- Automatically categorize expenses
- Analyze spending habits
- Visualize expense trends
- Generate downloadable reports

The project simulates a real-world finance tracking application and demonstrates Python development, data analysis, visualization, automation, and dashboard creation skills.

---

# 🎯 Problem Statement

People often struggle to:
- Track where money is spent
- Identify unnecessary expenses
- Maintain monthly budgets
- Analyze financial habits

This application solves these problems through automated analysis and interactive visual dashboards.

---

# ✨ Features

## ✅ Expense Management
- Add expenses manually
- Upload CSV expense files
- View all expense records

## ✅ Auto Expense Categorization
Expenses are automatically categorized into:
- Food
- Travel
- Shopping
- Bills
- Entertainment
- Others

## ✅ Data Storage
- SQLite database integration
- Persistent local storage

## ✅ Financial Analytics
- Total spending
- Average expense
- Highest spending category
- Payment method analysis
- Monthly spending trends

## ✅ Data Visualization
- Category-wise bar chart
- Monthly spending line chart
- Payment method pie chart
- Daily spending trend chart

## ✅ Report Generation
- Download monthly expense reports as CSV

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Streamlit | Web Dashboard |
| Pandas | Data Analysis |
| NumPy | Numerical Operations |
| SQLite | Database |
| Matplotlib | Charts |
| Seaborn | Data Visualization |

---

# 📂 Project Structure

```text
Personal-Expense-Tracker-Visualization/
│
├── data/
├── outputs/
├── reports/
├── images/
├── notebooks/
├── src/
├── app.py
├── requirements.txt
├── README.md
└── expense_tracker.db
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd Personal-Expense-Tracker-Visualization
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

```bash
streamlit run app.py
```

---

# 📊 Dashboard Functionalities

## 📌 Dashboard
- Total spending metrics
- Category-wise spending
- Monthly trends
- Payment analysis

## ➕ Add Expense
- Add expenses manually
- Auto categorization

## 📂 Upload CSV
Upload CSV files with:
- Date
- Amount
- Payment_Method
- Description

## 📋 View Expenses
- View all stored transactions

## 📑 Reports
- Generate downloadable monthly reports

---

# 📈 Generated Visualizations

The application generates:

- 📊 Category-wise Bar Chart
- 📈 Monthly Spending Trend
- 🥧 Payment Method Pie Chart
- 📅 Daily Spending Trend

Charts are automatically saved inside the `outputs/` folder.

---

# 🧠 Auto Categorization Logic

The application automatically categorizes expenses using keywords.

Example:

| Description | Category |
|---|---|
| Pizza | Food |
| Uber Ride | Travel |
| Amazon Order | Shopping |
| Electricity Bill | Bills |

---

# 💾 SQLite Database

The application stores expense data in SQLite database:

```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Date TEXT,
    Category TEXT,
    Amount REAL,
    Payment_Method TEXT,
    Description TEXT
);
```

---

# 📑 Sample CSV Format

```csv
Date,Amount,Payment_Method,Description
2025-01-01,250,UPI,Pizza
2025-01-02,120,Cash,Bus Ticket
2025-01-03,1800,Card,Amazon Shopping
```

---

# 📚 Learning Outcomes

This project helped in learning:

- Python Development
- Data Cleaning
- Data Visualization
- Streamlit Dashboard Development
- SQLite Database Integration
- Financial Analytics
- Report Automation
- GitHub Project Structuring

---

# 🔥 Industry Relevance

This project is useful for roles like:

- Python Developer
- Data Analyst
- Business Analyst
- Financial Analyst
- Automation Engineer
- Dashboard Developer

---

# 🚀 Future Enhancements

- AI-based expense prediction
- Budget alerts
- OCR bill scanning
- Banking API integration
- Cloud database support
- User authentication system
- Mobile app integration

---

# 🧪 Sample Insights

The system can identify:
- Highest spending category
- Monthly overspending trends
- Frequently used payment methods
- Average daily spending

---

# 👨‍💻 Author
Yashika Aggarwal

Developed as a Python + Data Analytics portfolio project.

---

# ⭐ GitHub Topics

```text
python
streamlit
sqlite
pandas
data-analysis
expense-tracker
finance
visualization
matplotlib
dashboard
```

---

# 🙌 Acknowledgment

Inspired by real-world personal finance management systems and expense analytics dashboards. Similar Streamlit-based expense tracking and finance visualization projects demonstrate how Python dashboards can simplify personal budgeting and financial insights. :contentReference[oaicite:1]{index=1}
