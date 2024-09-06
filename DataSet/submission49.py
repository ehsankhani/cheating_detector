def read_from_file(path):
    with open(path, 'r') as f:
        nums = [int(line.strip()) for line in f]
    return nums

def square_num_list(nums):
    squared = [i ** 2 for i in nums]
    return squared

def write_to_output(squared, output_path):
    with open(output_path, 'w') as f:
        for n in squared:
            f.write(f"{n}\n")

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    numbers = read_from_file(input_file)
    squared_numbers = square_num_list(numbers)
    write_to_output(squared_numbers, output_file)
    print(f"Squared numbers are saved in {output_file}")

if __name__ == "__main__":
    main()
