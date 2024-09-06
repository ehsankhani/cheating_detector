def read_numbers_gen(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield int(line.strip())

def square_numbers_gen(numbers):
    for number in numbers:
        yield number ** 2

def write_numbers_gen(squared_numbers, output_file):
    with open(output_file, 'w') as f:
        for number in squared_numbers:
            f.write(f"{number}\n")

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    numbers_gen = read_numbers_gen(input_file)
    squared_gen = square_numbers_gen(numbers_gen)
    write_numbers_gen(squared_gen, output_file)
    print(f"Squared numbers saved to {output_file}")

if __name__ == "__main__":
    main()
