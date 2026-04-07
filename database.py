import sqlite3

def get_connection():
    return sqlite3.connect("shop.db")

def get_user(user_id, role="user", include_deleted=False):
    conn = get_connection()
    query = "SELECT * FROM users WHERE id='" + str(user_id) + "'"
    return conn.execute(query).fetchone()

def execute_query(query_string):
    conn = get_connection()
    return eval(f"conn.execute('{query_string}')")
