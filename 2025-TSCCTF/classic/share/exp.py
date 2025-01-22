import string
from math import gcd
import secrets

# Define the charset
charset = string.digits + string.ascii_letters + string.punctuation
N = len(charset)

# Find the modular multiplicative inverse of A
def mod_inverse(A, N):
    for i in range(N):
        if (A * i) % N == 1:
            return i
    return -1

while True:
    A = secrets.randbelow(2**32)

    A_inv = mod_inverse(A, N)

    if A_inv == -1:
        continue
    
    B = secrets.randbelow(2**32)

    # Encrypted message (replace with the actual encrypted string)
    with open("flag", "r") as file:
        encrypted_message = file.readline()

    # Decrypt the message
    decrypted_message = ""
    for c in encrypted_message:
        y = charset.find(c)  # Get the index of the encrypted character
        x = (A_inv * (y - B)) % N  # Apply decryption formula
        decrypted_message += charset[x]  # Map back to the original character
    if "TSC{" in decrypted_message:
        print(f"A={A}")
        print(f"B={B}")
        print("Decrypted message:", decrypted_message)
        exit()
