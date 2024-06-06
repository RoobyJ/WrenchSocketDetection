from ultralytics import YOLO


model = YOLO('yolov8l.pt')
if __name__ == '__main__':
        results = model.train(data='data/YOLO_3D.yaml', epochs=1200, imgsz=1280, device=[0], batch=4, cache=True, patience=1000)

# For resuming training
# model = YOLO('runs/detect/train24/weights/last.pt')
# if __name__ == '__main__':
#         results = model.train(resume=True)