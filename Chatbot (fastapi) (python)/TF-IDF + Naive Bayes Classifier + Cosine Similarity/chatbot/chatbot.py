import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from spellchecker import SpellChecker
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class Chatbot:
    def __init__(self, model_path="data/model.pkl"):
        self.model_path = model_path
        self.vectorizer = None
        self.questions = []
        self.responses = []
        self.spell = SpellChecker()
        self.stopwords = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()
        self.load_model()

    def load_model(self):
        if os.path.exists(self.model_path):
            with open(self.model_path, "rb") as f:
                self.vectorizer, self.questions, self.responses = pickle.load(f)
        else:
            raise FileNotFoundError(f"Model file {self.model_path} not found. Please train the model first.")

    def preprocess(self, text):
        text = text.lower().strip()
        words = text.split()
        corrected_words = [self.spell.correction(word) or word for word in words]
        cleaned_words = [self.lemmatizer.lemmatize(word) for word in corrected_words if word not in self.stopwords]
        return ' '.join(cleaned_words)

    def predict(self, query):
        query = self.preprocess(query)
        X = self.vectorizer.transform([query])
        train_matrix = self.vectorizer.transform(self.questions)
        similarities = cosine_similarity(X, train_matrix).flatten()
        best_idx = similarities.argmax()
        if similarities[best_idx] < 0.5:
            return "I'm not sure I understand. Could you please clarify?"
        return self.responses[best_idx]
