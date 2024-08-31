def input_is_valid(x):
    if not isinstance(x, int) or x < 0:
        return False
    return True


def factorial(x):
    if not input_is_valid(x):
        raise ValueError("Input should be a non-negative integer")

    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact


def main():
    try:
        number = int(input("Enter a positive integer: "))
        print(f"The factorial is {factorial(number)}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
