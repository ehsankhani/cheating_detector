def get_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        num_list = [int(line.strip()) for line in file]
    return num_list

def square_values(num_list):
    squared_list = [n ** 2 for n in num_list]
    return squared_list

def save_numbers_to_file(squared_list, file_name):
    with open(file_name, 'w') as file:
        for num in squared_list:
            file.write(f"{num}\n")

def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    numbers = get_numbers_from_file(input_filename)
    squared = square_values(numbers)
    save_numbers_to_file(squared, output_filename)
    print(f"Results written to {output_filename}")

if __name__ == "__main__":
    main()
