const mongoose = require('mongoose');
const dotenv = require('dotenv');


dotenv.config();

const dbConnect = async () => {
  try {
    await mongoose.connect(process.env.DB_URL, {
      dbName: process.env.DB_NAME,
    });
    console.log('MongoDB connected');
  } catch (error) {
    console.error('MongoDB connection failed', error);
    process.exit(1);
  }
}

module.exports = dbConnect;