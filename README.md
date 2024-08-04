

# **Chatbot Project Overview**

1. **[Chatbot (Manual Data Input) (Python + Streamlit)](#chatbot-manual-data-input-python--streamlit)**
2. **[Chatbot (Custom Dataset) (JS + React)](#chatbot-custom-dataset-js--react)**
3. **[EarlyLearnerAI (Python + Streamlit )](#earlylearnerai-python)**

---

# **Chatbot (Manual Data Input) (Python + Streamlit)**

**ChatGPT 5 Turbo Supercharger V12 5.4L Peugeot Partner**

## Running the ChatGPT_5_Turbo_Supercharge App

The password for the admin panel is: `admin`

### On Windows

- Double-click `Chatgpt_5_Turbo_Supercharge.bat` to start the Streamlit app.

### On macOS/Linux

- Open a terminal and run `./Chatgpt_5_Turbo_Supercharge.sh` to start the Streamlit app.

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

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/chatbot-project.git
   cd chatbot-project
   ```

2. **Create and Activate Virtual Environment:**

   ```bash
   python -m venv rasa-new-env
   source rasa-new-env/bin/activate  # On Windows use `rasa-new-env\Scripts\activate`
   ```

3. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database:** Run the `app.py` script once to create the necessary data file:

   ```bash
   python app.py
   ```

5. **Train the Model:** Run the `train.py` script to train and save the model:

   ```bash
   python train.py
   ```

## Usage

1. **Train the Chatbot:** Launch the training interface:

   ```bash
   streamlit run app.py
   ```

   Enter new questions and responses to update the chatbot's training data.

2. **Chat with the Chatbot:** Launch the chatbot interface:

   ```bash
   streamlit run chat.py
   ```

   Type your messages and receive responses from the chatbot.

## Contributing

Feel free to open issues or submit pull requests. Contributions to improve the chatbot and its features are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

# **Chatbot (Custom Dataset) (JS + React)**

## Overview

This project consists of a React frontend for interacting with a chatbot and an Express backend that handles the chat logic using Dialogflow. The frontend allows users to send messages and receive responses from the chatbot, while the backend processes these messages and communicates with Dialogflow to generate responses.

## Technologies Used

- Frontend: React, Bootstrap
- Backend: Node.js, Express
- Dialogflow: Google Dialogflow API
- Cloudinary: For media management (if applicable)

## Setup Instructions

### Frontend Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**

   ```bash
   npm install
   ```

3. **Start the Development Server:**

   ```bash
   npm start
   ```

   The frontend will be available at [http://localhost:3000](http://localhost:3000).

### Backend Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**

   ```bash
   npm install
   ```

3. **Configure Environment Variables:** Create a `.env` file in the root directory with the following content:

   ```plaintext
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
   ```

4. **Start the Server:**

   ```bash
   npm start
   ```

   The backend will be available at [http://localhost:5000](http://localhost:5000).

## Endpoints

- **POST /api/Chat**

  - Request Body:

    ```json
    {
      "message": "Your message here"
    }
    ```

  - Response:

    ```json
    {
      "message": "Response from chatbot"
    }
    ```

## Usage

1. Open the frontend application in your browser ([http://localhost:3000](http://localhost:3000)).
2. Type a message into the input field and press Enter or click the "Send" button.
3. The chatbot's response will be displayed below the input field.

## Troubleshooting

- **CORS Issues:** Ensure that the backend server is running and CORS is properly configured.

---

# **EarlyLearnerAI (Python)**

**EarlyLearnerAI** is an adaptive chatbot designed to mimic the curiosity and learning style of a 4-year-old child. It engages in conversation, asks for clarifications when needed, and dynamically updates its knowledge base based on user input.

## Features

- **Child-like Interaction:** Engages with users in a manner similar to a 4-year-old.
- **Adaptive Learning:** Learns new information from user interactions and updates its knowledge base accordingly.

## Requirements

- Python 3.x
- Streamlit
- pymongo
- python-dotenv
- joblib
- scikit-learn
- spacy

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/EarlyLearnerAI.git
   cd EarlyLearnerAI
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Set up your environment variables:** Create a `.env` file in the root directory with the following content:

   ```plaintext
   MONGO_DB_URL=your_mongodb_url
   DB_NAME=your_database_name
   COLLECTION_NAME=your_collection_name
   ```

## Running the Application

1. **Start the Streamlit app:**

   ```bash
   streamlit run streamlit_app.py
   ```

2. **Insert new data into the model:** Use the provided script to add new question-response pairs from a JSON file:

   ```bash
   python insert_data_from_json.py
   ```

## Contributing

1. **Fork the repository.**
2. **Create a new branch:**

   ```bash
   git checkout -b feature/your-feature
   ```

3. **Commit your changes:**

   ```bash
   git add .
   git commit -m "Add new feature"
   ```

4. **Push to the branch:**

   ```bash
   git push origin feature/your-feature
   ```

5. **Open a pull request.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
