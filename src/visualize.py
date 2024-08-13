from PIL import Image as PilImage
import glob
import os

def visualize_results():
    HOME = os.getcwd()  # Get the current working directory
    #print(HOME)
    image_paths = glob.glob(f'{HOME}/runs/detect/predict/*.jpg')  # Find all .jpg files in the specified directory
    #image_paths = glob.glob(f'J:/Codes/yolo_proj/dataset/runs/detect/predict/*.jpg')  # Find all .jpg files in the specified directory
    print(HOME)

    if not image_paths:
        print("No images found.")
        return

    for image_path in image_paths[:5]:
        image = PilImage.open(image_path)  # Open the image using PIL
        image.show()  # Display the image
        print(f"Displaying: {image_path}\n")  # Print the path of the image being displayed

if __name__ == "__main__":
    visualize_results()



'''
from IPython.display import Image, display
import glob
import os

def visualize_results():
    HOME = os.getcwd()
    for image_path in glob.glob(f'{HOME}/runs/detect/predict/*.jpg'):
        display(Image(filename=image_path, width=600))
        print("\n")
'''
