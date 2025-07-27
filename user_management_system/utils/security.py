import hashlib
import re

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def validate_password(password: str) -> bool:
    if len(password) < 6:
        print("Password must be at least 6 characters long")
        return False
    if not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password):
        print("Password must contain both letters and numbers")
        return False
    return True
