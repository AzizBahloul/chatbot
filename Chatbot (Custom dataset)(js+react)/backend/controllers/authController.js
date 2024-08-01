const User = require('../models/userModel');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const dotenv = require('dotenv');
const Token = require('../models/tokenModel');
const sendEmail = require('../utils/sendEmail');
const cloudinary = require('cloudinary').v2; // Import cloudinary

dotenv.config();

const jwtSecretKey = process.env.JWT_SECRET_KEY;

// Signup function
const signup = async (req, res, next) => {
    const { fullname, username, email, password, avatar } = req.body;

    try {
        // Check if all fields are provided
        if (!fullname || !username || !email || !password) {
            return res.status(400).json({ message: 'Please fill in all fields' });
        }

        // Check password length
        if (password.length < 8) {
            return res.status(400).json({ message: 'Password should be at least 8 characters long' });
        }

        // Check if username already exists
        let existingUser = await User.findOne({ username });
        if (existingUser) {
            return res.status(400).json({ message: 'Username already exists' });
        }

        // Check if email already exists
        existingUser = await User.findOne({ email });
        if (existingUser) {
            return res.status(400).json({ message: 'You already have an account with this email' });
        }

        let avatarData = null;
        // Upload avatar to cloudinary
        if (avatar) {
            const result = await cloudinary.uploader.upload(avatar.url, {
                folder: 'avatars',
                width: 150,
                crop: "scale"
            });
            avatarData = {
                public_id: result.public_id,
                url: result.secure_url
            };
        }

        // Hash password
        const hashedPassword = await bcrypt.hash(password, 10);

        // Create new user
        const user = await User.create({
            fullname,
            username,
            email,
            password: hashedPassword,
            avatar: avatarData
        });

        // Create JWT token
        const maxAge = 3 * 60 * 60;
        const payload = { user: { id: user._id, username: user.username, role: user.role } };
        const token = jwt.sign(payload, jwtSecretKey, { expiresIn: maxAge });

        // Set JWT token in cookie
        res.cookie("jwt", token, {
            httpOnly: true,
            secure: true,
            maxAge: maxAge * 1000,
        });

        // Save token to database
        await Token.create({ userId: user._id, token: token });

        res.status(201).json({
            message: 'User successfully created!',
            user,
        });
    } catch (err) {
        res.status(400).json({
            message: "User not created!",
            error: err.message,
        });
    }
};

// Update profile function
const updateProfile = async (req, res, next) => {
    const { fullname, username, email, password, avatar } = req.body;
    const userId = req.user.id;

    try {
        // Find user by ID
        let user = await User.findById(userId);

        if (!user) {
            return res.status(400).json({ message: 'User not found' });
        }

        // Check if username is provided and not the same as the current username
        if (username && username !== user.username) {
            let existingUser = await User.findOne({ username });
            if (existingUser) {
                return res.status(400).json({ message: 'Username already exists' });
            }
            user.username = username;
        }

        // Check if email is provided and not the same as the current email
        if (email && email !== user.email) {
            let existingUser = await User.findOne({ email });
            if (existingUser) {
                return res.status(400).json({ message: 'Email already in use' });
            }
            user.email = email;
        }

        // Check if password is provided
        if (password) {
            // Check password length
            if (password.length < 8) {
                return res.status(400).json({ message: 'Password should be at least 8 characters long' });
            }
            // Hash new password
            const hashedPassword = await bcrypt.hash(password, 10);
            user.password = hashedPassword;
        }

        // Check if avatar is provided
        if (avatar) {
            // Upload new avatar to cloudinary
            const result = await cloudinary.uploader.upload(avatar.url, {
                folder: 'avatars',
                width: 150,
                crop: "scale"
            });
            const avatarData = {
                public_id: result.public_id,
                url: result.secure_url
            };
            user.avatar = avatarData;
        }

        // Save updated user profile
        await user.save();

        res.status(200).json({
            message: 'Profile updated successfully',
            user,
        });
    } catch (err) {
        res.status(400).json({
            message: "An error occurred!",
            error: err.message,
        });
    }
};

// Login function
const login = async (req, res, next) => {
    const { email, username, password } = req.body;

    if (!email && !username) {
        return res.status(400).json({ message: 'Please provide email or username' });
    }
    if (!password) {
        return res.status(400).json({ message: 'Please provide password' });
    }

    try {
        const user = await User.findOne(
            email ? { email } : { username },
        );

        if (!user) {
            return res.status(401).json({
                message: "Invalid credentials",
                error: "User not found",
            });
        } else {
            bcrypt.compare(password, user.password).then((result) => {
                if (result) {
                    const maxAge = 3 * 60 * 60;
                    const payload = { user: { id: user._id, username: user.username, role: user.role } };
                    const token = jwt.sign(payload, jwtSecretKey, { expiresIn: maxAge });
                    res.cookie("jwt", token, {
                        httpOnly: true,
                        secure: true,
                        maxAge: maxAge * 1000,
                    });
                    const newToken = Token.create({ userId: user._id, token: token });

                    res.status(200).json({
                        message: "Login successful",
                        user: { id: user._id },
                    });
                } else {
                    res.status(400).json({
                        message: "Invalid credentials",
                        error: "Password is incorrect",
                    });
                }
            });
        }
    } catch (err) {
        res.status(400).json({
            message: "An error occurred!",
            error: err.message,
        });
    }
};

// Forget password function
const forgetPassword = async (req, res, next) => {
    const { email } = req.body;

    if (!email) {
        return res.status(400).json({ message: 'Please provide email' });
    }

    try {
        const user = await User.findOne({ email });

        if (!user) {
            return res.status(400).json({ message: 'User not found' });
        }

        const resetCode = Math.floor(100000 + Math.random() * 900000);
        await user.updateOne({
            resetCode: resetCode,
        });

        const message = `
            <h1>You have requested a password reset</h1>
            <p>Your reset code is ${resetCode}</p>
            <p>If you did not request a password reset, please ignore this email and we recommend you to change your password as a precaution measure!</p>
            `;

        try {
            await sendEmail(user.email, 'Password Reset Request', message);

            res.status(200).json({ message: 'Email sent' });
        } catch (err) {
            await user.save();
            return res.status(500).json({ message: 'Email could not be sent' });
        }

    } catch (err) {
        res.status(400).json({
            message: "An error occurred!",
            error: err.message,
        });
    }
};

// Reset password function
const resetPassword = async (req, res, next) => {
    const { resetCode, newPassword } = req.body;

    if (!resetCode || !newPassword) {
        return res.status(400).json({ message: 'Please provide reset code and new password' });
    }

    try {
        const user = await User.findOne({ resetCode });

        if (!user) {
            return res.status(400).json({ message: 'Invalid reset code' });
        }

        bcrypt.hash(newPassword, 10)
            .then(async (hash) => {
                user.password = hash;
                user.resetCode = '';
                await user.save();
                res.status(200).json({ message: 'Password reset successful' });
            })
            .catch((err) => {
                res.status(400).json({
                    message: 'Password not reset',
                    error: err.message,
                });
            });
    } catch (err) {
        res.status(400).json({
            message: 'An error occurred',
            error: err.message,
        });
    }
};

module.exports = {
    signup,
    updateProfile,
    login,
    forgetPassword,
    resetPassword,
};
