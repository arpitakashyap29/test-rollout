def fetch_customer(customer_id: int):
    """Changed from str to int — breaking change"""
    import sqlite3
    conn = sqlite3.connect("shop.db")
    query = f"SELECT * FROM customers WHERE id={customer_id}"
    return conn.execute(query).fetchone()

def fetch_order(order_id: int):
    """Changed from str to int — breaking change"""
    import sqlite3
    conn = sqlite3.connect("shop.db")
    return conn.execute(f"SELECT * FROM orders WHERE id={order_id}").fetchone()
