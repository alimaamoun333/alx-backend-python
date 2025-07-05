# Python Generators - Database Seeding Project

This project demonstrates how to set up a MySQL database and seed it with user data from a CSV file using Python. It is part of the **ALX Backend Python - Generators** module.

---

## 🎯 Objectives

- Connect to MySQL server
- Create a database (`ALX_prodev`) if it does not exist
- Create a `user_data` table
- Load sample user data from a CSV file (`user_data.csv`)
- Prepare the data for further processing with Python generators

---

## 📂 Files

- `seed.py`  
  Contains all the logic for:
  - Connecting to MySQL
  - Creating the database and table
  - Inserting data
- `0-main.py`  
  Driver script to run all setup steps.
- `user_data.csv`  
  CSV file with sample data to seed the `user_data` table.

---

## 🛠 Setup Instructions

1. **Install MySQL and Python connector:**

   ```bash
   sudo apt-get install mysql-server
   pip install mysql-connector-python
