import sqlite3
import secrets

connection = sqlite3.connect('storage.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS notes (token TEXT PRIMARY_KEY, title TEXT, text TEXT, notes TEXT)')
connection.commit()

def add_note(title, text, notes):
    connection = sqlite3.connect('storage.db')
    cursor = connection.cursor()
    while get_note(token := secrets.token_urlsafe(16)) is not None:
        pass
    cursor.execute('INSERT INTO notes VALUES (?, ?, ?)', (token, title, text, notes))
    connection.commit()

    return token

def get_note(token):
    connection = sqlite3.connect('storage.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM notes WHERE token=?', (token, ))
    return cursor.fetchone()

def get_notes():
    connection = sqlite3.connect('storage.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM notes')
    return cursor.fetchall()

def update_note(token, title, text, notes):
    connection = sqlite3.connect('storage.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE notes SET title=? text=? notes=? WHERE token=?', (title, text, notes, token))
    connection.commit()

def delete_note(token):
    connection = sqlite3.connect('storage.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM notes WHERE token=?', (token, ))
    connection.commit()

def delete_all_notes():
    connection = sqlite3.connect('storage.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM notes')
    connection.commit()
