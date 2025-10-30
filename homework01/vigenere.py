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
    indx = 0
    extended_key = ""
    for i in range(0, len(plaintext)):
        extended_key += keyword[i % len(keyword)]

    for char in plaintext:
        if char.isalpha():
            shift = ord(extended_key[indx]) - ord('A')

            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            ciphertext += encrypted_char
            indx += 1
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
    extended_key = ""
    for i in range(0, len(ciphertext)):
        extended_key += keyword[i % len(keyword)]
    indx = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(extended_key[indx]) - ord('A')

            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

            plaintext += decrypted_char
            indx += 1
        else:
            plaintext += char

    return plaintext

