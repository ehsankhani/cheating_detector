def is_it_prime(num):
    if num <= 1:
        return False
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True

def prime_numbers_until(max_value):
    result = []
    for number in range(2, max_value + 1):
        if is_it_prime(number):
            result.append(number)
    return result

def main():
    max_value = 50
    primes = prime_numbers_until(max_value)
    print(f"Prime numbers up to {max_value}: {primes}")

if __name__ == "__main__":
    main()
