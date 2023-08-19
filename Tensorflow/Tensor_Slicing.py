import tensorflow as tf
import numpy as np # just used numpy because i could have lol 
matrix =np.array([[1,5] , 
                  [65,36] ,
                  [3,4],
                  [8,0]])

tensor = tf.Variable(matrix , dtype=tf.int64)

# print(tf.rank(tensor))

# print(tf.shape(tensor))


third_element = tensor[0,2] # I DON'T KNOW why slicng insn't working

row1 = tensor[0] #Selects the first row

column1 = tensor[: , 0] #Selects the 1st column


row2_and_row4 = tensor[1::2] #Selects the 2nd and 4th row





 

