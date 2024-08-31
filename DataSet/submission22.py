import logging

def check_non_negative_int(n):
    """Ensure the input is a non-negative integer."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

def factorial_by_loop(n):
    """Calculate factorial using a loop."""
    check_non_negative_int(n)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def digit_sum_of_factorial(fact):
    """Compute the sum of digits of the factorial."""
    return sum(int(digit) for digit in str(fact))

def log_results(n, factorial_result, sum_digits):
    """Log the factorial and digit sum to a log file."""
    logging.basicConfig(filename='factorial_log_output.log', level=logging.INFO)
    logging.info(f"Factorial of {n}: {factorial_result}, Sum of digits: {sum_digits}")

def main():
    while True:
        try:
            number = int(input("Enter a non-negative integer: "))
            factorial_result = factorial_by_loop(number)
            sum_digits = digit_sum_of_factorial(factorial_result)
            log_results(number, factorial_result, sum_digits)
            print(f"Factorial: {factorial_result}, Sum of digits: {sum_digits}")
        except ValueError as error:
            print(f"Error: {error}")

        if input("Calculate another? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()
