##!/usr/bin/env tf-gpu
import tensorflow as tf
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
    raise SystemError('GPU devicec not found')
print('Found GPU at : {}'.format(device_name))