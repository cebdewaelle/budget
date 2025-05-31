from argon2 import PasswordHasher

ph = PasswordHasher()

def hash_password(plain_password: str) -> str:
    return ph.hash(plain_password)

def verify_password(hashed_password: str, input_password: str) -> bool:
    try:
        ph.verify(hashed_password, input_password)
        return True
    except Exception:
        return False
