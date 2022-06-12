const express = require('express');
const {
  createIdCard, getIdCards, getIdCard,
} = require('../controllers/idcards');

const router = express.Router();

router.post('/', createIdCard);

router.get('/', getIdCards);

router.get('/:uid', getIdCard);

module.exports = router;
