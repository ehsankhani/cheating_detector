import math

def is_prime_optimized(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def list_primes_optimized(limit):
    return [num for num in range(2, limit + 1) if is_prime_optimized(num)]

def main():
    limit = 50
    prime_numbers = list_primes_optimized(limit)
    print(f"Prime numbers up to {limit}: {prime_numbers}")

if __name__ == "__main__":
    main()
