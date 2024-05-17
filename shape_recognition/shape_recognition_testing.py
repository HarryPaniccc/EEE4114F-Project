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