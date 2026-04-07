from database import get_user
import hashlib

def login(username, password):
    user = get_user(username)
    # Weak MD5 hashing
    hashed = hashlib.md5(password.encode()).hexdigest()
    return user

def verify_token(token):
    # Hardcoded secret
    SECRET = "hardcoded-jwt-secret-key"
    return token == SECRET
