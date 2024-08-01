const express = require('express');
const cors = require('cors');
const dbConnect = require('./config/dbConnect');
const dotenv = require('dotenv');
const cookieParser = require('cookie-parser');
const cloudinary = require('cloudinary').v2;
const bodyParser = require('body-parser');
const { SessionsClient } = require('dialogflow');  // Correct import for Dialogflow

dotenv.config();

const port = process.env.PORT;
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));  // Use bodyParser for URL encoding
app.use(bodyParser.json());  // Use bodyParser for JSON parsing
app.use(express.json());
app.use(cookieParser());

// Cloudinary configuration
cloudinary.config({
    cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
    api_key: process.env.CLOUDINARY_API_KEY,
    api_secret: process.env.CLOUDINARY_API_SECRET
});

const privateKey = process.env.DIALOGFLOW_PRIVATE_KEY.replace(/\\n/g, '\n');  // Correctly handle newlines
const clientEmail = process.env.DIALOGFLOW_CLIENT_EMAIL;
const sessionClient = new SessionsClient({
    credentials: {
        private_key: privateKey,
        client_email: clientEmail
    }
});

const sessionPath = sessionClient.sessionPath('chatbotmta3siaziz', '123456');  // Update the sessionPath

// Connect to database
dbConnect();

// Dialogflow message endpoint
app.post('/api/Chat', async (req, res) => {
    const { message } = req.body;

    const request = {
        session: sessionPath,
        queryInput: {
            text: {
                text: message,
                languageCode: 'en-US',
            },
        },
    };

    try {
        const responses = await sessionClient.detectIntent(request);
        const result = responses[0].queryResult;
        res.json({ message: result.fulfillmentText });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

const indexRouter = require('./routes/index');
app.use('/', indexRouter);

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

module.exports = app;
