from caesar import encrypt_caesar
from caesar import decrypt_caesar

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
    # PUT YOUR CODE HERE
    abc_lower = "abcdefghijklmnopqrstuvwxyz"
    abc_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i, ch in enumerate(plaintext):
        key_ch = keyword[i % len(keyword)] # тут берется буква ключа(пароля), которая соотвествует букве в тексте

        # определяем сдвиг
        if key_ch in abc_lower:
            shift = abc_lower.index(key_ch)
        elif key_ch in abc_upper:
            shift = abc_upper.index(key_ch)
        else:
            shift = 0 # если в ключе странный символ не из алфавита

        # шифруем текст
        ciphertext += encrypt_caesar(ch, shift)

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
    # PUT YOUR CODE HERE
    abc_lower = "abcdefghijklmnopqrstuvwxyz"
    abc_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i, ch in enumerate(ciphertext):
        key_ch = keyword[i % len(keyword)]

        if key_ch in abc_lower:
            shift = abc_lower.index(key_ch)
        elif key_ch in abc_upper:
            shift = abc_upper.index(key_ch)
        else:
            shift = 0

        plaintext += decrypt_caesar(ch, shift)
    return plaintext
