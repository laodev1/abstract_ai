from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Print the key to save it somewhere securely
print(key.decode())

# Optionally, write the key to a file for future use
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)
