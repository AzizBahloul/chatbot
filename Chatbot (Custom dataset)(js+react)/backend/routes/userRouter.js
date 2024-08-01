const router = require('express').Router();
const { getAllUsers, addUser, getUserById, deleteUser, updateUser} = require('../controllers/userController');
const { adminAuth, userAuth } = require('../middleware/auth');


// Get all users
router.route('/').get(getAllUsers);

// Add a user
router.route('/add').post(adminAuth, addUser);

//find a user by id
router.route('/:id').get(getUserById);

//delete a user
router.route('/delete/:id').delete(adminAuth, deleteUser);
 
//update a user
router.route('/update/:id').put(updateUser);

//update the role of the user to admin
router.route('/updateRole/').put(adminAuth, updateUser);

module.exports = router;