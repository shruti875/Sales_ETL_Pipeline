Sales-ETL-Pipeline
An automated ETL (Extract, Transform, Load) pipeline that streamlines the processing of retail sales data. This project demonstrates the ability to bridge raw data sources with structured analytical databases.

🛠 Tech Stack
Python: The core logic for data manipulation.

Pandas: Used for cleaning, filtering, and performing feature engineering on raw datasets.

SQLAlchemy: Integrated to handle the connection between Python and the database.

PostgreSQL: Used for structured data storage and efficient SQL-based querying.

🚀 Key Features
Automated Data Cleaning: Removes duplicates and handles missing values to ensure high data quality.

Feature Engineering: Automatically calculates Total_Revenue from quantity and price data.

Efficient ETL Workflow: Extracts raw data, transforms it, and loads it into a relational PostgreSQL database in one seamless pipeline.

SQL Integration: Demonstrates the ability to bridge Python-based data processing with professional-grade database management.

⚙️ How to Run
Clone the repository:

Clone this repository:

   ```bash
   git clone https://github.com/shruti875/Sales_ETL_Pipeline.git
   ```

Configure Database: Ensure PostgreSQL is running and create a database named sales_db.

Update Credentials: Open etl_pipeline.py and update your PostgreSQL username and password in the db_url variable.

Execute:

Bash
python etl_pipeline.py
📊 Sample SQL Query
Once the data is loaded, you can run this query in your database to get category insights:

SQL
SELECT "Category", SUM("Total_Revenue") AS total_earned
FROM sales_records
GROUP BY "Category"
ORDER BY total_earned DESC;

![Database Screenshot](screenshot<img width="408" height="482" alt="screenshot" src="https://github.com/user-attachments/assets/93f152fb-a330-4b81-b97c-d8614fc48c76" />
.png)
