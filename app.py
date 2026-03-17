import sqlite3

API_KEY = "sk_live_123456_SECRET"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()


def run_command(cmd):
    import os
    os.system(cmd)
