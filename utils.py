import math

def find_prime_factors(number): 
    """
    returns the canonical representation of a positive integer
    by the fundamental theorem of arithmetic :D
    the keys are the prime factors and the values are the exponents
    Wheel Factorization
    """
    divisors = dict()

    while number % 2 == 0:
        number = number // 2
        if 2 in divisors:
            divisors[2] += 1
        else:
            divisors[2] = 1

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            number = number // i
            if i in divisors:
                divisors[i] += 1
            else:
                divisors[i] = 1
    
    if number > 1: # if the number is prime
        divisors[number] = 1 
    

    return divisors


def euclid_extended(a, b):
    """
    returns the gcd of a and b
    and the coefficients of Bezout's identity
    """
    x = 1
    y = 0
    x1 = 0
    y1 = 1
    a1 = a
    b1 = b
    while b1 != 0:
        q = a1 // b1
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1
        a1, b1 = b1, a1 - q * b1

    return a1, x, y

def inverse_element_ring(elem, ring):
    """
    returns the reverse element of elem in ring
    """
    gcd, x, y = euclid_extended(elem, ring)
    if gcd == 1:
        return x % ring
    else:
        return None # elem and ring are not coprime

def discrete_log_bf(base, c, modulus): 
    x = 1
    while True: 
        if pow(base, x, modulus) == c:
            return x
        x += 1

def is_prime(number): 
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(find_prime_factors(100))
    print(find_prime_factors(353))
    print(find_prime_factors(352))
    print(discrete_log_bf(3, 135, 353))
    
    print()
    for i in range(1, 1000):
        if pow(2, i - 1, i) == 1 and not(is_prime(i)):
            print(i, find_prime_factors(i))

    print()
    for i in range(1, 1000):
        if pow(3, i - 1, i) == 1 and not(is_prime(i)):
            print(i, find_prime_factors(i))

    temp = 91
    print((pow(3, 91) - 1) // 2)
    for i in range(1, 256, 2): 
        print((pow(3, i) - 1) // 2)