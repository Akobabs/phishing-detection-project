import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import roc_curve, auc
import joblib
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Base directory (same as phishing_detector.py)
BASE_DIR = Path(__file__).resolve().parent.parent
CLEANED_FILE = BASE_DIR / 'data' / 'cleaned_emails.csv'
MAINMODEL_FILE = BASE_DIR / 'models' / 'nb_model.joblib'
VECTORIZER_FILE = BASE_DIR / 'models' / 'tfidf_vectorizer.joblib'

class PhishingDetectorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Phishing Email Detector")
        self.root.geometry("900x600")
        self.root.configure(bg="#e0e0e0")

        # Initialize model and vectorizer
        try:
            self.model = joblib.load(MAINMODEL_FILE)
            self.vectorizer = joblib.load(VECTORIZER_FILE)
        except FileNotFoundError:
            messagebox.showerror("Error", "Model or vectorizer file not found. Run phishing_detector.py first.")
            self.root.destroy()
            return

        # Load dataset for ROC-AUC
        try:
            self.df = pd.read_csv(CLEANED_FILE)
            self.df = self.df.dropna(subset=['cleaned_text', 'label'])  # Drop missing values
            self.df['cleaned_text'] = self.df['cleaned_text'].replace('nan', pd.NA)  # Replace 'nan' strings
            self.df = self.df.dropna(subset=['cleaned_text'])  # Drop again after replacing
            self.X = self.df['cleaned_text']
            self.y = self.df['label'].map({'spam': 1, 'ham': 0})  # Convert labels to 0/1 for ROC
            self.X_tfidf = self.vectorizer.transform(self.X)
        except FileNotFoundError:
            messagebox.showerror("Error", "Dataset 'cleaned_emails.csv' not found.")
            self.root.destroy()
            return
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process dataset: {str(e)}")
            self.root.destroy()
            return

        # Create GUI elements
        self.create_gui()

        # Plot ROC-AUC on startup
        self.plot_roc_auc()

    def preprocess_text(self, text):
        text = str(text).lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]
        return ' '.join(tokens)

    def create_gui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Left frame (Input, Output, Explainability)
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        # Input section
        ttk.Label(left_frame, text="Enter Email Text:", font=("Helvetica", 14, "bold")).pack(anchor="w")
        self.input_text = scrolledtext.ScrolledText(left_frame, height=6, width=50, font=("Helvetica", 11), borderwidth=2, relief="groove")
        self.input_text.pack(pady=5, fill=tk.BOTH, expand=True)
        self.input_text.insert(tk.END, "Enter your email here...")

        # Predict button
        ttk.Button(left_frame, text="Predict", command=self.predict_email, style="TButton").pack(pady=10)

        # Prediction section
        self.prediction_label = ttk.Label(left_frame, text="Prediction: N/A", font=("Helvetica", 14, "bold"), foreground="#333333")
        self.prediction_label.pack(pady=5)

        # Confidence section
        self.confidence_label = ttk.Label(left_frame, text="Confidence: N/A", font=("Helvetica", 12), foreground="#555555")
        self.confidence_label.pack(pady=5)

        # Explainability section
        ttk.Label(left_frame, text="Explainability (Top Influential Words):", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(10, 0))
        self.explanation_text = scrolledtext.ScrolledText(left_frame, height=6, width=50, font=("Helvetica", 11), borderwidth=2, relief="groove")
        self.explanation_text.pack(pady=5, fill=tk.BOTH, expand=True)
        self.explanation_text.config(state='disabled')

        # Right frame (ROC-AUC Graph)
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)

        # ROC-AUC plot
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=right_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Configure button style
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10, background="#4CAF50", foreground="white")
        style.map("TButton", background=[('active', '#45a049')])

    def plot_roc_auc(self):
        try:
            # Get model probabilities for ROC
            y_scores = self.model.predict_proba(self.X_tfidf)[:, 1]  # Probability for 'spam'
            fpr, tpr, _ = roc_curve(self.y, y_scores)
            roc_auc = auc(fpr, tpr)

            # Plot ROC curve
            self.ax.clear()
            self.ax.plot(fpr, tpr, color='#1f77b4', lw=2, label=f'ROC Curve (AUC = {roc_auc:.2f})')
            self.ax.plot([0, 1], [0, 1], color='gray', lw=1, linestyle='--', label='Random Guess')
            self.ax.set_xlim([0.0, 1.0])
            self.ax.set_ylim([0.0, 1.05])
            self.ax.set_xlabel('False Positive Rate', fontsize=10)
            self.ax.set_ylabel('True Positive Rate', fontsize=10)
            self.ax.set_title('ROC-AUC Curve', fontsize=12, pad=10)
            self.ax.legend(loc="lower right", fontsize=8)
            self.ax.grid(True, linestyle='--', alpha=0.7)
            self.ax.set_facecolor('#f9f9f9')
            self.fig.tight_layout()
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to plot ROC-AUC: {str(e)}")

    def get_explanation(self, email_text):
        # Preprocess and transform email text
        cleaned_text = self.preprocess_text(email_text)
        email_tfidf = self.vectorizer.transform([cleaned_text]).toarray()[0]

        # Get feature names (words) from vectorizer
        feature_names = self.vectorizer.get_feature_names_out()

        # Get log probabilities from Naive Bayes for spam and ham
        log_prob_spam = self.model.feature_log_prob_[1]  # Spam class
        log_prob_ham = self.model.feature_log_prob_[0]   # Ham class

        # Calculate the difference in log probabilities (indicating influence)
        influence = log_prob_spam - log_prob_ham
        word_influence = [(feature_names[i], influence[i] * email_tfidf[i]) for i in range(len(feature_names)) if email_tfidf[i] > 0]
        word_influence.sort(key=lambda x: abs(x[1]), reverse=True)

        # Return top 5 words contributing to the prediction
        top_words = word_influence[:5]
        explanation = "\n".join([f"{word}: Influence Score = {score:.4f}" for word, score in top_words])
        return explanation

    def predict_email(self):
        # Get email text from input
        email_text = self.input_text.get("1.0", tk.END).strip()
        if not email_text or email_text == "Enter your email here...":
            messagebox.showwarning("Input Error", "Please enter an email text.")
            return

        try:
            # Preprocess and predict
            cleaned_text = self.preprocess_text(email_text)
            email_tfidf = self.vectorizer.transform([cleaned_text])
            prediction = self.model.predict(email_tfidf)
            probabilities = self.model.predict_proba(email_tfidf)

            # Update prediction label
            result = "Phishing" if prediction[0] == 'spam' else "Legitimate"
            self.prediction_label.config(text=f"Prediction: {result}", foreground="#d32f2f" if result == "Phishing" else "#388e3c")

            # Update confidence
            confidence = max(probabilities[0]) * 100  # Convert to percentage
            self.confidence_label.config(text=f"Confidence: {confidence:.2f}%")

            # Update explainability
            explanation = self.get_explanation(email_text)
            self.explanation_text.config(state='normal')
            self.explanation_text.delete("1.0", tk.END)
            self.explanation_text.insert(tk.END, explanation)
            self.explanation_text.config(state='disabled')
        except Exception as e:
            messagebox.showerror("Error", f"Prediction failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhishingDetectorGUI(root)
    root.mainloop()