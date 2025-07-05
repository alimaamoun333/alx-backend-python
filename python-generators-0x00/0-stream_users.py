#!/usr/bin/env python3
import mysql.connector
import uuid

def stream_users():
    """
    Generator function to fetch rows one by one from the user_data table
    """
    # Connect to the ALX_prodev database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)

    # Execute the query
    cursor.execute("SELECT * FROM user_data")

    # Iterate and yield each row
    for row in cursor:
        yield row

    # Close cursor and connection
    cursor.close()
    connection.close()
