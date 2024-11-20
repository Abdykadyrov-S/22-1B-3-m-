import sqlite3

connection = sqlite3.connect("Geeks.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS direction (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR (30),
description TEXT         
)
""")

def get_direction():
    directions = cursor.execute("SELECT name FROM direction")
    directions = cursor.fetchall()
    list_direction = []
    for i in directions:
        list_direction.append(i[0])
    return list_direction
