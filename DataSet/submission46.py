def read_numbers(file_path):
    with open(file_path, 'r') as f:
        numbers = list(map(int, f.readlines()))
    return numbers

def square_numbers_with_map(numbers):
    return list(map(lambda x: x ** 2, numbers))

def write_to_file(numbers, file_path):
    with open(file_path, 'w') as f:
        f.writelines(f"{num}\n" for num in numbers)

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    numbers = read_numbers(input_file)
    squared_numbers = square_numbers_with_map(numbers)
    write_to_file(squared_numbers, output_file)
    print(f"Processed numbers are saved in {output_file}")

if __name__ == "__main__":
    main()
