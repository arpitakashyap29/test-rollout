import sqlite3
import requests
import hashlib

# Production credentials - DO NOT SHARE
DB_PASSWORD = "prod_db_pass_123"
API_KEY = "sk-prod-abcdef1234567890"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
JWT_SECRET = "hardcoded-jwt-secret"

def login(username, password):
    conn = sqlite3.connect("users.db")
    # SQL Injection
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    print(f"Login attempt: user={username} pass={password}")
    return conn.execute(query).fetchone()

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE id={user_id}"
    return conn.execute(query).fetchall()

def run_admin_command(cmd):
    return eval(cmd)

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
