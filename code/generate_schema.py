import os
import psycopg2
import pandas as pd

def generate_db_schema_md(output_file):
    # Get the connection string from the environment variable
    connection_string = os.getenv('DB_CONNECTION_STRING')
    
    if not connection_string:
        print("Error: The connection string is not set in the environment variable 'DB_CONNECTION_STRING'.")
        return

    # Connect to the database
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    # Get table names
    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """)
    tables = cursor.fetchall()

    with open(output_file, 'w') as file:
        # Write the header for the Markdown file
        file.write("# **Database Schema Documentation**\n\n")
        file.write("## **Overview**\n\n")
        file.write("This document outlines the structure and purpose of each table in the database.\n\n")
        file.write("## **Tables Overview**\n\n")
        
        # List all the tables
        for i, table in enumerate(tables, start=1):
            file.write(f"{i}. **{table[0]}**\n")

        file.write("\n---\n\n")

        # For each table, get the column names and types
        for i, table in enumerate(tables, start=1):
            file.write(f"### **{i}. {table[0]}**\n\n")
            file.write("**Description:** \n\n")
            file.write("| Column Name | Data Type | Description |\n")
            file.write("| ----------- | --------- | ----------- |\n")

            cursor.execute(f"""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_name = '{table[0]}'
                ORDER BY ordinal_position;
            """)
            columns = cursor.fetchall()

            for column in columns:
                file.write(f"| {column[0]} | {column[1]} |  |\n")

            file.write("\n")

    # Close the connection
    cursor.close()
    conn.close()

# Example usage
output_file = "database_schema.md"
generate_db_schema_md(output_file)

print(f"Database schema documentation generated at {output_file}.")