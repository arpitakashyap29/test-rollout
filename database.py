import sqlite3

def get_connection():
    return sqlite3.connect("shop.db")

def get_user(user_id):
    conn = get_connection()
    return conn.execute(f"SELECT * FROM users WHERE id={user_id}").fetchone()

def get_product(product_id):
    conn = get_connection()
    return conn.execute(f"SELECT * FROM products WHERE id={product_id}").fetchone()
