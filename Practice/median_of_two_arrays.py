def median_of_two_arrays (arr1 : list, arr2 : list)->int:
    arr3 = arr1 + arr2

    arr3.sort()

    n = len(arr3)

    if (n % 2 == 0 ):
        median_index1 = n / 2 # it could havebeen n // 2 which would be returning an integer but I type casted it anyway ,,, 
        median_index1 = int(median_index1)
        median_index2 = median_index1 - 1
        median = (arr3[median_index1] + arr3[median_index2]) / 2
        return median
    else :
        median_index = n / 2
        median_index = int(median_index)
        return arr3[median_index]




arr1 = [1,3,4,6,7,8]
arr2 = [2,5]

print(median_of_two_arrays(arr1, arr2))
