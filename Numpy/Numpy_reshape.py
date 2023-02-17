import numpy as np

arr = np.arange(4).reshape(2,2) #reshape(Matrix row , Matrix coloum)

print(arr)

print("The shape of the matrix is : ", arr.shape) 
 
#Since the arr is a tuple 0 index of the tuple is going to be the row value..  

row_val=arr.shape[0]

print("Print the value of the row is ",row_val)






