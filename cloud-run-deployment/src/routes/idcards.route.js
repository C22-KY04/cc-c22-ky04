const express = require('express');
const {
  createIdCard, getIdCards, getIdCard, updateIdCard, deleteIdCard,
} = require('../controllers/idcards.controller');

const router = express.Router();

router.post('/', createIdCard);

router.get('/', getIdCards);

router.get('/:uid', getIdCard);

router.put('/:uid', updateIdCard);

router.delete('/:uid', deleteIdCard);

module.exports = router;
