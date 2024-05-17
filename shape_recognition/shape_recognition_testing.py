import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

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

model = tf.keras.models.load_model('shape_recognition.keras')

test_image_number = 1
while os.path.isfile(f"shape_recognition/homegrowntests/test_image_{test_image_number}.jpg"): # so long as there is a shape here, excuse gross address formatting
    try:
        img = cv2.imread(f"shape_recognition/homegrowntests/test_image_{test_image_number}.jpg")[:,:,0]
        # img = np.invert(np.array([img]))
        img = np.array([img])
        prediction = model.predict(img)
        chosen_shape = int(np.argmax(prediction))
        print(f"The shape is a {shapes[chosen_shape]}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    except:
        print("Error because Harry is an idiot!")
    finally:
        test_image_number += 1
