import streamlit as st
import pandas as pd
import pickle
from train import load_model, predict_response

st.title('Chat with Chatbot')

# Load model once when the script runs
model = load_model()

def get_response(user_input):
    return predict_response(user_input, model)

# User input
user_message = st.text_input('You:', '')

if st.button('Send'):
    if user_message:
        response = get_response(user_message)
        st.write(f'Chatbot: {response}')
    else:
        st.error('Please enter a message.')
