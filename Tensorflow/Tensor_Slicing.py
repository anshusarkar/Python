import tensorflow as tf
import numpy as np # just used numpy because i could have lol 
matrix =np.array([[1,5] , 
                  [65,36] ,
                  [3,4],
                  [8,0]])

tensor = tf.Variable(matrix , dtype=tf.int64)

# print(tf.rank(tensor))

# print(tf.shape(tensor))


third_element = tensor[0,2]
