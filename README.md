# chatbot
chatgpt 5 turbo supercharger v12 5.4L Peugeot  partner 

## Running the Chatgpt_5_Turbo_Supercharge App

### On Windows

- Double-click `Chatgpt_5_Turbo_Supercharge.bat` to start the Streamlit app.

### On macOS/Linux

- Open a terminal and run `./Chatgpt_5_Turbo_Supercharge.sh` to start the Streamlit app.


# Chatbot Project

## Overview
This project is a chatbot application built using Streamlit for the user interface and a Naive Bayes classifier for handling user interactions. The chatbot can respond to a range of predefined questions and is designed to be easily extendable with new questions and responses.

## Features
- **Chatbot Interface:** A Streamlit app for interacting with the chatbot.
- **Training Interface:** A separate Streamlit app for adding new questions and responses to the chatbot's training data.
- **Text Correction:** Spelling correction for user inputs to improve response accuracy.

## Project Structure
The project contains the following key files:
- `app.py`: Streamlit app for training the chatbot with new questions and responses.
- `chat.py`: Streamlit app for interacting with the chatbot.
- `train.py`: Script for training the chatbot model and predicting responses.
- `data/chatbot_data.csv`: CSV file storing the training data for the chatbot.
- `models/chatbot_model.pkl`: Pickled file storing the trained model.

## Installation
1. **Clone the Repository:** `git clone https://github.com/your-username/chatbot-project.git` and `cd chatbot-project`.
2. **Create and Activate Virtual Environment:** `python -m venv rasa-new-env` and `source rasa-new-env/bin/activate` (On Windows use `rasa-new-env\Scripts\activate`).
3. **Install Required Packages:** `pip install -r requirements.txt`.
4. **Initialize the Database:** Run the `app.py` script once to create the necessary data file: `python app.py`.
5. **Train the Model:** Run the `train.py` script to train and save the model: `python train.py`.

## Usage
1. **Train the Chatbot:** Launch the training interface: `streamlit run app.py`. Enter new questions and responses to update the chatbot's training data.
2. **Chat with the Chatbot:** Launch the chatbot interface: `streamlit run chat.py`. Type your messages and receive responses from the chatbot.

## Contributing
Feel free to open issues or submit pull requests. Contributions to improve the chatbot and its features are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please reach out to [your-email@example.com](mailto:your-email@example.com).
