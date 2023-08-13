import torch as tor 

x = tor.rand(4,4)

y = x.view(16) # view is used to resize / reshape the tensor
z = x.view(-1 , 8)
print(y.size()) # y is now a linear array
print(z.size()) # z is now a 2x8 matrix 