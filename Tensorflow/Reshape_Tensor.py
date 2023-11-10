import tensorflow as tf 

tensor1 = tf.ones([1,2,3]) # one 2x3 tensor 

print(tensor1)


tensor2 = tf.reshape(tensor1 , [2,3,1]) # two 3x1 tensors 

print(tensor2)


tensor3 = tf.reshape(tensor2 , [3,2,1]) # three 2x1 tensors

print(tensor3)


tensor4 = tf.zeros([2,3,4]) # two 3x4 matrix

print(tensor4)

tensor5 = tf.reshape(tensor4 , [2,-1]) # converts 3x4 tensor to 3x1 tensor though applyes on tensor that consists elements more than target tensor

print(tensor5)
