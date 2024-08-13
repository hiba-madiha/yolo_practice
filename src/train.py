from ultralytics import YOLO
import os

def train_model():
    # Load and train the YOLO model
    HOME = os.getcwd()
    #dataset_path = os.path.join(HOME, 'dataset')
    dataset_path = os.path.join(HOME, 'IC-Defect-1')
    model = YOLO('yolov8n.pt')  # Load the YOLO model
    
    model.train(
        data=os.path.join(dataset_path, 'data.yaml'),
        epochs=1,
        imgsz=640,
        plots=True
    )
