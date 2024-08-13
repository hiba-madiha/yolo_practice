from roboflow import Roboflow
import os

def download_data():
    HOME = os.getcwd()  # Get the current working directory
    dataset_dir = os.path.join(HOME, 'dataset')  # Create the path for the dataset folder
    
    # Check if the directory exists; if not, create it
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)

    os.chdir(dataset_dir)  # Change the current working directory to the dataset folder
    
    rf = Roboflow(api_key="rDVmqwQ044wktmZwBCe7")  # Initialize Roboflow with your API key
    project = rf.workspace("seif-el-din-amr-kamel").project("ic-defect")  # Access the specific project
    version = project.version(1)  # Access the specific version of the project
    dataset = version.download("yolov8")  # Download the dataset
    
    #return dataset  # Return the dataset object
    return dataset    # Return the dataset object

