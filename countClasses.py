import os

socket_6 =0
socket_12 = 0
socket_torx = 0

for file in os.listdir('C:\\Projects\\WrenchSocketDetection\\train_data\data\\train\\labels'):
    if os.path.isfile('C:\\Projects\\WrenchSocketDetection\\train_data\data\\train\\labels\\' + file) and file[-4:] == ".txt":
        f = open('C:\\Projects\\WrenchSocketDetection\\train_data\data\\train\\labels\\' + file, "r")
        x = f.readlines()

        for i in x:
            if (i[0] == '0'):
                socket_6 += 1

            if (i[0] == '1'):
                socket_12 += 1

            if (i[0] == '2'):
                socket_torx += 1
        f.close()

print(socket_6)
print(socket_12)
print(socket_torx)
