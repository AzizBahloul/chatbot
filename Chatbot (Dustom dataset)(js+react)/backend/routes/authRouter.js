const router = require('express').Router();
const {signup, login, forgetPassword, resetPassword}  = require('../controllers/authController');

router.route("/signup").post(signup);
router.route("/login").post(login);
router.route("/forgetpassword").post(forgetPassword);
router.route("/resetpassword").post(resetPassword);

module.exports = router;
