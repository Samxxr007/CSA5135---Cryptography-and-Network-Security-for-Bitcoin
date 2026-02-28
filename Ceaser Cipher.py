plaintext = input("Enter text to encrypt: ")
shift_key = int(input("Enter shift key (1-25): "))

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ""
for char in plaintext:
    if char in lower:
        index = lower.index(char)
        result += lower[(index + shift_key) % 26]
    elif char in upper:
        index = upper.index(char)
        result += upper[(index + shift_key) % 26]
    else:
        result += char

print(f"Encrypted text: {result}")