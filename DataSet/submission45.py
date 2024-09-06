def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def square_numbers(numbers):
    return [num ** 2 for num in numbers]

def write_numbers_to_file(numbers, output_file):
    with open(output_file, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    numbers = read_numbers_from_file(input_file)
    squared_numbers = square_numbers(numbers)
    write_numbers_to_file(squared_numbers, output_file)
    print(f"Squared numbers have been written to {output_file}")

if __name__ == "__main__":
    main()
