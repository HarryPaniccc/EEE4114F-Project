import os


directory = f"shape_recognition/shapesdataset/test_set/angleCross"
number_files = len(os.listdir(directory))

print(number_files)


address = f"shape_recognition/shapesdataset/test_set"
shape = f"angleCross"
training_set_size = len(os.listdir(address + f"/" + shape))
print(training_set_size)