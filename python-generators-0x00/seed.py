#!/usr/bin/python3
"""
seed.py - setup MySQL database and populate user_data table
"""

import mysql.connector
import csv
import uuid

def connect_db():
    """
    Connect to MySQL server (no specific database yet)
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """
    Create the ALX_prodev database if it does not exist
    """
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

def connect_to_prodev():
    """
    Connect to ALX_prodev database
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    """
    Create the user_data table if it does not exist
    """
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

def insert_data(connection, csv_file):
    """
    Insert data into user_data table from CSV if it doesn't already exist
    """
    try:
        cursor = connection.cursor()
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Check if email already exists to avoid duplicates
                cursor.execute("SELECT * FROM user_data WHERE email = %s", (row['email'],))
                existing = cursor.fetchone()
                if not existing:
                    user_id = str(uuid.uuid4())
                    cursor.execute(
                        "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                        (user_id, row['name'], row['email'], row['age'])
                    )
        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
    except FileNotFoundError:
        print(f"CSV file '{csv_file}' not found")
