import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

class Chatbot:
    def __init__(self, model_path="data/model.h5", tokenizer_path="data/tokenizer.pkl", label_mapping_path="data/label_mapping.pkl", max_len=50):
        self.model_path = model_path
        self.tokenizer_path = tokenizer_path
        self.label_mapping_path = label_mapping_path
        self.max_len = max_len
        self.load_model_and_resources()

    def load_model_and_resources(self):
        if os.path.exists(self.model_path) and os.path.exists(self.tokenizer_path) and os.path.exists(self.label_mapping_path):
            self.model = load_model(self.model_path)
            with open(self.tokenizer_path, "rb") as f:
                self.tokenizer = pickle.load(f)
            with open(self.label_mapping_path, "rb") as f:
                self.label_mapping = pickle.load(f)
        else:
            raise FileNotFoundError("Required model resources not found. Please train the model first.")

    def predict(self, query):
        sequence = self.tokenizer.texts_to_sequences([query])
        padded_seq = pad_sequences(sequence, maxlen=self.max_len, padding="post")
        preds = self.model.predict(padded_seq)
        label_idx = np.argmax(preds, axis=1)[0]
        return self.label_mapping.get(label_idx, "I'm not sure I understand.")
