require('dotenv').config();
const login = require('./auth');

const email = process.env.EMAIL;
const password = process.env.PASSWORD;

login(email, password);
