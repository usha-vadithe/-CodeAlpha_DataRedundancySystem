import sqlite3

def create_table():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()
