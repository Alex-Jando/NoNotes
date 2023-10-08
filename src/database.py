import sqlite3
import secrets

connection = sqlite3.connect('storage.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS notes (token TEXT PRIMARY_KEY, text TEXT, notes TEXT)')
connection.commit()

def add_note(text, notes):
    while get_note(token := secrets.token_urlsafe(16)) is not None:
        pass
    cursor.execute('INSERT INTO notes VALUES (?, ?, ?)', (token, text, notes))
    connection.commit()

def get_note(token):
    cursor.execute('SELECT * FROM notes WHERE token=?', (token, ))
    return cursor.fetchone()

def get_notes():
    cursor.execute('SELECT * FROM notes')
    return cursor.fetchall()

def update_note(token, text, notes):
    cursor.execute('UPDATE notes SET text=? notes=? WHERE token=?', (text, notes, token))
    connection.commit()

def delete_note(token):
    cursor.execute('DELETE FROM notes WHERE token=?', (token, ))
    connection.commit()

def delete_all_notes():
    cursor.execute('DELETE FROM notes')
    connection.commit()
