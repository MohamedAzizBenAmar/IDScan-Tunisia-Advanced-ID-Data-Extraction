from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2

# Load the model
model = load_model("converted_keras_v/keras_model.h5", compile=False)


# Load the labels (if needed)
# class_names = open("labels.txt", "r").readlines()

def correct_image_rotation(image_path, model):
    # Load the original image
    original_img = Image.open(image_path).convert("RGB")  # Ensure the image is in RGB format
    original_width, original_height = original_img.size  # Get original dimensions

    # Resize and preprocess the image for model input
    img = ImageOps.fit(original_img, (224, 224), Image.LANCZOS)  # Resize to (224, 224) using LANCZOS
    img_array = np.array(img) / 255.0  # Convert to numpy array and normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make prediction
    prediction = np.argmax(model.predict(img_array), axis=1)[0]

    # Correct rotation based on prediction
    if prediction == 1:
        rotated_img = np.array(original_img)  # No rotation
    elif prediction == 0:
        rotated_img = np.rot90(np.array(original_img), k=1, axes=(0, 1))
    elif prediction == 3:
        rotated_img = np.rot90(np.array(original_img), k=2, axes=(0, 1))
    elif prediction == 2:
        rotated_img = np.rot90(np.array(original_img), k=3, axes=(0, 1))

    return rotated_img


# Correct the rotation of a new image
image_path = 'C12.jpg'
corrected_image = correct_image_rotation(image_path, model)

# Save or display the corrected image
if corrected_image is not None:
    Image.fromarray(corrected_image).save('corrected_image.jpg')
    # Uncomment the following line to display the corrected image
    # Image.fromarray(corrected_image).show()
else:
    print("No valid image rotation produced for the given image.")