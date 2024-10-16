arr = [1,4,6,7,8,89,8,6,4,6,9]


def bubble_sort(arr : list, n : int)->list:
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            return arr  


print(bubble_sort(arr, len(arr)))

