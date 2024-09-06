def check_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

def find_primes(upper_limit):
    prime_list = []
    for n in range(2, upper_limit + 1):
        if check_prime(n):
            prime_list.append(n)
    return prime_list

def main():
    upper_limit = 50
    primes = find_primes(upper_limit)
    print(f"Primes up to {upper_limit}: {primes}")

if __name__ == "__main__":
    main()
