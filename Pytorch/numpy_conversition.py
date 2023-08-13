import torch as tor 

x = tor.rand (4,4)
a = tor.ones (5)
z = x.numpy() # numpy array or any array is processed by cpu
              # where tensors are handeled by gpr
              # .numpy() function does the converts them 
b = a.numpy()
print(z)
print(b)