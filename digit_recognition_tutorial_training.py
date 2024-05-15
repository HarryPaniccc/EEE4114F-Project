
import os
import cv2
import numpy
import matplotlib.pyplot as plt
import tensorflow as tf


mnist = tf.keras.datasets.mnist #Get dataset, all labeled

#Sets train data and labels, as well as test data and labels
(x_train, y_train), (x_test, y_test) = mnist.load_data()


#Normalizing all shit to be not 0,255 but 0,1
x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)

model = tf.keras.models.Sequential() #Basic?

model.add(tf.keras.layers.Flatten(input_shape = (28,28)))

model.add(tf.keras.layers.Dense(128, activation='relu'))

model.add(tf.keras.layers.Dense(128, activation='relu'))

model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)

model.save('handwritten.keras')