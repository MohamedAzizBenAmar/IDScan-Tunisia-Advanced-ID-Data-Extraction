import json
from flask import Flask, request, render_template, redirect, jsonify
from werkzeug.utils import secure_filename
import os
import cv2
import easyocr
from ultralytics import YOLO
from tensorflow.keras.models import load_model
from PIL import Image
import pytesseract
from rotate import correct_image_rotation
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
app = Flask(__name__)
# Configure upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Load YOLOv8 model
model1 = YOLO("bestFace.pt")
model2 = YOLO("bestVerso.pt")
# Initialize EasyOCR reader
easyocr_reader = easyocr.Reader(['ar'])  # Specify the languages you want to recognize
# Function to add a border around the image to enhance OCR accuracy
def add_border(image, border_size=10, border_color=(255, 255, 255)):
    bordered_image = cv2.copyMakeBorder(image, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=border_color)
    return bordered_image
# Function to extract text from an image using EasyOCR and Tesseract
def extract_text(model, image):
    results = model(image)
    class_results = {}

    for result in results:
        boxes = []
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            boxes.append((x1, y1, x2, y2, box))

        boxes.sort(key=lambda x: x[1])

        for x1, y1, x2, y2, box in boxes:
            x1 -= 1; x2 += 1; y1 -= 1; y2 += 1
            cropped_image = image[y1:y2, x1:x2]  
            binary_cropped_image = add_border(cropped_image, border_size=10, border_color=(255, 255, 255))

            easyocr_results = easyocr_reader.readtext(binary_cropped_image, decoder='beamsearch', beamWidth=5,
                batch_size=1, workers=0, paragraph=True, detail=1, rotation_info=[0], min_size=3,
                contrast_ths=0.1, adjust_contrast=1, text_threshold=0.3, low_text=0.2,
                link_threshold=0.4, mag_ratio=1.0, width_ths=0.7)
            easyocr_text = " ".join([result[1] for result in easyocr_results if len(result) >= 1])
            tesseract_text = pytesseract.image_to_string(binary_cropped_image, lang='ara').strip()

            class_id = int(box.cls[0])
            class_name = result.names[class_id]
            confidence = float(box.conf)

            bbox_result = {
                "confidence": confidence,
                "easyocr_text": easyocr_text,
                "tesseract_text": tesseract_text
            }

            if class_name == "full_name":
                if class_name not in class_results:
                    class_results[class_name] = []
                class_results[class_name].append(bbox_result)
            elif class_name not in class_results or confidence > class_results[class_name]["confidence"]:
                class_results[class_name] = bbox_result

    detected_texts = []
    for class_name, results in class_results.items():
        if class_name == "full_name":
            for result in results:
                detected_texts.append({"class_name": class_name, **result})
        else:
            detected_texts.append({"class_name": class_name, **results})

    return detected_texts
# Route to render index.html for file upload
@app.route('/')
def index():
    return render_template('index.html')
# Route to handle file upload and text extraction
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file1' not in request.files or 'file2' not in request.files:
        return redirect(request.url)
    file1 = request.files['file1']
    file2 = request.files['file2']
    if file1.filename == '' or file2.filename == '':
        return redirect(request.url)
    if file1 and file2:
        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)
        filepath1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
        filepath2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
        file1.save(filepath1)
        file2.save(filepath2)
        # Process first image
        image1 = cv2.imread(filepath1)
        img1 = correct_image_rotation(filepath1, load_model("converted_keras/keras_model.h5", compile=False))
        Image.fromarray(img1).save('corrected_image1.jpg')
        extracted_texts1 = extract_text(model1,img1)
        # Process second image
        image2 = cv2.imread(filepath2)
        img2 = correct_image_rotation(filepath2, load_model("converted_keras_v/keras_model.h5", compile=False))
        Image.fromarray(img2).save('corrected_image2.jpg')
        extracted_texts2 = extract_text(model2,img2)
        # Combine results
        combined_results = {
            "image1": extracted_texts1,
            "image2": extracted_texts2
        }
        # Save the results to a single JSON file
        json_filename = f'results_{filename1}_{filename2}.json'
        with open(os.path.join(app.config['UPLOAD_FOLDER'], json_filename), 'w', encoding='utf-8') as f:
            json.dump(combined_results, f, ensure_ascii=False, indent=4)
        # Convert to JSON string with ensure_ascii=False and pretty print
        combined_results_json = json.dumps(combined_results, ensure_ascii=False, indent=4)
        # Return the JSON response with UTF-8 encoding
        response = app.response_class(
            response=combined_results_json,
            status=200,
            mimetype='application/json'
        )
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
if __name__ == '__main__':
    app.run(debug=True)
 