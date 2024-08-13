from ultralytics import YOLO
import os

def predict_images():
    HOME = os.getcwd()
    model = YOLO(os.path.join(HOME, 'runs/detect/train/weights/best.pt'))  # Load the trained model
    
    predictions = model.predict(
        source=os.path.join(HOME, 'IC-Defect-1/test/images/'),
        conf=0.25,
        save=True,
        line_thickness=1
    )
    return predictions
