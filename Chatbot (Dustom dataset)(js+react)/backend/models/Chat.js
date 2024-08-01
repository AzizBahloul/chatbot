const mongoose = require('mongoose');

const messageSchema = new mongoose.Schema({
  userMessage: {
    type: String,
    required: true,
  },
  botMessage: {
    type: String,
    required: true,
  },
});

module.exports = mongoose.model('Chat', messageSchema);
