def validate_input(num):
    if isinstance(num, int) and num >= 0:
        return True
    return False


def factorial_recursive(num):
    if not validate_input(num):
        raise ValueError("Input must be a non-negative integer")

    if num == 0:
        return 1
    else:
        return num * factorial_recursive(num - 1)


try:
    user_input = int(input("Please enter an integer: "))
    print(f"The factorial of {user_input} is {factorial_recursive(user_input)}")
except ValueError as error:
    print(error)
