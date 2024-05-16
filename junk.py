import os


directory = f"shape_recognition/shapesdataset/test_set/angleCross"
number_files = len(os.listdir(directory))

print(number_files)


address = f"shape_recognition/shapesdataset/test_set"
shape = f"angleCross"
training_set_size = len(os.listdir(f"{address}/{shape}"))
print(training_set_size)


count = 1
print(f"{address}/{shape}/{shape}_{"{:02d}".format(count)}.jpg")

while os.path.isfile(f"{address}/{shape}/{shape}_{"{:02d}".format(count)}.jpg"): # so long as there is a shape here
    count += 1


print(count)