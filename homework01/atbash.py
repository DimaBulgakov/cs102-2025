"""ШИФР АТБАШ"""


def encrypt_atbash(plaintext: str) -> str:
    ciphertext = ""
    alphabet = ord("Z") - ord("A") + 1
    for char in plaintext:
        if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            if char.isupper():
                base = ord("A")
            else:
                base = ord("a")
            ciphertext += chr((alphabet - ((ord(char) - base + 1) % alphabet) + base))
        else:
            ciphertext += char
    return ciphertext
