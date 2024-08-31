def is_valid_input(n):
    return isinstance(n, int) and n >= 0


def calculate_factorial(n):
    if not is_valid_input(n):
        raise ValueError("Please enter a non-negative integer")

    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def main():
    try:
        num = int(input("Enter a number to find its factorial: "))
        print(f"Factorial: {calculate_factorial(num)}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
