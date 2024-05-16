import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Step 1: Import all the images as a datase

#Reads in x_train and y_train values from a folder
def train_from(address, shape): # Both must be fstrings, 
    training_set_size = len(os.listdir(f"{address}/{shape}"))
    y_train = np.array(training_set_size)
    x_train = np.array(training_set_size)
    
    shape_number = 1

    while os.path.isfile(f"{address}/{shape}_{"{:02d}".format(shape_number)}.png"): # so long as there is a shape here
        try:
            x_train.append
        except:
            #Failed
            print("Error!")
        finally:
            shape_number += 1
            #idfk how this works
    return (x_train, y_train)


