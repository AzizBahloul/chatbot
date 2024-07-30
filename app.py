import streamlit as st
import pandas as pd
import os
import csv

# Path to the data file
DATA_PATH = 'data/chatbot_data.csv'

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

# Initialize the database
initialize_database()

# Streamlit app interface
st.title('Chatbot Training GUI')

questions = st.text_area('Enter questions (one per line):')
responses = st.text_area('Enter the response for these questions:')

if st.button('Add'):
    if questions and responses:
        add_to_database(questions, responses)
        st.success('Questions and response added!')
    else:
        st.error('Please fill in both fields.')
