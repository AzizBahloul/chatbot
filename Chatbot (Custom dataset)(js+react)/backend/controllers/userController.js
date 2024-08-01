let User = require('../models/userModel');


// get all users
const getAllUsers = (req, res) => {
    User.find()
        .then(users => res.json(users))
        .catch(error => res.status(400).json('Error: ' + error));
}


// add a user
const addUser = (req, res) => {
    const fullname = req.body.fullname;
    const username = req.body.username;
    const email = req.body.email;
    const password = req.body.password;
    const role = req.body.role;

    const newUser = new User({
        fullname,
        username,
        email,
        password,
        role
    });

    newUser.save()
        .then(() => res.json('User added!', newUser))
        .catch(error => res.status(400).json('Error: ' + error));
}

// find a user by id
const getUserById = (req, res) => {
    User.findById(req.params.id)
        .then(user => res.json(user))
        .catch(error => res.status(400).json('Error: ' + error));
}


// delete a user
const deleteUser = (req, res) => {
    User.findByIdAndDelete(req.params.id)
        .then(() => res.json('User deleted!'))
        .catch(error => res.status(400).json('Error: ' + error));
}

// update a user
const updateUser = async (req, res) => {
    User.findByIdAndUpdate(
        req.params.id,
        { $set: req.body },
        { new: true },
    )
        .then((user) => {
            if (!user) {
                return res.status(404).json({ message: 'User not found' });
            }
            res.json({ message: 'User updated!', user });
        })
}

// updating the roles of users 
const updateRole = async (req, res, next) => {
    const { role, id } = req.body;
    if (role && id) {
        if (role === 'admin') {
            await User.findById(id)
                .then((user) => {
                    if (user.role !== 'admin') {
                        user.role = role;
                        user.save()
                            .then(() => res.status(200).json({ message: 'Role updated successfully' }))
                            .catch(error => res.status(400).json('Error: ' + error));
                    } else {
                        res.status(400).json({ message: 'User is already an admin' });
                    }
                })
                .catch(error => res.status(400).json('Error: ' + error));
        }
    } else {
        res.status(400).json({ message: 'Please provide role and id' });
    }
}

module.exports = {
    getAllUsers,
    addUser,
    getUserById,
    deleteUser,
    updateUser,
    updateRole
}