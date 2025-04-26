# Phishing Detection and Cybersecurity Awareness Tool

## Project Overview
This project is focused on detecting phishing emails using machine learning and providing a cybersecurity awareness program for enterprise employees. It leverages the Enron Spam Dataset to train a Naive Bayes model for phishing detection and includes an interactive awareness program to educate users on recognizing and preventing phishing attacks. The tool is designed for local deployment and is uploaded to GitHub for sharing and collaboration.

### Objectives
- **Phishing Detection**: Develop a machine learning model to classify emails as phishing ("spam") or legitimate ("ham") with a user-friendly GUI.
- **Cybersecurity Awareness**: Create an educational program with a detailed guide, an interactive quiz (text-based and GUI versions), and simulated phishing emails.
- **Enterprise Focus**: Tailor the program to enterprise employees, addressing risks like data breaches and operational disruptions.

### Technologies Used
- **Python 3.8+**
- **Machine Learning Libraries**: `pandas`, `numpy`, `scikit-learn`
- **NLP**: `nltk`
- **GUI Framework**: `tkinter`
- **Visualization**: `matplotlib`
- **Serialization**: `joblib`

---

## Setup Instructions

1. **Install Python**:  
   Install Python 3.8 or higher from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/<akobabs>/phishing-detection-project.git
   cd phishing-detection-project
   ```

3. **Set Up a Virtual Environment** (Recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Download NLTK Data**:
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

6. **Download the Enron Spam Dataset**:
   - Download from [Kaggle](https://www.kaggle.com/datasets/wcukierski/enron-spam).
   - Place it in the `data/` directory as `enron_spam_data.csv`.

---

## Usage Guide

### 1. Phishing Detection

#### Step 1: Preprocess the Dataset
```bash
python src/preprocess_data.py
```
- Combines subject and body into a single text field.
- Cleans and preprocesses text.
- Outputs `data/cleaned_emails.csv`.

#### Step 2: Train the Model
```bash
python src/phishing_detector.py
```
- Trains a `MultinomialNB` model.
- Saves model and TF-IDF vectorizer to `models/`.

Example output:
```
Accuracy: 0.947
Classification Report:
    precision    recall  f1-score   support
ham     0.93        0.97       0.95      3000
spam    0.96        0.92       0.94      2500
```

#### Step 3: Run the GUI Detector
```bash
python src/phishing_detector_gui.py
```
- Input email text and get classification.
- View prediction confidence and ROC-AUC graph.

---

### 2. Cybersecurity Awareness Program

#### Step 1: Read the Awareness Guide
- Open `docs/phishing_awareness.md`.

#### Step 2: Take the Phishing Awareness Quiz
- **GUI Version**:
  ```bash
  python src/phishing_quiz_gui.py
  ```
- **Text-Based Version**:
  ```bash
  python src/phishing_quiz.py
  ```

#### Step 3: Practice with Simulated Phishing Emails
```bash
python src/simulate_phishing.py
```
- Displays random simulated phishing scenarios.
- Highlights phishing red flags.

---

## Features

### Phishing Detection
- Command-line and GUI-based phishing detection.
- Model confidence scores and explainability.
- ROC-AUC performance visualization.

### Cybersecurity Awareness
- Awareness guide tailored for enterprises.
- Interactive quizzes (GUI and CLI).
- Simulated phishing email practice.

---

## File Structure
```
phishing-detection-project/
├── data/
│   ├── enron_spam_data.csv
│   └── cleaned_emails.csv
├── models/
│   ├── nb_model.joblib
│   └── tfidf_vectorizer.joblib
├── src/
│   ├── preprocess_data.py
│   ├── phishing_detector.py
│   ├── phishing_detector_gui.py
│   ├── phishing_quiz.py
│   ├── phishing_quiz_gui.py
│   └── simulate_phishing.py
├── docs/
│   ├── phishing_awareness.md
│   ├── results.md
│   ├── demo_gui.png
│   └── demo_quiz_gui.png
├── requirements.txt
└── README.md
```

---

## Results
- **Accuracy**: 94.7%
- **Precision (Spam)**: 96%
- **Recall (Spam)**: 92%
- **F1-Score (Spam)**: 94%
- **ROC-AUC**: 0.95

Full results available in `docs/results.md`.

---

## Demo Screenshots

### GUI Detector
![GUI Detector with ROC-AUC and Explainability](docs/demo_gui.png)

### GUI Quiz
![GUI Quiz](docs/demo_quiz_gui.png)

---

## Troubleshooting
- **GUI Not Opening**: Ensure `tkinter` and `matplotlib` are installed.  
  On Linux:
  ```bash
  sudo apt-get install python3-tk
  ```
- **Missing Files**: Make sure `enron_spam_data.csv` is placed under `data/`.
- **NLTK Errors**: Re-run the NLTK download commands for missing resources.

---

## Status
✅ Fully functional:
- Phishing detection with CLI and GUI.
- Full cybersecurity awareness program.
- Complete documentation and screenshots.

---

## Future Improvements
- Add more explainability features.
- Expand phishing email simulation scenarios.
- Merge awareness tools into a single GUI dashboard.

---

## Acknowledgments
- Enron Spam Dataset: [Kaggle Dataset](https://www.kaggle.com/datasets/wcukierski/enron-spam)