import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.callbacks import EarlyStopping

def train_model(data_path="data/dataset.csv", model_path="data/model.h5", tokenizer_path="data/tokenizer.pkl", label_mapping_path="data/label_mapping.pkl"):
    data = pd.read_csv(data_path, on_bad_lines='skip')
    if 'question' not in data.columns or 'response' not in data.columns:
        raise ValueError("Dataset must contain 'question' and 'response' columns.")
    questions = data["question"].astype(str).tolist()
    responses = data["response"].astype(str).tolist()
    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(responses)
    num_classes = len(label_encoder.classes_)
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(questions)
    sequences = tokenizer.texts_to_sequences(questions)
    max_len = max(len(seq) for seq in sequences)
    padded_sequences = pad_sequences(sequences, maxlen=max_len, padding="post")
    categorical_labels = to_categorical(labels, num_classes=num_classes)
    model = Sequential()
    model.add(Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=128, input_length=max_len))
    model.add(LSTM(64, recurrent_activation='sigmoid', unroll=True))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    early_stop = EarlyStopping(monitor="loss", patience=3)
    model.fit(padded_sequences, categorical_labels, epochs=20, batch_size=32, callbacks=[early_stop])
    model.save(model_path)
    with open(tokenizer_path, "wb") as f:
        pickle.dump(tokenizer, f)
    label_mapping = {i: label for i, label in enumerate(label_encoder.classes_)}
    with open(label_mapping_path, "wb") as f:
        pickle.dump(label_mapping, f)
    print("Model, tokenizer, and label mapping saved.")

if __name__ == "__main__":
    train_model()
