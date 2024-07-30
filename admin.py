import streamlit as st
import pandas as pd
import os
import csv
import pickle
from train import train_model, load_model

# Path to the data file
DATA_PATH = 'data/chatbot_data.csv'
MODEL_PATH = 'models/chatbot_model.pkl'

# Initialize the database if it does not exist
def initialize_database():
    if not os.path.exists(DATA_PATH):
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
        df = pd.DataFrame(columns=['question', 'responses'])
        df.to_csv(DATA_PATH, index=False, quoting=csv.QUOTE_ALL)

# Add questions and responses to the database
def add_to_database(questions, responses):
    questions_list = [q.strip() for q in questions.split('\n') if q.strip()]
    if questions_list:
        df_new = pd.DataFrame({'question': questions_list, 'responses': [responses] * len(questions_list)})
        
        if os.path.exists(DATA_PATH) and os.path.getsize(DATA_PATH) > 0:
            df_existing = pd.read_csv(DATA_PATH)
            existing_questions = df_existing['question'].tolist()
            new_questions = [q for q in questions_list if q not in existing_questions]
            
            if len(new_questions) < len(questions_list):
                st.warning('Some questions are duplicates and will not be added.')
            
            df_new = pd.DataFrame({'question': new_questions, 'responses': [responses] * len(new_questions)})
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            df_combined = df_new
        
        df_combined.to_csv(DATA_PATH, index=False, quoting=csv.QUOTE_ALL)
        
        # Automatically train the model after updating the dataset
        train_model()
        st.success('Questions and response added and model trained!')

# Inject custom CSS for titles
st.markdown("""
    <style>
    .title {
        font-size: 2.5em;
        font-weight: bold;
        color: #1E90FF;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 30px;
    }
    .subtitle {
        font-size: 1.5em;
        font-weight: 600;
        color: #1E90FF;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit app interface
st.markdown('<div class="title">Chatbot Training Admin</div>', unsafe_allow_html=True)

# Authentication
with st.container():
    password = st.text_input('Password:', type='password', key='password', placeholder='Enter password', help='Password required to access the app')
    if password == 'admin':
        st.markdown('<div class="subtitle">Admin Panel</div>', unsafe_allow_html=True)
        
        # Initialize the database
        initialize_database()

        # Use a form to handle submission with Enter key
        with st.form(key='input_form'):
            questions = st.text_area('Enter questions (one per line):')
            responses = st.text_area('Enter the response for these questions:')
            submit_button = st.form_submit_button(label='Add')

            if submit_button:
                if questions and responses:
                    add_to_database(questions, responses)
                else:
                    st.error('Please fill in both fields.')
    elif password:
        st.error('Invalid password')
