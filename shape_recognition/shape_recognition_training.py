import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Step 1: Import all the images as a datase

#Reads in x_train and y_train values from a folder
def get_dataset(address, shape): # returns x and y of a target address 

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

for i in range(len(shapes)):
    (x_train_new, y_train_new) = get_dataset(addresses[0], shapes[i])
  
    plt.imshow(x_train_new[1], cmap = plt.cm.binary)
    plt.show()

    if i == 0:
        x_train = x_train_new
        y_train = y_train_new
        continue
    
    x_train = np.append(x_train, x_train_new)
    y_train = np.append(y_train, y_train_new)

print(y_train[100])

address1 = f"shape_recognition/shapesdataset/test_set"
shape1 = f"angleCross"
(x_train, y_train) = get_dataset(address1, shape1)
# # Proves we have got what we want
plt.imshow(x_train[51], cmap = plt.cm.binary)
plt.show()
print(y_train[51])
print(x_train[51])