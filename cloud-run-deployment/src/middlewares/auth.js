const admin = require('../config/firebase');

const getIdToken = (req, res, next) => {
  if (req.headers.authorization) {
    req.idToken = req.headers.authorization;
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
    } catch (e) {
      return res.status(401).json({
        status: 'Unauthorized',
        message: 'You are not authorized to make this request',
      });
    }
  });
};

module.exports = isAuthenticated;
