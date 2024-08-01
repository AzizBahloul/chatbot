const nodemailer = require('nodemailer');
require('dotenv').config();

const transport = nodemailer.createTransport({
  service: 'Gmail',
  auth: {
    user: process.env.EMAIL,
    pass: process.env.PASSWORD,
  },
});

let mailOptions = {
    from : process.env.EMAIL,
    to : '',
    subject : '',
    html : '',
}

const sendEmail = (email, subject, text) => {
    mailOptions.to = email;
    mailOptions.subject = subject;
    mailOptions.html = text;

    transport.sendMail(mailOptions, (err, info) => {
        if (err) {
            console.log("Error sending email:", err);
        } else {
            console.log(`Email sent: ${info.response}`);
        }
    });
}

module.exports = sendEmail;
