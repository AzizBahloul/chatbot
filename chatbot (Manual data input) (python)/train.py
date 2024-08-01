import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from textblob import TextBlob
import os

# Paths
DATA_PATH = 'data/chatbot_data.csv'
MODEL_PATH = 'models/chatbot_model.pkl'

def load_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Data file not found: {DATA_PATH}")
    return pd.read_csv(DATA_PATH)

def train_model():
    try:
        data = load_data()
        print(f"Data loaded. Shape: {data.shape}")

        vectorizer = TfidfVectorizer()  # Using TfidfVectorizer instead of CountVectorizer
        X = vectorizer.fit_transform(data['question'])
        y = data['responses']
        
        print(f"Feature matrix shape: {X.shape}")
        print(f"Labels shape: {y.shape}")
        
        model = MultinomialNB()
        model.fit(X, y)
        
        with open(MODEL_PATH, 'wb') as f:
            pickle.dump((vectorizer, model), f)
        
        print("Model trained and saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
    with open(MODEL_PATH, 'rb') as f:
        vectorizer, model = pickle.load(f)
    return vectorizer, model

def correct_spelling(text):
    return str(TextBlob(text).correct())

def predict_response(user_input, model):
    vectorizer, classifier = model
    corrected_input = correct_spelling(user_input)
    user_input_vec = vectorizer.transform([corrected_input])
    prediction = classifier.predict(user_input_vec)
    print(f"User input: {user_input}")
    print(f"Corrected input: {corrected_input}")
    print(f"Prediction: {prediction[0]}")
    return prediction[0]

if __name__ == '__main__':
    if not os.path.exists(MODEL_PATH):
        train_model()
    else:
        print("Model already exists. To retrain, delete the existing model file.")
