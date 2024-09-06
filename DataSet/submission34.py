def generate_fibonacci_recursive(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = generate_fibonacci_recursive(n - 1, memo) + generate_fibonacci_recursive(n - 2, memo)
    return memo[n]

def get_fibonacci_sequence(limit):
    sequence = []
    i = 0
    while True:
        next_value = generate_fibonacci_recursive(i)
        if next_value >= limit:
            break
        sequence.append(next_value)
        i += 1
    return sequence

def display_fibonacci_sequence(seq):
    print("The Fibonacci sequence up to the specified limit is:")
    for idx, num in enumerate(seq):
        print(f"Fibonacci[{idx}] = {num}")

def main():
    limit = 100
    fibonacci_sequence = get_fibonacci_sequence(limit)
    display_fibonacci_sequence(fibonacci_sequence)

if __name__ == "__main__":
    main()
