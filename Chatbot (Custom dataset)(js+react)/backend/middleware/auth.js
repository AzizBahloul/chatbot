const jwt = require('jsonwebtoken');
const dotenv = require('dotenv');

dotenv.config();

const jwtSecretKey = process.env.JWT_SECRET_KEY;

const adminAuth = (req, res, next) => {
    const token = req.header('Authorization')?.replace('Bearer ', '');
    if (token) {
        let decodedToken = jwt.verify(token, jwtSecretKey)
        if (!decodedToken) {
                console.log(err.message);
                res.status(401).json({ message: 'Unauthorized' });
            } else {
                if (decodedToken.user.role !== 'admin') {
                    res.status(401).json({ message: 'Unauthorized, you are not an admin' });
                } else {
                    next();
                }
            }
        } else {
        res.status(401).json({ message: 'Unauthorized, token not available' });
    }
}

const userAuth = (req, res, next) => {
    const token = req.header('Authorization')?.replace('Bearer ', '');
    if (token) {
        jwt.verify(token, jwtSecretKey, (err, decodedToken) =>{
            if (err) {
                console.log(err.message);
                res.status(401).json({ message: 'Unauthorized' });
            } else {
                if (decodedToken.role !== 'member') {
                    res.status(401).json({ message: 'Unauthorized' });
                } else {
                    next();
                }
            }
        })
    } else {
        res.status(401).json({ message: 'Unauthorized, token not available' });
    }
}

module.exports = { adminAuth, userAuth };