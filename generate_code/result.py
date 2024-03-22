def find_common_divisors(a, b):
    return [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]

def generate_primes(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

