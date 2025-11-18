"""ШИФР АТБАШ"""


def encrypt_atbash(plaintext: str) -> str:
    ciphertext = ""
    alphabet = ord("Z") - ord("A") + 1
    for char in plaintext:
        if ord("A") <= ord(char) <= ord("Z") or ord("a") <= ord(char) <= ord("z"):
            if char.isupper():
                base = ord("A")
            else:
                base = ord("a")
            ciphertext += chr((alphabet - ((ord(char) - base + 1) % alphabet) + base))
        else:
            ciphertext += char
    return ciphertext
