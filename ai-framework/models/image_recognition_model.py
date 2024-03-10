import torch
from torchvision import models, transforms
from PIL import Image
import json
import requests

# Define a transformation sequence for the input image
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def load_image(image_path):
    """Loads an image from the disk."""
    image = Image.open(image_path)
    return image

def predict_image(model, transformed_image):
    """Make a prediction with the pretrained model."""
    # Disable gradient calculation for inference
    with torch.no_grad():
        outputs = model(transformed_image.unsqueeze(0))
        _, predicted = outputs.max(1)
        return predicted.item()

def get_class_labels():
    """Load ImageNet class labels."""
    class_idx_url = 'https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json'
    class_idx = requests.get(class_idx_url).json()
    return class_idx

def main(image_path):
    # Load and preprocess the image
    image = load_image(image_path)
    transformed_image = transform(image)

    # Load a pretrained ResNet model
    model = models.resnet50(pretrained=True)
    model.eval()  # Set the model to inference mode

    # Make a prediction
    predicted_idx = predict_image(model, transformed_image)

    # Get human-readable class labels
    class_labels = get_class_labels()

    # Print the prediction
    print(f"Predicted class: {class_labels[predicted_idx]}")

if __name__ == "__main__":
    image_path = 'path/to/your/image.jpg'  # Update this path to your image file
    main(image_path)
