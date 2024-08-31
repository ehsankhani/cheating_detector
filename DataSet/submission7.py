def sort_bubble(array):
    length = len(array)
    for i in range(length):
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

nums = [64, 34, 25, 12, 22, 11, 90]
sort_bubble(nums)
print("Sorted array:", nums)
