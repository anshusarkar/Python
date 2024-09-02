import tensorflow as tf
tf.__version__
#print(tf.config.list_physical_devices('GPU'))

#To declear a Variable in tensorflow tf.Variable get's used

string = tf.Variable("This is a string", tf.string)
number = tf.Variable(325, tf.int64)
floating = tf.Variable(9.32 , tf.float64)

