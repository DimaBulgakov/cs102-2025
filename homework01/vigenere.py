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
    upper_base = ord("A")
    lower_base = ord("a")

    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = keyword[i % len(keyword)]
            shift = ord(key_char) - ord("A")
            if char.isupper():
                ciphertext += chr((ord(char) - upper_base + shift) % alphabet + upper_base)
            else:
                ciphertext += chr((ord(char) - lower_base + shift) % alphabet + lower_base)
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
    upper_base = ord("A")
    lower_base = ord("a")
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = keyword[i % len(keyword)]
            shift = ord(key_char) - ord("A")
            if char.isupper():
                plaintext += chr((ord(char) - upper_base - shift) % alphabet + upper_base)
            else:
                plaintext += chr((ord(char) - lower_base - shift) % alphabet + lower_base)
        else:
            plaintext += char

    return plaintext
