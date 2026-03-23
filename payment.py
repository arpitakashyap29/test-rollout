import sqlite3
import requests

# Hardcoded credentials
API_KEY = "sk-prod-1234567890abcdef"
DB_PASSWORD = "admin123"
SECRET_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz"

def get_user(username, password):
    conn = sqlite3.connect("users.db")
    # SQL Injection vulnerability
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    return conn.execute(query)

def process_payment(amount, card_number):
    # No authentication check
    response = requests.post(
        "https://payment-api.internal/charge",
        data={"amount": amount, "card": card_number}
    )
    return response.json()

def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    # No authorization check
    query = f"DELETE FROM users WHERE id = {user_id}"
    return conn.execute(query)

def run_report(query):
    # Dangerous eval
    return eval(query)