# 🇹🇳 IDScan-Tunisia: Advanced National ID Data Extraction

IDScan-Tunisia is an automated system designed to extract structured data from **Tunisian National Identity Cards (CIN)** using advanced image processing and OCR technologies.

---

## 📌 Objective

Develop an automated and reliable solution to extract personal data from CIN cards through image preprocessing, OCR, and intelligent data structuring.

---

## 🛠️ Project Components

### 🔹 1. Image Preprocessing
- **Image Acquisition:** Using high-resolution cameras or scanners  
- **Image Enhancement:** Applying filters to improve clarity  
- **Perspective Correction:** Fixing geometric distortions  

---

### 🔹 2. Optical Character Recognition (OCR)
- **Text Detection:** Locating text regions on the CIN  
- **Text Extraction:** Using OCR engines (Tesseract, EasyOCR)  
- **Post-Processing:** Cleaning and correcting extracted text  

---

### 🔹 3. Information Extraction
- **Field Detection:** Identifying key fields (Name, First Name, CIN Number, etc.)  
- **Data Structuring:** Formatting results into **JSON**  

---

### 🔹 4. User Interface
- **Web Interface:** Simple GUI to view the card and extracted data  
- **Data Export:** JSON, CSV, Excel  

---

## 🏗️ Technologies Used

| Technology            | Usage                |
|----------------------|----------------------|
| **Python**           | Main programming language |
| **Tesseract, EasyOCR** | OCR engine for text extraction |
| **OpenCV, PIL**      | Image processing & preprocessing |
| **Flask**            | Web application backend |
| **JSON**             | Data storage & API format |

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/MohamedAzizBenAmar/IDScan-Tunisia-Advanced-ID-Data-Extraction.git
