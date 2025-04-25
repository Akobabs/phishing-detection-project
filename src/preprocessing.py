import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / 'data' / 'enron_spam_data.csv'
CLEANED_FILE = BASE_DIR / 'data' / 'cleaned_emails.csv'

# Load dataset
df = pd.read_csv(DATA_FILE)

# Combine Subject and Message into a single text field
df['text'] = df['Subject'].astype(str) + ' ' + df['Message'].astype(str)

# Keep only relevant columns
df = df[['text', 'Spam/Ham']]

# Rename 'Spam/Ham' to 'label' for consistency
df = df.rename(columns={'Spam/Ham': 'label'})

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values (replace 'nan' strings and drop actual NaN)
df['text'] = df['text'].replace('nan nan', pd.NA)  # Handle cases where Subject and Message are both NaN
df = df.dropna(subset=['text', 'label'])

# Text preprocessing function
def preprocess_text(text):
    text = str(text).lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Apply preprocessing
df['cleaned_text'] = df['text'].apply(preprocess_text)

# Additional check to ensure no 'nan' strings remain in cleaned_text
df['cleaned_text'] = df['cleaned_text'].replace('nan', pd.NA)
df = df.dropna(subset=['cleaned_text'])

# Save cleaned dataset
df.to_csv(CLEANED_FILE, index=False)
print("Dataset cleaned and saved as 'cleaned_emails.csv'")
print(f"Processed {len(df)} emails")