def polyalphabetic_cipher(text, keys, decrypt=False):
    result = []
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = keys[key_index % len(keys)]
            if decrypt:
                shift = -shift
            
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted)
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)


# Example usage
keys = [3, 5, 7]
plaintext = "HELLO"
ciphertext = polyalphabetic_cipher(plaintext, keys)
print(f"Encrypted: {ciphertext}")
print(f"Decrypted: {polyalphabetic_cipher(ciphertext, keys, decrypt=True)}")