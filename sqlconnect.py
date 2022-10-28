import mysql.connector
from mysql.connector import Error
import pandas as pd

ROOT_PASS = ""

def create_server_connection(host_name, user_name, user_password, db_name=""):
    connection = None
    try:
        if db_name:
            connection = mysql.connector.connect(
                    host=host_name,
                    user=user_name,
                    passwd=user_password,
                    database=db_name
            )
        else:
            connection = mysql.connector.connect(
                    host=host_name,
                    user=user_name,
                    passwd=user_password
            )
        print("MySQL database connection established.")
    except Error as e:
        print(f"Error {e}")

    return connector

def execute_query(connection, query):
    create_database_indicator = "CREATE DATABASE"
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        if create_database_indicator in query:
            print("Database created successfully.")
        else:
            connection.commit()
            print("Query successful.")
            
    except Error as e:
        print(f"Error {e}")

connection = create_server_connection("localhost", "root", ROOT_PASS)
