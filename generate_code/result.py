def find_common_divisors(a, b):
    divisors_a = [i for i in range(1, a + 1) if a % i == 0]
    divisors_b = [i for i in range(1, b + 1) if b % i == 0]
    common_divisors = [i for i in divisors_a if i in divisors_b]
    return common_divisors

def generate_primes(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
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

