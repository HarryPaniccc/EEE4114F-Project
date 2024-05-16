
import os
import cv2
import numpy
import matplotlib.pyplot as plt
import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#Normalizing all shit to be not 0,255 but 0,1
x_test = tf.keras.utils.normalize(x_test, axis = 1)


model = tf.keras.models.load_model('handwritten.keras')
loss, accuracy = model.evaluate(x_test, y_test)

print(loss)
print(accuracy)