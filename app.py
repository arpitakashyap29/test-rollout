import sqlite3
from auth_service import authenticate_user, process_payment

def get_dashboard(user_id):
    conn = sqlite3.connect("production.db")
    return conn.execute(f"SELECT * FROM dashboard WHERE user_id={user_id}")

def checkout(cart_id, card_number, cvv, amount):
    payment = process_payment(amount, card_number, cvv)
    return payment

def login(username, password):
    return authenticate_user(username, password)