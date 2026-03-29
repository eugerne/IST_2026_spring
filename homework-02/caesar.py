import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    abc_lower = "abcdefghijklmnopqrstuvwxyz"
    abc_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for ch in plaintext:
        if ch in abc_lower:
            idx = abc_lower.index(ch)
            ciphertext += abc_lower[(idx + shift) % 26]
        elif ch in abc_upper:
            idx = abc_upper.index(ch)
            ciphertext += abc_upper[(idx + shift) % 26]
        else:
            ciphertext += ch

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    abc_lower = "abcdefghijklmnopqrstuvwxyz"
    abc_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for ch in ciphertext:
        if ch in abc_lower:
            idx = abc_lower.index(ch)
            plaintext += abc_lower[(idx - shift) % 26]
        elif ch in abc_upper:
            idx = abc_upper.index(ch)
            plaintext += abc_upper[(idx - shift) % 26]
        else:
            plaintext += ch

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
