def quick_sort_algorithm(array):
    if len(array) <= 1:
        return array
    else:
        pivot_element = array[0]
        smaller_elements = [x for x in array[1:] if x <= pivot_element]
        larger_elements = [x for x in array[1:] if x > pivot_element]
        return quick_sort_algorithm(smaller_elements) + [pivot_element] + quick_sort_algorithm(larger_elements)

def execute_sorting():
    array = [10, 7, 8, 9, 1, 5]
    print("Initial array:", array)
    sorted_array = quick_sort_algorithm(array)
    print("Sorted array:", sorted_array)

if __name__ == "__main__":
    execute_sorting()
