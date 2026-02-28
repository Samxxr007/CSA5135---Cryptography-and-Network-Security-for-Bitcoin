# Vigenere Cipher Encryption

def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_index = 0

    for char in plaintext.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char

    return ciphertext


# INPUT
plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

# OUTPUT
ciphertext = vigenere_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)