import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent
CLEANED_FILE = BASE_DIR / 'data' / 'cleaned_emails.csv'
MAINMODEL_FILE = BASE_DIR / 'models' / 'nb_model.joblib'
VECTORIZER_FILE = BASE_DIR / 'models' / 'tfidf_vectorizer.joblib'

# Text preprocessing function
def preprocess_text(text):
    text = str(text).lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Load cleaned dataset
df = pd.read_csv(CLEANED_FILE)

# Drop missing values and handle 'nan' strings
df['cleaned_text'] = df['cleaned_text'].replace('nan', pd.NA)
df = df.dropna(subset=['cleaned_text', 'label'])

# Prepare features and labels
X = df['cleaned_text']
y = df['label']

# Convert text to TF-IDF features
vectorizer = TfidfVectorizer(max_features=5000)
X_tfidf = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model and vectorizer
joblib.dump(model, MAINMODEL_FILE)
joblib.dump(vectorizer, VECTORIZER_FILE)

# Predict new email
def predict_email(email_text):
    model = joblib.load(MAINMODEL_FILE)
    vectorizer = joblib.load(VECTORIZER_FILE)
    cleaned_text = preprocess_text(email_text)
    email_tfidf = vectorizer.transform([cleaned_text])
    prediction = model.predict(email_tfidf)
    return "Phishing" if prediction[0] == 'spam' else "Legitimate"

# Example usage
if __name__ == "__main__":
    sample_email = "Urgent: Update your account now to avoid suspension!"
    result = predict_email(sample_email)
    print(f"Sample email prediction: {result}")

    sample_email2 = "Hi, let's meet for coffee tomorrow."
    result2 = predict_email(sample_email2)
    print(f"Sample email 2 prediction: {result2}")