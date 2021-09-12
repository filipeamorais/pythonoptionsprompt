import sqlite3
from sqlite3.dbapi2 import connect

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute("CREATE TABLE entries (content TEXT,date TEXT )")

def add_entry (entry_content, entry_date):
    with connection:
        connection.execute("INSERT INTO entries VALUES ('Rolf','Smith')")

def get_entries():
    with connection:
        connection.execute("SELECT * FROM entries")
    