import pickle
import re
from sklearn.feature_extraction.text import CountVectorizer
import os

class Chatbot:
    def __init__(self, model_file):
        # Ensure the file path is correct
        model_file_path = os.path.join(os.path.dirname(__file__), model_file)
        if not os.path.exists(model_file_path):
            raise FileNotFoundError(f"Model file {model_file_path} not found.")
        with open(model_file_path, 'rb') as f:
            self.vectorizer, self.model = pickle.load(f)
    
    def preprocess(self, text):
        # Simple text cleaning
        text = re.sub(r'\s+', ' ', text)
        text = text.lower()
        return text
    
    def predict(self, query):
        query = self.preprocess(query)
        X = self.vectorizer.transform([query])
        response = self.model.predict(X)[0]
        return response

chatbot = Chatbot('model.pkl')

def get_response(query):
    return chatbot.predict(query)
