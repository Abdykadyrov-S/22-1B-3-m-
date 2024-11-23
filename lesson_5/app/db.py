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

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
telegram_id INTEGER,
name VARCHAR (30),
age INTEGER,
email VARCHAR (60)
)
""")

def register(telegram_id, name):
    cursor.execute(f"SELECT telegram_id FROM users WHERE telegram_id = {telegram_id}")
    users = cursor.fetchone()
    print(users)
    if users:
        print("Вы уже прошли регистрацию")
    else:
        cursor.execute(f"""INSERT INTO users (telegram_id, name)
                    VALUES ({telegram_id}, '{name}')""")
        connection.commit()

def get_user(telegram_id):
    cursor.execute(f"SELECT * FROM users WHERE telegram_id = {telegram_id}")
    user = cursor.fetchone()
    return user

def get_direction():
    directions = cursor.execute("SELECT name FROM direction")
    directions = cursor.fetchall()
    list_direction = []
    for i in directions:
        list_direction.append(i[0])
    return list_direction

def update_profile_in_db(id, name, age, email):
    cursor.execute(f"""UPDATE users SET 
                   name = '{name}', age = {age}, email = '{email}'
                WHERE telegram_id = {id}""")
    connection.commit()


