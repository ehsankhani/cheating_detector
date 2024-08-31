def is_valid_input(n):
    if isinstance(n, int) and n >= 0:
        return True
    return False


def find_factorial(n):
    if not is_valid_input(n):
        raise ValueError("Input must be a non-negative integer")

    if n == 0:
        return 1
    else:
        return n * find_factorial(n - 1)


try:
    number = int(input("Enter a number: "))
    print(f"The factorial of {number} is {find_factorial(number)}")
except ValueError as e:
    print(e)
