import numpy as np
# Vector is actualy a singel dimensional array
arr = np.arange(5)
arr2 = np.array([1,5,9,6,7])
arr3 = []

for i in range(len(arr)):
    arr3.append(arr[i]+arr2[i])


print(" Two vectors are : " , arr , arr2)

print(" Addition of the two vectors are : " , arr3)
