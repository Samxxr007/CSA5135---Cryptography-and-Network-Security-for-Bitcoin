def double_columnar_transposition(plaintext, key1, key2):
    """
    Encrypt plaintext using double columnar transposition.
    
    Args:
        plaintext: Text to encrypt
        key1: First key for first transposition
        key2: Second key for second transposition
    
    Returns:
        Encrypted text
    """
    plaintext = plaintext.replace(" ", "").upper()
    
    # First transposition
    cipher1 = columnar_transposition(plaintext, key1)
    
    # Second transposition
    cipher2 = columnar_transposition(cipher1, key2)
    
    return cipher2


def columnar_transposition(text, key):
    """Single columnar transposition."""
    key_len = len(key)
    text_len = len(text)
    
    # Pad text if necessary
    if text_len % key_len != 0:
        text += "X" * (key_len - text_len % key_len)
    
    # Create matrix
    matrix = [text[i:i + key_len] for i in range(0, len(text), key_len)]
    
    # Get column order from key
    col_order = sorted(range(key_len), key=lambda i: key[i])
    
    # Read columns in key order
    cipher = ""
    for col_idx in col_order:
        for row in matrix:
            cipher += row[col_idx]
    
    return cipher


def double_columnar_decryption(ciphertext, key1, key2):
    """
    Decrypt ciphertext using double columnar transposition.
    """
    # Reverse second transposition
    plain1 = reverse_columnar_transposition(ciphertext, key2)
    
    # Reverse first transposition
    plaintext = reverse_columnar_transposition(plain1, key1)
    
    return plaintext.rstrip("X")


def reverse_columnar_transposition(cipher, key):
    """Reverse single columnar transposition."""
    key_len = len(key)
    cipher_len = len(cipher)
    rows = cipher_len // key_len
    
    # Get column order
    col_order = sorted(range(key_len), key=lambda i: key[i])
    
    # Create matrix
    matrix = [[""] * key_len for _ in range(rows)]
    
    # Fill matrix by reading cipher columns
    idx = 0
    for col_order_idx in col_order:
        for row in range(rows):
            matrix[row][col_order_idx] = cipher[idx]
            idx += 1
    
    # Read matrix row by row
    plaintext = "".join("".join(row) for row in matrix)
    
    return plaintext


# Example usage
if __name__ == "__main__":
    plaintext = "HELLO"
    key1 = "CIPHER"
    key2 = "SECRET"
    
    encrypted = double_columnar_transposition(plaintext, key1, key2)
    print(f"Plaintext: {plaintext}")
    print(f"Key 1: {key1}")
    print(f"Key 2: {key2}")
    print(f"Encrypted: {encrypted}")
    
    decrypted = double_columnar_decryption(encrypted, key1, key2)
    print(f"Decrypted: {decrypted}")