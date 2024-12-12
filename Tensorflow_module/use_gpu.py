##!/home/anshu/anaconda3/envs/Tensorflow-gpu/bin/python

# In the above line of the shebang command Tensorflow is the name of the environment variable of my system change it accordiong

import tensorflow as tf
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
    raise SystemError('GPU devicec not found')
print('Found GPU at : {}'.format(device_name))