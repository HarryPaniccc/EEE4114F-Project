import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Step 1: Import all the images as a datase

#Reads in x_train and y_train values from a folder
def train_from(address, shape): # Both must be fstrings
    training_set_size = len(os.listdir(address + f"/" + shape))
    y_train = np.array(1)
    y_train[0] = shape
    shape_number = 1
    while os.path.isfile(address + f"/training_set" + shape):
        try:
            x_train.append
        except:
            #Failed
        finally:
            shape_number += 1
            #idfk how this works
    return (x_train, y_train)


