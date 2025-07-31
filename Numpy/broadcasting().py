import numpy as np

array1 = np.array([[1,2,3,4]]) #it's a 2d array with 1 row

array2 = np.array([1],[2],[3],[4]) #it's a 2d array with 1 coloum 

print(array1.shape)
print(array2.shape)

print(array1 * array2) #it's called array broadcasting, basically 2d array multiplication 