import sqlite3

connection = sqlite3.connect('storage.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS notes (token TEXT PRIMARY_KEY, text TEXT, notes TEXT)')
connection.commit()