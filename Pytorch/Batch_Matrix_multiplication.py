import torch as tor 
# Batch martices are batches of matrices
# in the function below rand(10,3,4) 1st paramiters is the batch number 
# And 2nd parameter is row size and 3rd parameter is column size
batch1 = tor.rand(10,3,4) 
batch2 = tor.rand(10,4,5)

res = tor.bmm(batch1, batch2)

print(res.size())