import sqlite3
import pandas as pd

# Initialize the database
DATABASE = 'WK7/google_flask_app/users.db'

# search for user in database
db = sqlite3.connect(DATABASE)
cursor = db.cursor()

# get list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# get values from users table
df = pd.read_sql_query("SELECT * FROM users", db)
df
