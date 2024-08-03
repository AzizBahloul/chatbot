import json
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
        try:
            data = list(self.collection.find({}))
            self.knowledge_base = pd.DataFrame(data)
            if not self.knowledge_base.empty:
                self.update_model()
        except Exception as e:
            print(f"Error loading knowledge: {e}")

    def update_model(self):
        if not self.knowledge_base.empty:
            X = self.vectorizer.fit_transform(self.knowledge_base["question"])
            self.model.fit(X)
            joblib.dump(self.vectorizer, 'model_vectorizer.pkl')
            joblib.dump(self.model, 'model_nearest_neighbors.pkl')

    def load_model(self):
        if os.path.exists('model_vectorizer.pkl') and os.path.exists('model_nearest_neighbors.pkl'):
            self.vectorizer = joblib.load('model_vectorizer.pkl')
            self.model = joblib.load('model_nearest_neighbors.pkl')

    def learn(self, question, response):
        try:
            new_entry = {"question": question, "response": response}
            self.collection.insert_one(new_entry)
            self.load_knowledge()
            self.update_model()
            print(f"Inserted question: {question}, response: {response}")
        except Exception as e:
            print(f"Error learning new data: {e}")

def insert_data_from_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        chatbot = ChildChatbot()
        for entry in data:
            question = entry.get("question")
            response = entry.get("response")
            if question and response:
                chatbot.learn(question, response)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = 'data.json'  # Path to your JSON file
    insert_data_from_json(file_path)
