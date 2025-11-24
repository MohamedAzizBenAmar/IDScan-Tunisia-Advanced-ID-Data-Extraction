IDScan-Tunisia: Advanced National ID Data Extraction

📌 Objective

To develop an automated solution for extracting data from Tunisian National Identity Cards (CIN) using advanced image processing and Optical Character Recognition (OCR).

🛠️ Project Components

🔹 1. Image Preprocessing

Image Acquisition: Using high-resolution cameras or scanners.

Image Enhancement: Applying filters to improve quality.

Perspective Correction: Correcting geometric distortions.

🔹 2. Optical Character Recognition (OCR)

Text Detection: Identifying zones containing text.

Text Extraction: Converting the text into digital format (Tesseract, EasyOCR).

Post-Processing: Cleaning and correcting the extracted data.

🔹 3. Information Extraction

Field Identification: Detecting key information (Name, First Name, CIN number, etc.).

Data Structuring: Organizing the extracted data into JSON format.

🔹 4. User Interface

Web Application/GUI: Intuitive interface for visualizing images and extracted data.

Data Export: Exporting to CSV, Excel, or JSON.

🏗️ Technologies Used

Technology

Usage

Python

Main Language

Tesseract, EasyOCR

OCR

OpenCV, PIL

Image Processing

Flask

Web Development

JSON Files

Data Storage

🚀 How to Run the Project

1️⃣ Clone the Repository

git clone [https://github.com/MohamedAzizBenAmar/IDScan-Tunisia-Advanced-ID-Data-Extraction.git](https://github.com/MohamedAzizBenAmar/IDScan-Tunisia-Advanced-ID-Data-Extraction.git)


2️⃣ Go to the Project Directory

cd IDScan-Tunisia-Advanced-ID-Data-Extraction


3️⃣ Set up a virtual environment:

python -m venv venv


4️⃣ Activate the virtual environment:

venv\Scripts\activate


5️⃣ Install the required dependencies:

pip install -r requirements.txt


6️⃣ Run the application: To start the web application, use:

python app.py
