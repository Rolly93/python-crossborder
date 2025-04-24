import json
import sqlite3

DATABASE_FILE = 'mydatabase.db'

def create_table():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shipments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            embarque TEXT,
            operacion TEXT,
            unidad TEXT,
            origen TEXT,
            destino TEXT,
            referencia TEXT,
            cliente TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_data(table_name, data_json):
    #conn = sqlite3.connect(DATABASE_FILE)
    #cursor = conn.cursor()
    try:
        data = json.loads(data_json)
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
     #   cursor.execute(sql, tuple(data.values()))
     #   conn.commit()
     #   conn.close()
        print(f"Data inserted successfully into {table_name}")
    except sqlite3.Error as e:
    #    if conn:
    #        conn.rollback()
    #    conn.close()
        return f"Error inserting data: {e}"
    except json.JSONDecodeError as e:
    #    conn.close()
        return f"Error decoding JSON data: {e}"#

def read_data(table_name):
    #conn = sqlite3.connect(DATABASE_FILE)
    #cursor = conn.cursor()
    try:
        sql = f"SELECT * FROM {table_name}"
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        conn.close()
        return json.dumps(result)
    except sqlite3.Error as e:
        conn.close()
        return f"Error reading data: {e}"

if __name__ == '__main__':
    create_table()
    # Example usage if you run this file directly
    data_to_insert = json.dumps({
        "embarque": "TEST123",
        "operacion": "LOAD",
        "unidad": "TRUCK456",
        "origen": "Laredo",
        "destino": "Monterrey",
        "referencia": "REF789",
        "cliente": "Acme Corp"
    })
    insert_result = insert_data("shipments", data_to_insert)
    print(insert_result)
    read_result = read_data("shipments")
    print(read_result)