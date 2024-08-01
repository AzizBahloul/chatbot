const router = require('express').Router();
const axios = require('axios');
const Message = require('../models/Chat');  // Importing the Mongoose model

const PROJECT_ID = 'chatbotmta3siaziz';

router.post('/query', async (req, res, next) => {
  try {
    const { userMessage } = req.body;
    const { accessToken } = req.oauth2;

    const dialogflowResponse = await axios.post(
      `https://dialogflow.googleapis.com/v2/projects/${PROJECT_ID}/agent/sessions/test-session:detectIntent`,
      {
        queryInput: {
          text: {
            text: userMessage,
            languageCode: 'en-US',
          },
        },
      },
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        },
      }
    );

    console.log('Dialogflow Response:', dialogflowResponse.data);

    const botMessage = dialogflowResponse.data.queryResult.fulfillmentText;

    // Save the messages to MongoDB
    const message = new Message({
      userMessage,
      botMessage,
    });

    await message.save();

    res.json({ userMessage, botMessage });
  } catch (error) {
    console.error('Error:', error);

    if (error.response) {
      console.error('Error Response:', error.response.data);
    }

    next(error);  // Pass the error to the middleware
  }
});

// Route to fetch conversation history
router.get('/Chat', async (req, res, next) => {
  try {
    const messages = await Message.find();
    res.json(messages);
  } catch (error) {
    console.error('Error fetching messages:', error);
    next(error);  // Pass the error to the middleware
  }
});

module.exports = router;
