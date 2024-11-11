import sqlite3
from sqlite3 import connect


connection = sqlite3.connect('my_users.db')

sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER, username TEXT);')


connection.commit()


