import hashlib

message = input("Enter message: ")
key = 5

# create hash
hash_val = hashlib.sha256(message.encode()).hexdigest()

# simple encryption
cipher = ""
for c in message:
    cipher += chr(ord(c) + key)

print("Encrypted Message:", cipher)
print("Message Hash:", hash_val)