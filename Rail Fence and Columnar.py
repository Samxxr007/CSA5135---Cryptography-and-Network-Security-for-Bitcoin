def rail_fence_encrypt(plaintext, num_rails):
    """Encrypt using Rail Fence cipher"""
    if num_rails < 2:
        return plaintext
    
    rails = ['' for _ in range(num_rails)]
    rail = 0
    direction = 1
    
    for char in plaintext:
        rails[rail] += char
        rail += direction
        
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
    
    return ''.join(rails)


def rail_fence_decrypt(ciphertext, num_rails):
    """Decrypt Rail Fence cipher"""
    if num_rails < 2:
        return ciphertext
    
    # Calculate rail lengths
    rail_lens = [0] * num_rails
    rail = 0
    direction = 1
    
    for _ in ciphertext:
        rail_lens[rail] += 1
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
    
    # Split ciphertext into rails
    rails = []
    idx = 0
    for length in rail_lens:
        rails.append(ciphertext[idx:idx + length])
        idx += length
    
    # Read diagonally
    plaintext = ''
    rail = 0
    direction = 1
    rail_positions = [0] * num_rails
    
    for _ in ciphertext:
        plaintext += rails[rail][rail_positions[rail]]
        rail_positions[rail] += 1
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
    
    return plaintext


def columnar_encrypt(plaintext, key):
    """Encrypt using Columnar Transposition cipher"""
    # Remove spaces and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()
    
    # Create a list of tuples (key_char, index)
    key_order = sorted(enumerate(key), key=lambda x: x[1])
    
    # Arrange plaintext in rows
    num_cols = len(key)
    num_rows = (len(plaintext) + num_cols - 1) // num_cols
    
    # Pad plaintext if necessary
    plaintext += 'X' * (num_rows * num_cols - len(plaintext))
    
    # Create grid
    grid = [plaintext[i*num_cols:(i+1)*num_cols] for i in range(num_rows)]
    
    # Read columns in key order
    ciphertext = ''
    for orig_idx, _ in key_order:
        for row in grid:
            ciphertext += row[orig_idx]
    
    return ciphertext


def columnar_decrypt(ciphertext, key):
    """Decrypt using Columnar Transposition cipher"""
    key_order = sorted(enumerate(key), key=lambda x: x[1])
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    
    # Create grid and fill columns in key order
    grid = [[''] * num_cols for _ in range(num_rows)]
    idx = 0
    
    for orig_idx, _ in key_order:
        for row in range(num_rows):
            grid[row][orig_idx] = ciphertext[idx]
            idx += 1
    
    # Read row by row
    plaintext = ''.join(''.join(row) for row in grid)
    return plaintext


def main():
    """Command-line interface allowing user input for encryption/decryption"""
    print("Choose cipher:\n1. Rail Fence\n2. Columnar Transposition")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        mode = input("Encrypt or decrypt (e/d): ").strip().lower()
        text = input("Enter text: ")
        try:
            rails = int(input("Enter number of rails: "))
        except ValueError:
            print("Invalid number of rails")
            return
        if mode == "e":
            print("Ciphertext:", rail_fence_encrypt(text, rails))
        elif mode == "d":
            print("Plaintext:", rail_fence_decrypt(text, rails))
        else:
            print("Invalid mode")

    elif choice == "2":
        mode = input("Encrypt or decrypt (e/d): ").strip().lower()
        text = input("Enter text: ")
        key = input("Enter key (string): ")
        if mode == "e":
            print("Ciphertext:", columnar_encrypt(text, key))
        elif mode == "d":
            print("Plaintext:", columnar_decrypt(text, key))
        else:
            print("Invalid mode")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()