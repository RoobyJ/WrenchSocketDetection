from ultralytics import YOLO
from fastapi import FastAPI
from enum import Enum
import cv2


class Socket(Enum):
    Hex = 0
    Twelve = 1
    Torx = 2


class ObjectDto:
    socketSixCount = 0
    socketTwelveCount = 0
    socketTorxCount = 0

    def __init__(self, socketSixCount=0, socketTwelveCount=0, socketTorxCount=0):
        self.socketSixCount = socketSixCount
        self.socketTwelveCount = socketTwelveCount
        self.socketTorxCount = socketTorxCount


app = FastAPI()

model = YOLO('best.pt', )


@app.get("/getObjects")
async def root():
    cam = cv2.VideoCapture(0)
    _, image = cam.read()
    print(image)
    results = model.predict(image, save=True, imgsz=1280, conf=0.1)
    hexCount = 0
    twelveCount = 0
    torxCount = 0
    for r in results:
        for x in range(0, len(r.boxes.cls)):
            match Socket(int(r.boxes.cls[x].item())):
                case Socket.Hex:
                    hexCount += 1
                case Socket.Twelve:
                    twelveCount += 1
                case Socket.Torx:
                    torxCount += 1

    return ObjectDto(hexCount, twelveCount, torxCount)

# run api by command: uvicorn detection:app
# below is code for testing for a set of ready pictures
# import os
# path = 'PATH_TO_YOUR_PHOTOS'
# for file in os.listdir(path):
#     print(file)
#     if os.path.isfile(path + file) and file[-3:] != ".py":
#         results = model.predict(path + file, save=False, imgsz=1280, conf=0.1)
#         for r in results:
#             print(r.boxes[0].xyxy)
#
#     break


