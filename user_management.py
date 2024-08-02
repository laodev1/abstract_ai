from cryptography.fernet import Fernet
import os

# Load the encryption key from an environment variable
encryption_key = os.environ.get("ENCRYPTION_KEY").encode()
cipher_suite = Fernet(encryption_key)

def encrypt_api_key(api_key: str) -> str:
    return cipher_suite.encrypt(api_key.encode()).decode()

def decrypt_api_key(encrypted_api_key: str) -> str:
    return cipher_suite.decrypt(encrypted_api_key.encode()).decode()

users = {
    "user1": {"api_key": encrypt_api_key("api_key_user1")},
    # Add more users as needed
}

def validate_api_key(api_key: str) -> bool:
    for user in users.values():
        if decrypt_api_key(user["api_key"]) == api_key:
            return True
    return False
