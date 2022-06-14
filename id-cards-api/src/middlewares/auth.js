const admin = require('firebase-admin');

const serviceAccount = require('../../serviceAccountKey.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});

const isAuthenticated = async (req, res, next) => {
  const { authorization } = req.headers;

  if (!authorization) {
    return res.status(400).json({
      status: 'Bad Request',
      message: 'No token provided.',
    });
  }

  if (authorization.startsWith('Bearer ')) {
    const idToken = authorization.split('Bearer ')[1];

    try {
      await admin.auth().verifyIdToken(idToken);
    } catch {
      return res.status(401).json({
        status: 'Unauthorized',
        message: 'You do not have permissions to access the service.',
      });
    }
  }

  return next();
};

module.exports = isAuthenticated;
