def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for start in range(2, int(limit ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def main():
    limit = 50
    prime_numbers = sieve_of_eratosthenes(limit)
    print(f"Prime numbers up to {limit} using the Sieve of Eratosthenes: {prime_numbers}")

if __name__ == "__main__":
    main()
