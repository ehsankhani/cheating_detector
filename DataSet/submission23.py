import logging

def validate_non_negative(num):
    """Validate that the input is a non-negative integer."""
    if not isinstance(num, int) or num < 0:
        raise ValueError("Input must be a non-negative integer.")

def calculate_factorial(num):
    """Calculate factorial using a while loop."""
    validate_non_negative(num)
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial

def calculate_sum_of_digits(factorial_value):
    """Sum the digits of the factorial."""
    return sum(int(digit) for digit in str(factorial_value))

def log_results_to_file(num, factorial_value, sum_digits):
    """Log the factorial and digit sum to a log file."""
    logging.basicConfig(filename='factorial_computation.log', level=logging.INFO)
    logging.info(f"Factorial of {num}: {factorial_value}, Sum of digits: {sum_digits}")

def factorial_calculation():
    while True:
        try:
            num = int(input("Please enter a non-negative integer: "))
            factorial_value = calculate_factorial(num)
            sum_digits = calculate_sum_of_digits(factorial_value)
            log_results_to_file(num, factorial_value, sum_digits)
            print(f"Factorial: {factorial_value}, Sum of digits: {sum_digits}")
        except ValueError as ve:
            print(f"Error: {ve}")

        if input("Perform another calculation? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    factorial_calculation()
