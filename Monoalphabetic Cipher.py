import string
import random

def create_cipher_key():
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    return dict(zip(string.ascii_lowercase, alphabet))

def encrypt(text, key):
    return "".join(key.get(c, c) for c in text.lower())

def decrypt(text, key):
    reverse_key = {v: k for k, v in key.items()}
    return "".join(reverse_key.get(c, c) for c in text.lower())

if __name__ == "__main__":
    key = create_cipher_key()
    message = "hello world"
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)
    
    print(f"Key: {key}\nOriginal: {message}\nEncrypted: {encrypted}\nDecrypted: {decrypted}")
