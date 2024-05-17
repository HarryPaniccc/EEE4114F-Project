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
    y = np.full(training_set_size, 0)
    # y = np.full(training_set_size,shape, dtype='<U20')
    

    while os.path.isfile(f"{address}/{shape}/{shape}_{"{:02d}".format(shape_number)}.jpg"): # so long as there is a shape here, excuse gross address formatting
        try:
            img = cv2.imread(f"{address}/{shape}/{shape}_{"{:02d}".format(shape_number)}.jpg")[:,:,0]
            img = np.invert(np.array([img]))
            x[shape_number - index_difference] = img #again, indexing is broken because of how dataset is labelled
            y[shape_number - index_difference] = shapes.index(shape)
            # y[shape_number - index_difference] = shape
        except:
            #Failed
            print("Error because Harry is an idiot!")
        finally:
            shape_number += 1
            #idfk how this works
    return (x, y)

def get_dataset(address, shapes): # returns all labelled data from a dataset
    for i in range(len(shapes)):
        (x_new, y_new) = get_shape_data(address, shapes[i])
  
        # plt.imshow(x_new[1], cmap = plt.cm.binary)
        # plt.show()

        if i == 0:
            x = x_new
            y = y_new
            continue

        x = np.append(x, x_new, 0)
        y = np.append(y, y_new, 0)

    return (x, y)


addresses = [f"shape_recognition/shapesdataset/training_set", f"shape_recognition/shapesdataset/test_set"]

                            # Indices:
                            # --------
shapes = [f"angleCross",    # 0
          f"ellipse",       # 1
          f"hexagon",       # 2
          f"line",          # 3
          f"square",        # 4
          f"straightCross", # 5
          f"triangle"]      # 6

(x_train, y_train) = get_dataset(addresses[0], shapes) #training data
(x_test, y_test) = get_dataset(addresses[1], shapes) #testing data

x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)


max_epochs = 30
epochs = np.linspace(1, max_epochs, max_epochs)
print(epochs)
loss_list = []
accuracy_list = []

# Generates many models for a bunch of epochs to see which is most effective
for i in epochs:
    model = tf.keras.models.Sequential()
    # model.add(tf.keras.layers.Flatten(input_shape = (64,64)))

    model.add(tf.keras.layers.Conv2D(2,5, activation='relu',input_shape=(64,64,1)))
    model.add(tf.keras.layers.Flatten(input_shape=(60,60)))

    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dense(7, activation='softmax'))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=int(i))

    loss, accuracy = model.evaluate(x_test, y_test)
    loss_list.append(loss)
    accuracy_list.append(accuracy)

print(accuracy_list)

for i in epochs:
    print(f"For {int(i)} epochs we have {loss_list[int(i)-1]:.4f} loss and {accuracy_list[int(i)-1]:.4f} accuracy")

plt.plot(epochs, np.subtract(1, accuracy_list), color='red')
plt.plot(epochs, loss_list, color='blue')
plt.ylabel("Number of Epochs")
plt.legend(["Error", "Loss"], loc="upper right")
plt.show()