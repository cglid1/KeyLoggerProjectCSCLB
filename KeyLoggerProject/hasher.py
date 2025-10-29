
import hashlib, os
from cryptography.fernet import Fernet


def strong_hash(password: str, iterations: int = 100_000) -> str: # designed to hash a dictionary 100,000 times
    salt = os.urandom(16)
    hashed = password.encode("utf-8")
    for _ in range(iterations):
        hashed = hashlib.sha512(salt + hashed).digest()
    return hashed.hex()

def verify_hash(password: str, stored_hash: str,) -> bool:
    return strong_hash(password) == stored_hash

key = b"8KNqXGk96VxoJMMiX6sp_5GkKP6gQvwBZKn_dEmJQR4=" # variable key for the encrytpion and decryption functions
fernet_key = Fernet.generate_key()  
fernet = Fernet(key)

def encryption(password: str): # encoder function
    
    encMessage = fernet.encrypt(password.encode())
    return encMessage

def decryption(encMessage: str): # decoder function
    decMessage = fernet.decrypt(encMessage).decode()
    return decMessage