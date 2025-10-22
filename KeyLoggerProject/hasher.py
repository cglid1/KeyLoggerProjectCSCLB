
import hashlib, binascii, os



def strong_hash(password: str, iterations: int = 100_000) -> str: # designed to hash a dictionary 100,000 times
    salt = os.urandom(16)
    hashed = password.encode("utf-8")
    for _ in range(iterations):
        hashed = hashlib.sha512(salt + hashed).digest()
    return hashed.hex()

def verify_hash(password: str, stored_hash: str,) -> bool:
    return strong_hash(password) == stored_hash


