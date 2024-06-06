import os

for i, file in enumerate(os.listdir('.')):
    if file[-3:] != '.py':
        os.rename(file, '2_' + file[2:-4] + ".jpg")
