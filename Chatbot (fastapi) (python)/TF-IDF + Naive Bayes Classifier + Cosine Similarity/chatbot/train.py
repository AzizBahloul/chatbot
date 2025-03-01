import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_model(data_path="data/dataset.csv", model_path="data/model.pkl"):
    try:
        data = pd.read_csv(data_path, on_bad_lines='skip')
        if 'question' not in data.columns or 'response' not in data.columns:
            raise ValueError("Dataset must contain 'question' and 'response' columns.")

        questions = data["question"]
        responses = data["response"]

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(questions)

        model = MultinomialNB()
        model.fit(X, responses)

        with open(model_path, "wb") as f:
            pickle.dump((vectorizer, questions.tolist(), responses.tolist()), f)

        print(f"Model trained successfully and saved to {model_path}")

    except FileNotFoundError:
        print(f"Error: Dataset not found at {data_path}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    train_model()
