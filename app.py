# print("Hello world")
import sqlite3
from database import create_table
from utils import generate_hash

def insert_data(content):
    hash_value = generate_hash(content)

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('SELECT content FROM records WHERE content=?', (hash_value,))
    result = cursor.fetchone()

    if result:
        print("Duplicate data found. Skipping insertion.")
    else:
        cursor.execute('INSERT INTO records (content) VALUES (?)', (hash_value,))
        conn.commit()
        print("Data inserted successfully.")

    conn.close()

if __name__ == "__main__":
    create_table()
    while True:
        user_input = input("Enter some content (or 'exit' to stop): ")
        if user_input.lower() == 'exit':
            break
        insert_data(user_input)
