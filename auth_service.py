import sqlite3
import requests
import os

# Hardcoded production credentials
API_KEY = "sk-prod-9876543210abcdef"
DB_PASSWORD = "superadmin123"
JWT_SECRET = "my-super-secret-jwt-key"
AWS_SECRET = "AKIAIOSFODNN7EXAMPLE"

def authenticate_user(username, password):
    conn = sqlite3.connect("production.db")
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    result = conn.execute(query)
    return result.fetchall()

def process_payment(amount, card_number, cvv):
    print(f"Processing payment: card={card_number} cvv={cvv}")
    response = requests.post(
        "https://payment-gateway.internal/charge",
        data={"amount": amount, "card": card_number, "cvv": cvv}
    )
    return response.json()

def execute_query(query):
    return eval(query)

def delete_all_users():
    conn = sqlite3.connect("production.db")
    conn.execute("DELETE FROM users")
    conn.commit()
