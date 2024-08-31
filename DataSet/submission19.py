import logging

def validate_input(num):
    """Ensure the input is a non-negative integer."""
    return isinstance(num, int) and num >= 0

def compute_factorial(num):
    """Compute the factorial using a recursive approach."""
    if num == 0:
        return 1
    else:
        return num * compute_factorial(num - 1)

def record_result(num, result):
    """Record the factorial computation to a log file."""
    logging.basicConfig(filename='factorial_calculations.log', level=logging.INFO)
    logging.info(f"Computed factorial of {num}: {result}")

def process_factorial():
    try:
        input_num = int(input("Please enter a non-negative integer: "))
        if not validate_input(input_num):
            raise ValueError("Only non-negative integers are accepted.")
        result = compute_factorial(input_num)
        record_result(input_num, result)
        print(f"Factorial of {input_num} is {result}")
    except ValueError as error:
        print(error)

def main():
    while True:
        process_factorial()
        repeat = input("Would you like to calculate another factorial? (yes/no): ")
        if repeat.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
