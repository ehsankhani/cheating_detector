def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def list_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    limit = 50
    prime_numbers = list_primes(limit)
    print(f"Prime numbers up to {limit}: {prime_numbers}")

if __name__ == "__main__":
    main()
