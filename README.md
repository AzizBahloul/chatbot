# FOR Chatbot (Manual data input) (python + streamlit)
chatgpt 5 turbo supercharger v12 5.4L Peugeot  partner 

# Running the Chatgpt_5_Turbo_Supercharge App
the password for the admin panel is : admin

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


# FOR Chatbot (Custom dataset)(js+react)



# Chatbot Project

## Overview

This project consists of a React frontend for interacting with a chatbot and an Express backend that handles the chat logic using Dialogflow. The frontend allows users to send messages and receive responses from the chatbot, while the backend processes these messages and communicates with Dialogflow to generate responses.

## Technologies Used

- Frontend: React, Bootstrap
- Backend: Node.js, Express
- Dialogflow: Google Dialogflow API
- Cloudinary: For media management (if applicable)

## Setup Instructions

### Frontend Setup

1. Clone the Repository:

   git clone <repository-url>
   cd <repository-directory>

2. Install Dependencies:

   npm install

3. Start the Development Server:

   npm start

   The frontend will be available at http://localhost:3000.

### Backend Setup

1. Clone the Repository:

   git clone <repository-url>
   cd <repository-directory>

2. Install Dependencies:

   npm install

3. Configure Environment Variables:

   Create a .env file in the root directory with the following content:

   PORT=5000
   DB_URL=<your-mongodb-url>
   DB_NAME=<your-database-name>
   EMAIL=<your-email>
   PASSWORD=<your-password>
   CLOUDINARY_CLOUD_NAME=<your-cloud-name>
   CLOUDINARY_API_KEY=<your-api-key>
   CLOUDINARY_API_SECRET=<your-api-secret>
   DIALOGFLOW_PRIVATE_KEY=<your-private-key>
   DIALOGFLOW_CLIENT_EMAIL=<your-client-email>

4. Start the Server:

   npm start

   The backend will be available at http://localhost:5000.

## Endpoints

- POST /api/Chat

  - Request Body:

    {
      "message": "Your message here"
    }

  - Response:

    {
      "message": "Response from chatbot"
    }

## Usage

1. Open the frontend application in your browser (http://localhost:3000).
2. Type a message into the input field and press Enter or click the "Send" button.
3. The chatbot's response will be displayed below the input field.

## Troubleshooting

- CORS Issues:
  Ensure that the backend server is running and CORS is properly configured.

