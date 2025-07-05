#!/usr/bin/env python3
import mysql.connector

def stream_users_in_batches(batch_size):
    """
    Generator to fetch rows in batches from user_data
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM user_data")

    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        yield rows

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """
    Processes each batch to filter users over age 25
    """
    for batch in stream_users_in_batches(batch_size):
        for row in batch:
            if row['age'] > 25:
                print(row)
