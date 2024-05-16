import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Step 1: Import all the images as a datase

#Reads in x_train and y_train values from a folder
def get_shape_data(address, shape): # returns labeled set of one label type 

    training_set_size = len(os.listdir(f"{address}/{shape}"))

    if address == f"shape_recognition/shapesdataset/training_set":
        shape_number = 41
        index_difference = 41
    else:
        shape_number = 1
        index_difference = 1
	

    x = np.empty((training_set_size, 64, 64))
    y = np.full(training_set_size,shape, dtype='<U20')
    

    while os.path.isfile(f"{address}/{shape}/{shape}_{"{:02d}".format(shape_number)}.jpg"): # so long as there is a shape here, excuse gross address formatting
        try:
            img = cv2.imread(f"{address}/{shape}/{shape}_{"{:02d}".format(shape_number)}.jpg")[:,:,0]
            img = np.invert(np.array([img]))
            x[shape_number - index_difference] = img #again, indexing is broken because of how dataset is labelled
            y[shape_number - index_difference] = shape
            #x_train[0] = img
        except:
            #Failed
            print("Error because Harry is an idiot!")
        finally:
            shape_number += 1
            #idfk how this works
    return (x, y)


def get_dataset(addresses, shapes): # returns all labelled data from a dataset
    for i in range(len(shapes)):
        (x_new, y_new) = get_shape_data(addresses[0], shapes[i])
  
        plt.imshow(x_new[1], cmap = plt.cm.binary)
        plt.show()

        if i == 0:
            x = x_new
            y = y_new
            continue

        x = np.append(x, x_new, 0)
        y = np.append(y, y_new, 0)

    return (x, y)

# Defining our target addresses and labels
addresses = [f"shape_recognition/shapesdataset/training_set",
             f"shape_recognition/shapesdataset/test_set"]

shapes = [f"angleCross", 
          f"ellipse", 
          f"hexagon", 
          f"line", 
          f"square", 
          f"straightCross", 
          f"triangle"]

(x_train, y_train) = get_dataset(addresses, shapes)

# From this point on our x_train and y_train is correct