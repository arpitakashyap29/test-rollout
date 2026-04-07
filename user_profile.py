import sqlite3

def update_email(user_id, new_email):
    conn = sqlite3.connect("users.db")
    # SQL injection risk
    query = f"UPDATE users SET email='{new_email}' WHERE id={user_id}"
    conn.execute(query)
    conn.commit()

def get_profile(user_id):
    conn = sqlite3.connect("users.db")
    query = f"SELECT name, email FROM users WHERE id={user_id}"
    return conn.execute(query).fetchone()
