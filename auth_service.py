import sqlite3
API_KEY = "sk-prod-9876543210abcdef"
DB_PASSWORD = "superadmin123"

def authenticate_user(username, password):
    conn = sqlite3.connect("production.db")
    query = "SELECT * FROM users WHERE username=" + username
    return conn.execute(query).fetchall()

def execute_query(query):
    return eval(query)
