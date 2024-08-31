import logging

def validate_input_is_non_negative_integer(n):
    """Validates that the input is a non-negative integer."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("The provided input must be a non-negative integer.")

def compute_factorial_recursive(n):
    """Compute the factorial of a number using recursion."""
    if n == 0:
        return 1
    return n * compute_factorial_recursive(n - 1)

def compute_factorial_iterative(n):
    """Compute the factorial of a number using an iterative method."""
    validate_input_is_non_negative_integer(n)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def compute_sum_of_digits(num):
    """Compute the sum of the digits of a number."""
    return sum(int(digit) for digit in str(num))

def log_calculation_results(n, factorial_result, digit_sum_result):
    """Log the results of the calculations to a file."""
    logging.basicConfig(filename='factorial_results.log', level=logging.INFO)
    logging.info(f"Input: {n}, Factorial: {factorial_result}, Sum of digits: {digit_sum_result}")

def factorial_menu():
    while True:
        try:
            user_input = int(input("Enter a non-negative integer: "))
            validate_input_is_non_negative_integer(user_input)
            factorial_result = compute_factorial_iterative(user_input)
            digit_sum_result = compute_sum_of_digits(factorial_result)
            log_calculation_results(user_input, factorial_result, digit_sum_result)
            print(f"Factorial: {factorial_result}, Sum of digits: {digit_sum_result}")
        except ValueError as e:
            print(f"Error: {e}")

        choice = input("Calculate another factorial? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    factorial_menu()
