def generate_fibonacci_iterative(limit):
    fibonacci_sequence = [0, 1]
    while True:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_value >= limit:
            break
        fibonacci_sequence.append(next_value)
    return fibonacci_sequence

def print_fibonacci_sequence(seq):
    print("Fibonacci sequence up to the limit:")
    for index, value in enumerate(seq):
        print(f"Index {index}: {value}")

def main():
    limit = 100
    fibonacci_sequence = generate_fibonacci_iterative(limit)
    print_fibonacci_sequence(fibonacci_sequence)

if __name__ == "__main__":
    main()
