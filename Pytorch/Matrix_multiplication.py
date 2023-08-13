import torch as tor 

mat1 = tor.rand(3,3)

mat2 = tor.rand(3,3)

res = tor.mm(mat1 , mat2) # this function multiplies matrices 

print (res)