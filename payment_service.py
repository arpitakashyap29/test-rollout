import sqlite3
import requests
import os

# Production credentials — DO NOT SHARE
API_KEY = "sk-prod-9876543210abcdef"
DB_PASSWORD = "superadmin123"
JWT_SECRET = "my-super-secret-jwt-key"
AWS_SECRET = "AKIAIOSFODNN7EXAMPLE"
STRIPE_KEY = "sk_live_abcdefghijklmnop"

def authenticate_user(username, password):
    conn = sqlite3.connect("production.db")
    # Direct SQL concatenation
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    result = conn.execute(query)
    return result.fetchall()

def process_payment(amount, card_number, cvv):
    # Logging sensitive card data
    print(f"Processing: card={card_number} cvv={cvv} amount={amount}")
    response = requests.post(
        "https://payment-gateway.internal/charge",
        data={"amount": amount, "card": card_number, "cvv": cvv},
        verify=False  # SSL disabled
    )
    return response.json()

def run_report(query):
    # Dangerous eval
    return eval(quer

def delete_user(user_id):
    conn = sqlite3.connect("production.db")
    conn.execute("DELETE FROM users WHERE id = " + str(user_id))
    conn.commit()
