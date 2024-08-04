import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import spacy
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import joblib

# Load environment variables from .env file
load_dotenv()

class ChildChatbot:
    def __init__(self):
        db_url = os.getenv("MONGO_DB_URL")
        db_name = os.getenv("DB_NAME")
        collection_name = os.getenv("COLLECTION_NAME")

        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.vectorizer = TfidfVectorizer()
        self.model = NearestNeighbors(n_neighbors=1, algorithm='auto')
        self.nlp = spacy.load("en_core_web_sm")
        self.load_knowledge()

    def load_knowledge(self):
        data = list(self.collection.find({}))
        self.knowledge_base = pd.DataFrame(data)
        if not self.knowledge_base.empty:
            self.update_model()

    def update_model(self):
        if not self.knowledge_base.empty:
            X = self.vectorizer.fit_transform(self.knowledge_base["question"])
            self.model.fit(X)
            # Save the model and vectorizer
            joblib.dump(self.vectorizer, 'model_vectorizer.pkl')
            joblib.dump(self.model, 'model_nearest_neighbors.pkl')

    def load_model(self):
        # Load the model and vectorizer
        if os.path.exists('model_vectorizer.pkl') and os.path.exists('model_nearest_neighbors.pkl'):
            self.vectorizer = joblib.load('model_vectorizer.pkl')
            self.model = joblib.load('model_nearest_neighbors.pkl')

    def ask(self, question):
        if self.knowledge_base.empty:
            return None
        X = self.vectorizer.transform([question])
        distances, indices = self.model.kneighbors(X)
        if distances[0][0] < 0.5:  # threshold for considering a match
            return self.knowledge_base.iloc[indices[0][0]]["response"]
        return None

    def learn(self, question, response):
        new_entry = {"question": question, "response": response}
        self.collection.insert_one(new_entry)
        self.load_knowledge()  # Reload the updated knowledge base
        self.update_model()  # Update and save the model

