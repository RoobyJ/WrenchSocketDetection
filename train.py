from ultralytics import YOLO


model = YOLO('yolov8l.pt')
if __name__ == '__main__':
        results = model.train(data='data/YOLO_3D.yaml', epochs=100, imgsz=640, device=[0], batch=4 ,cache=True)
