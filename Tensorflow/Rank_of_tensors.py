##!/usr/bin/env tf

import tensorflow as tf 

Rank_1_tensor = tf.Variable(["Test"], tf.string)

# Rank of a tensor is nothing but it's dimension 

Rank_2_tensor = tf.Variable(["Test","One"] , ["Ok" , "Echo"] , tf.string)


#print (Rank_2_tensor)

print(Rank_2_tensor.shape)

