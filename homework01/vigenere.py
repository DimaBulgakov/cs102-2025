"""ШИФР ВИНЕЖЕРА"""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()
    alphabet = ord("Z") - ord("A") + 1

    for i, char in enumerate(plaintext):
        if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            key_char = keyword[i % len(keyword)]
            shift = ord(key_char) - ord("A")
            if char.isupper():
                base = ord("A")
            else:
                base = ord("a")
            ciphertext += chr((ord(char) - base + shift) % alphabet + base)
        else:
            ciphertext += char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.upper()
    alphabet = ord("Z") - ord("A") + 1
    for i, char in enumerate(ciphertext):
        if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            key_char = keyword[i % len(keyword)]
            shift = ord(key_char) - ord("A")
            if char.isupper():
                base = ord("A")
            else:
                base = ord("a")
            plaintext += chr((ord(char) - base - shift) % alphabet + base)
        else:
            plaintext += char

    return plaintext
