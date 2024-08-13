from src.dataloader import download_data
from src.train import train_model
from src.predict import predict_images
from src.visualize import visualize_results

def main():
    # Download the dataset
    download_data()
    
    # Train the model
    train_model()
    
    # Predict using the trained model
    predict_images()
    
    # Visualize the results
    visualize_results()

if __name__ == "__main__":
    main()
