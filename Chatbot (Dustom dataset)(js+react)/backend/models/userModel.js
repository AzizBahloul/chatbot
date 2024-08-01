const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const userSchema = new Schema(
    {
        fullname: {
            type: String,
            required: true
        },
        username: {
            type: String,
            unique: true,
            required: true
        },
        email: {
            type: String,
            unique: true,
            required: true
        },
        password: {
            type: String,
            minlength: 8,
            required: true
        },
        role: {
            type: String,
            default: 'Member',
          
        },
        resetCode: {
            type: String,
            nullable: true
        },
        avatar: {
            public_id: {
                type: String,
                required: true
            },
            url: {
                type: String,
                required: true
            }
        },
        createdAt: {
            type: Date,
            default: Date.now
        }

    },{
        timestamps: true
    }   
);

const User = mongoose.model('User', userSchema);

module.exports = User;

