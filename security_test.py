import sqlite3
import hashlib
import os

# Hardcoded credentials
API_KEY = "sk-prod-abcdef1234567890"
DB_PASSWORD = "admin123"

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE id={user_id}"
    return conn.execute(query).fetchone()

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
