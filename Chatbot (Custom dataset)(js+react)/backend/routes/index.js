const router = require('express').Router();
const authRouter = require('./authRouter');
const userRouter = require('./userRouter');
const dialogflow = require('./dialogflow');

router.use('/auth', authRouter);
router.use('/users', userRouter);
router.use('/dialogflow', dialogflow);

module.exports = router;
