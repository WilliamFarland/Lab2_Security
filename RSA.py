import random

"""
UMass Amherst, ECE 371, Introduction to security Engineering
RSA Implementation for Part1 of Lab 2
Revisions by: William Farland 

*** Some information that you should remember ***

Technical steps for RSA:
1. Select two large prime numbers, x and y. The prime numbers need to be large so that they will be difficult for someone 
to figure out.

2. Calculate n = x * y

3. Calculate the totient function; ϕ(n)=(x−1)(y−1)

4. Select an integer e, such that e is co-prime to ϕ(n) and 1 < e < ϕ(n) 
The pair of numbers (n,e)(n,e) makes up the public key.


What is RSA?
    -RSA is an asymmetric cryptography algorithm
    -RSA utilizes both a public and private key
        -these two keys are different and mathematically linked
    -The public key is available to anyone
    -The private key must remain anonymous
    
Who invented RSA?
    -Ron Rivest, Adi Shamir, and Leonard Adleman.
    
How does RSA work?
    Ex. Bob wants to send a confidential message to Alice.
    
    Step 1) Bob writes his message, and encrypts it using Alice's public key
    Step 2) Bob sends the encrypted cipher text to Alice
    Step 3) Alice decrypts the message using her private key

What is the definition of coprime?
    -Two numbers are considered coprime when they have no common factors other than 1
    
What is the totient function? 
    -Euler's totient function (also called the Phi function) counts the number of positive 
        integers less than n that are coprime to n. 
    -Ex. Compute ϕ(15)
    Factors of 15: 1, 3, 5, 15
    Numbers less than 15: 1,2,3,4,5,6,7,8,9,10,11,12,13,14
    1 --> coprime       c=1
    2 --> coprime       c=2 
    3 --> not coprime 
    4 --> coprime       c=3 
    5 --> not coprime 
    6 --> not coprime       
    7 --> coprime       c=4
    8 --> coprime       c=5 
    9 --> not coprime 
    10 --> not coprime 
    11 --> coprime      c=6 
    12 --> not coprime
    13 --> coprime      c=7
    14 --> coprime      c=8
    
    Count of coprime #'s: 8
    
"""

# Part 1 - Bob wants to send Alice a confidential message
# Need to generate the keys, p & q
# p & q need to be very large prime numbers
# for the purposes of this lab you will get yous provided in the excel file
# for now use the default p & q values in order to test your code
p, q = 1297273, 1297651


def gcd(a, b):
    """ function for finding gcd of two numbers using euclidean algorithm """
    while b != 0:
        a, b = b, a % b
    return a


def get_d(e, z):
    """ uses extended euclidean algorithm to get the d value """
    # Enter code here
    d = 0
    return d


def is_prime(num):
    """ determines if provided input is a prime number or not """
    if num > 1:
        for i in range(2, num // 2):  # Iterate from 2 to n / 2
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
            else:
                return True
    else:
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    # Step 1
    n = p * q
    # Step 2 Calculate the totient function;  ϕ(n) = (x−1)(y−1)

    e = 0
    n = 0
    d = 0
    return (e, n), (d, n)


def encrypt(pk, plaintext):
    # Enter code here
    # plaintext is a single character
    # cipher is a decimal number which is the encrypted version of plaintext
    # the pow function is much faster in calculating power compared to the ** symbol !!!
    cipher = 0
    return cipher


def decrypt(pk, ciphertext):
    # Enter code here
    # ciphertext is a single decimal number
    # the returned value is a character that is the decryption of ciphertext
    plain = 'a'
    return ''.join(plain)


def main():
    public, private = generate_keypair(p, q)
    print("RSA Public Key pair = " + str(public))
    print("RSA Private Key pair = " + str(private))
