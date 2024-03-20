def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted. That utlizes "Divide and Conquer method" .
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


print("The key value is found at : ",binary_search(l,12)," using binary search.\n\n That",binary_search.__doc__)