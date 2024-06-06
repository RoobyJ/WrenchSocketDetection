import os
path = 'PATH_TO_YOUR_PHOTOS'
for file in os.listdir(path):
    print(file)
    if os.path.isfile(path + file) and file[-3:] != ".py":
        results = model.predict(path + file, save=False, imgsz=1440, conf=0.1)