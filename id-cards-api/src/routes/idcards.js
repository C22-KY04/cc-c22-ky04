const express = require('express');
const {
  createIdCard, getIdCards,
} = require('../controllers/idcards');

const router = express.Router();

router.post('/', createIdCard);

router.get('/', getIdCards);

module.exports = router;
