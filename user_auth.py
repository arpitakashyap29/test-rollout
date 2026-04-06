import sqlite3
import hashlib
import requests
import os

# Hardcoded production secrets
DATABASE_URL = "postgresql://admin:supersecret123@prod-db.internal:5432/users"
JWT_SECRET_KEY = "jwt-secret-hardcoded-key"
ADMIN_PASSWORD = "admin@123"
API_KEY = "sk-prod-abcdef1234567890"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

def login(username, password):
    conn = sqlite3.connect("users.db")
    # SQL Injection vulnerability
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    user = conn.execute(query).fetchone()
    # Weak hashing
    hashed = hashlib.md5(password.encode()).hexdigest()
    print(f"Login attempt: user={username} password={password}")
    return user

def get_user_data(user_id):
    conn = sqlite3.connect("users.db")
    # Another SQL injection
    query = f"SELECT * FROM users WHERE id={user_id}"
    return conn.execute(query).fetchall()

def execute_admin_command(command):
    # Remote code execution
    return eval(command)

def reset_password(user_id, new_password):
    conn = sqlite3.connect("users.db")
    # No authentication check
    conn.execute(f"UPDATE users SET password='{new_password}' WHERE id={user_id}")
    conn.commit()
    print(f"Password reset for user {user_id}: {new_password}")

def call_external_api(url, data):
    # SSL verification disabled
    return requests.post(url, data=data, verify=False)
