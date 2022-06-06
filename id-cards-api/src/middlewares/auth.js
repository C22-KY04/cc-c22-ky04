const admin = require('../config/firebase');

const getIdToken = (req, res, next) => {
  const authHeader = req.headers.authorization;

  if (authHeader.startsWith('Bearer ')) {
    req.idToken = authHeader.split('Bearer ').pop();
  } else {
    req.idToken = null;
  }

  next();
};

const isAuthenticated = (req, res, next) => {
  getIdToken(req, res, async () => {
    try {
      const { idToken } = req;

      await admin
        .auth()
        .verifyIdToken(idToken);

      return next();
    } catch (error) {
      return res.status(401).json({
        status: 'Unauthorized',
        message: 'You do not have permissions to access the service.',
      });
    }
  });
};

module.exports = isAuthenticated;