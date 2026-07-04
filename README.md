# 📊 Sales ETL Pipeline

An automated ETL (Extract, Transform, Load) pipeline that streamlines the processing of retail sales data.
This project demonstrates how to transform raw data into a structured format and load it into a relational database for analysis.

---

## 🛠 Tech Stack

* **Python** – Core logic for data processing
* **Pandas** – Data cleaning, filtering, and feature engineering
* **SQLAlchemy** – Database connection and ORM handling
* **PostgreSQL** – Structured data storage and querying

---

## 🚀 Key Features

* **Automated Data Cleaning**
  Removes duplicates and handles missing values to ensure high-quality data

* **Feature Engineering**
  Automatically calculates `Total_Revenue` from quantity and price

* **Efficient ETL Workflow**
  Extracts raw data → transforms it → loads into PostgreSQL seamlessly

* **SQL Integration**
  Bridges Python-based processing with a relational database system

---

## ⚙️ How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shruti875/Sales_ETL_Pipeline.git
cd Sales_ETL_Pipeline
```

### 2️⃣ Configure Database

* Make sure PostgreSQL is running
* Create a database named: `sales_db`

---

### 3️⃣ Update Credentials

Open `etl_pipeline.py` and update:

```python
db_url = "postgresql://username:password@localhost:5432/sales_db"
```

---

### 4️⃣ Run the Pipeline

```bash
python etl_pipeline.py
```

---

## 📊 Sample SQL Query

```sql
SELECT "Category", SUM("Total_Revenue") AS total_earned
FROM sales_records
GROUP BY "Category"
ORDER BY total_earned DESC;
```

---

## 📸 Database Output Screenshot

<img width="408" height="482" alt="screenshot png" src="https://github.com/user-attachments/assets/3fa5c28d-13f0-447c-8aa7-749269e8eac5" />

![Database Screenshot](screenshot.png)

---

## 📌 Project Highlights

* Demonstrates real-world ETL pipeline design
* Shows integration between Python and SQL databases
* Focuses on clean, structured, and reusable code
* Suitable for data engineering and analytics portfolios

---

## 🔮 Future Improvements

* Add scheduling (Airflow / Cron jobs)
* Integrate cloud database (AWS RDS)
* Add dashboard (Power BI / Tableau)
* Handle large-scale data (Big Data tools)

---

## 🙌 Author

**Shruti Vishwakarma**

---

⭐ If you found this useful, consider giving it a star!
