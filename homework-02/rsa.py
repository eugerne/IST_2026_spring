import random
import typing as tp


def is_prime(n: int) -> bool:
    """
    Tests to see if a number is prime.

    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if n == 1:
        return False
    
    for d in range(2, int(n**0.5 + 1)):
        if n % d == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.

    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.

    >>> multiplicative_inverse(7, 40)
    23
    """

    '''
    Как работает?
    Мы ищем x и y такие, что Ax + By = d, где d - НОД для A и B
    Для начал ищем этот самый НОД => в конце алгоритма получаем
    уравнение 0x + dy = d - оно разрешимо при x=0, y=1.
    Вносим это в таблицу, а остальные x_i, y_i находим по формулам:
    x_i = y_i-1
    y_i = x_i-1 - y_i-1 * (Ai//Bi)
    В таком случае последнее полученное y_i - это обратный элемент
    '''

    # простой алгоритм евклида и запись в таблицу
    a, b = phi, e
    table = [[a, b, a % b, a // b]]

    while a % b != 0:
        a, b = b, a % b
        table.append([a, b, a % b, a // b])

    # расширенный алгоритм евклида(добавляем x и y)
    table[-1].extend([0, 1]) # x_k = 0, y_k = 1

    for i in range(len(table) - 2, -1, -1):
        _, _, _, q, x_next, y_next = table[i+1]
        x_i = y_next
        y_i = x_next - y_next * table[i][3] # q_i
        table[i].extend([x_i, y_i])

    # x_0 - это обратный элемент
    x = table[0][5]
    return x % phi

def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    n = p*q

    phi = (p-1)*(q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
