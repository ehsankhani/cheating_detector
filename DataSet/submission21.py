import logging

def validate_non_negative(num):
    """Validates the input as a non-negative integer."""
    if not isinstance(num, int) or num < 0:
        raise ValueError("Input must be a non-negative integer.")

def factorial_via_recursion(num):
    """Compute the factorial using a recursive function."""
    if num == 0:
        return 1
    return num * factorial_via_recursion(num - 1)

def factorial_via_iteration(num):
    """Compute the factorial using iteration."""
    validate_non_negative(num)
    fact = 1
    for i in range(2, num + 1):
        fact *= i
    return fact

def sum_digits(num):
    """Sum the digits of the factorial."""
    return sum(int(digit) for digit in str(num))

def log_results(num, factorial, digits_sum):
    """Log the results to a file."""
    logging.basicConfig(filename='factorial_calculations.log', level=logging.INFO)
    logging.info(f"Number: {num}, Factorial: {factorial}, Sum of digits: {digits_sum}")

def main_menu():
    while True:
        try:
            number = int(input("Please enter a non-negative integer: "))
            validate_non_negative(number)
            factorial_result = factorial_via_iteration(number)
            digits_sum_result = sum_digits(factorial_result)
            log_results(number, factorial_result, digits_sum_result)
            print(f"Factorial: {factorial_result}, Sum of digits: {digits_sum_result}")
        except ValueError as error_message:
            print(f"Error: {error_message}")

        continue_choice = input("Do you want to calculate another factorial? (yes/no): ")
        if continue_choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main_menu()
