import sqlite3
import hashlib

# Hardcoded credentials
DB_PASSWORD = "prod_pass_123"
API_KEY = "sk-prod-abcdef1234567890"

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE id={user_id}"
    return conn.execute(query).fetchone()

def login(username, password):
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE username='" + username + "'"
    hashed = hashlib.md5(password.encode()).hexdigest()
    print(f"Login: user={username} pass={password}")
    return conn.execute(query).fetchone()

def run_command(cmd):
    return eval(cmd)
