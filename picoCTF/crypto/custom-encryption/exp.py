from random import randint
import sys

def generator(g, x, p):
    return pow(g, x) % p

def decrypt(cipher, key):
    plaintext = ""
    for code in cipher:
        plaintext += chr(code // key // 311)
    return plaintext

def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True

def dynamic_xor_decryption(cipher_text, text_key): # text_key = "trudeau"
    plaintext = ""
    key_length = len(text_key)
    for i, char in enumerate(cipher_text):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        plaintext = decrypted_char + plaintext
    return plaintext

def rev_test(ciphertext, text_key):
    p = 97
    g = 31
    a = 94
    b = 21
    u = generator(g, a, p)      # u = g^a % p
    v = generator(g, b, p)      # v = g^b % p
    shared_key = generator(v, a, p)    # key = v^a % p

    semi_flag = decrypt(ciphertext, shared_key)
    flag = dynamic_xor_decryption(semi_flag, text_key)
    print(f'flag is: {flag}')

if __name__ == "__main__":
    ciphertext = [131553, 993956, 964722, 1359381, 43851, 1169360, 950105, 321574, 1081658, 613914, 0, 1213211, 306957, 73085, 993956, 0, 321574, 1257062, 14617, 906254, 350808, 394659, 87702, 87702, 248489, 87702, 380042, 745467, 467744, 716233, 380042, 102319, 175404, 248489]
    rev_test(ciphertext, "trudeau")
