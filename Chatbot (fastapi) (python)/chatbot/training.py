import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_model(csv_file, model_file):
    # Load the dataset
    data = pd.read_csv(csv_file)
    
    # Extract questions and responses
    questions = data['question']
    responses = data['response']
    
    # Vectorize the questions
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(questions)
    
    # Train a model
    model = MultinomialNB()
    model.fit(X, responses)
    
    # Save the model and vectorizer
    with open(model_file, 'wb') as f:
        pickle.dump((vectorizer, model), f)
    
    print("Model training completed and saved to", model_file)

if __name__ == "__main__":
    train_model('dataset.csv', 'model.pkl')
