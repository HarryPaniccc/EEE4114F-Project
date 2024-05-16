import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Step 1: Import all the images as a datase

#Reads in x_train and y_train values from a folder
def training_from(address, shape): # Both must be fstrings, 

    training_set_size = len(os.listdir(f"{address}/{shape}"))

    x_train = np.empty((training_set_size, 64, 64))
    y_train = np.full(training_set_size,shape, dtype='<U20')

    # x_train = [np.empty(64 * 64) for _ in range(training_set_size)]
    # y_train = [np.empty(64 * 64) for _ in range(training_set_size)]
    
    shape_number = 1

    while os.path.isfile(f"{address}/{shape}/{shape}_{"{:02d}".format(shape_number)}.jpg"): # so long as there is a shape here
        try:
            img = cv2.imread(f"{address}/{shape}/{shape}_{"{:02d}".format(shape_number)}.jpg")[:,:,0]
            img = np.invert(np.array([img]))
            x_train[shape_number - 1] = img
            y_train[shape_number - 1] = shape
            #x_train[0] = img
        except:
            #Failed
            print("Error!")
        finally:
            shape_number += 1
            #idfk how this works
    return (x_train, y_train)

address1 = f"shape_recognition/shapesdataset/test_set"
shape1 = f"angleCross"
(x_train, y_train) = training_from(address1, shape1)

# Proves we have got what we want
plt.imshow(x_train[1], cmap = plt.cm.binary)
plt.show()
print(y_train[1])