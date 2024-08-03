import streamlit as st
from chatbot import ChildChatbot
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the chatbot
db_url = os.getenv("MONGO_DB_URL")
db_name = os.getenv("DB_NAME")
collection_name = os.getenv("COLLECTION_NAME")
chatbot = ChildChatbot()

st.title("Child-like Chatbot")

# Create session state to keep track of conversation
if 'conversation' not in st.session_state:
    st.session_state.conversation = []
if 'user_input' not in st.session_state:
    st.session_state.user_input = ''
if 'new_response' not in st.session_state:
    st.session_state.new_response = ''
if 'response_pending' not in st.session_state:
    st.session_state.response_pending = False

def handle_input():
    user_question = st.session_state.user_input.strip()
    
    if user_question:
        st.session_state.response_pending = True
        response = chatbot.ask(user_question)
        if response:
            st.session_state.conversation.append(f"You: {user_question}")
            st.session_state.conversation.append(f"Chatbot: {response}")
            st.session_state.response_pending = False
        else:
            st.session_state.conversation.append(f"You: {user_question}")
            st.session_state.conversation.append("Chatbot: I don't know. Can you teach me?")
            st.session_state.new_response = ''  # Clear new response field for next input
        st.session_state.user_input = ''  # Clear input field after response is processed

def handle_new_response():
    new_response = st.session_state.new_response.strip()
    
    if new_response:
        last_question = st.session_state.conversation[-2].replace("You: ", "")
        chatbot.learn(last_question, new_response)
        st.session_state.conversation.append(f"You taught: {new_response}")
        st.session_state.conversation.append("Chatbot: Thank you! I've learned something new.")
        st.session_state.new_response = ''  # Clear new response field
        st.session_state.response_pending = False

# Display conversation in a chat-like format
if 'conversation' in st.session_state and st.session_state.conversation:
    chat_display = "\n".join(st.session_state.conversation)
    st.text_area("Chat", value=chat_display, height=300, disabled=True)

# User input and response handling
if not st.session_state.response_pending:
    st.text_input("Type your message:", key="user_input", on_change=handle_input)

if st.session_state.conversation and st.session_state.conversation[-1] == "Chatbot: I don't know. Can you teach me?":
    st.text_input("Provide the answer:", key="new_response", on_change=handle_new_response)
