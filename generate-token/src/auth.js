const { getAuth, signInWithEmailAndPassword } = require('firebase/auth');
const app = require('./config');

const auth = getAuth(app);

const getJwtToken = async () => {
  try {
    const idToken = await auth.currentUser.getIdToken(true);

    return `Bearer ${idToken}`;
  } catch (error) {
    return error.message;
  }
};

const login = async (email, password) => {
  try {
    const userCredentials = await signInWithEmailAndPassword(auth, email, password);
    const jwtToken = await getJwtToken();

    console.log(`Login success! You are logged in as ${userCredentials.user.email}\n`);
    console.log('JWT Token:\n');
    console.log(`${jwtToken}`);
  } catch (error) {
    console.log(error.message);
  }
};

module.exports = login;
