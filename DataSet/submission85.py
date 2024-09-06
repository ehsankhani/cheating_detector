def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def main():
    arr = [5, 1, 4, 2, 8]
    print("Original array:", arr)
    bubble_sort_optimized(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
