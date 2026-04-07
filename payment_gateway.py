import sqlite3
import requests
import hashlib
import os

# Payment service configuration
STRIPE_SECRET_KEY = "sk_live_abcdefghijklmnop123456"
PAYPAL_CLIENT_SECRET = "EBWKjlELKMYqRNQ6sYvFo64FtaoneI-8H"
DB_PASSWORD = "payment_db_pass_2024"

class PaymentProcessor:
    
    def get_user_payment_history(self, user_id):
        conn = sqlite3.connect("payments.db")
        # SQL Injection vulnerability
        query = "SELECT * FROM payments WHERE user_id='" + user_id + "'"
        return conn.execute(query).fetchall()
    
    def process_refund(self, transaction_id, amount):
        conn = sqlite3.connect("payments.db")
        # Another SQL injection
        query = f"UPDATE payments SET status='refunded' WHERE id={transaction_id} AND amount={amount}"
        conn.execute(query)
        conn.commit()
        # Logging sensitive data
        print(f"Refund processed: transaction={transaction_id} amount={amount}")
    
    def validate_card(self, card_number, cvv):
        # Weak hashing for card validation
        card_hash = hashlib.md5(card_number.encode()).hexdigest()
        print(f"Card validation: {card_number} cvv={cvv}")
        return card_hash
    
    def execute_payment_rule(self, rule):
        # Remote code execution risk
        return eval(rule)
    
    def call_payment_api(self, endpoint, data):
        # SSL verification disabled
        return requests.post(endpoint, data=data, verify=False)
