# IDScan-Tunisia: Advanced National ID Data Extraction

## 📌 Objectif
Développer une solution automatisée pour extraire les données des Cartes d'Identité Nationales Tunisiennes (CIN) en utilisant le traitement d'image avancé et la reconnaissance optique de caractères (OCR).

---

## 🛠️ Composants du Projet

### 🔹 1. Prétraitement d'Image
- **Acquisition d'Image** : Utilisation de caméras haute résolution ou de scanners.
- **Amélioration de l'Image** : Application de filtres pour améliorer la qualité.
- **Correction de Perspective** : Correction des distorsions géométriques.

### 🔹 2. Reconnaissance Optique de Caractères (OCR)
- **Détection de Texte** : Identification des zones contenant du texte.
- **Extraction de Texte** : Conversion du texte en format numérique (Tesseract, EasyOCR).
- **Post-Traitement** : Nettoyage et correction des données extraites.

### 🔹 3. Extraction d'Informations
- **Identification des Champs** : Détection des informations clés (Nom, Prénom, CIN, etc.).
- **Structuration des Données** : Organisation des données extraites en format JSON.

### 🔹 4. Interface Utilisateur
- **Application Web/GUI** : Interface intuitive pour visualiser les images et les données extraites.
- **Exportation des Données** : Export en CSV, Excel ou JSON.

---

## 🏗️ Technologies Utilisées
| Technologie  | Utilisation  |
|-------------|-------------|
| **Python** | Langage principal |
| **Tesseract, EasyOCR** | OCR |
| **OpenCV, PIL** | Traitement d'images |
| **Flask** | Développement Web |
| **JSON Files** | Stockage des données |

---

## 🚀 Comment Exécuter le Projet ?

### 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/MohamedAzizBenAmar/IDScan-Tunisia-Advanced-ID-Data-Extraction.git
```
### 2️⃣ Aller dans le répertoire du projet
```bash
cd IDScan-Tunisia-Advanced-ID-Data-Extraction
```
### 3️⃣ Set up a virtual environment:
```bash
python -m venv venv
```
### 4️⃣ Activate the virtual environment:
```bash
venv\Scripts\activate
```
### 5️⃣Install the required dependencies:
```bash
pip install -r requirements.txt
```
### 6️⃣ Run the application: To start the web application, use:
```bash
python app.py
```

