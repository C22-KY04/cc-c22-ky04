const Firestore = require('@google-cloud/firestore');

const db = new Firestore();

const createIdCard = async (req, res) => {
  try {
    const { uid } = req.body;

    const data = {
      uid: req.body.uid,
      province: req.body.province,
      district: req.body.district,
      id_number: req.body.id_number,
      full_name: req.body.full_name,
      place_date_of_birth: req.body.place_date_of_birth,
      gender: req.body.gender,
      blood_type: req.body.blood_type,
      address: req.body.address,
      neighborhood: req.body.neighborhood,
      village: req.body.village,
      subdistrict: req.body.subdistrict,
      religion: req.body.religion,
      marital_status: req.body.marital_status,
      occupation: req.body.occupation,
      nationality: req.body.nationality,
      expiry_date: req.body.expiry_date,
    };

    await db.collection('id_cards').doc(uid).set(data);

    res.status(201).json({
      status: 'Created',
      message: 'Successfully added ID Card',
    });
  } catch (error) {
    res.status(400).json({
      status: 'Bad Request',
      message: error.message,
    });
  }
};

const getIdCards = async (req, res) => {
  try {
    const idCardsRef = db.collection('id_cards');
    const snapshot = await idCardsRef.get();

    const docs = [];

    if (!snapshot.empty) {
      snapshot.forEach((doc) => docs.push(doc.data()));

      res.status(200).json(docs);
    } else {
      res.status(404).json({
        status: 'Not Found',
        message: 'ID card not found',
      });
    }
  } catch (error) {
    res.status(400).json({
      status: 'Bad Request',
      message: error.message,
    });
  }
};

const getIdCard = async (req, res) => {
  try {
    const { uid } = req.params;

    const idCardRef = db.collection('id_cards').doc(uid);
    const doc = await idCardRef.get();

    if (doc.exists) {
      res.status(200).json(doc.data());
    } else {
      res.status(404).json({
        status: 'Not Found',
        message: 'ID card not found',
      });
    }
  } catch (error) {
    res.status(400).json({
      status: 'Bad Request',
      message: error.message,
    });
  }
};

const updateIdCard = async (req, res) => {
  try {
    const { uid } = req.params;

    const data = {
      uid,
      province: req.body.province,
      district: req.body.district,
      id_number: req.body.id_number,
      full_name: req.body.full_name,
      place_date_of_birth: req.body.place_date_of_birth,
      gender: req.body.gender,
      blood_type: req.body.blood_type,
      address: req.body.address,
      neighborhood: req.body.neighborhood,
      village: req.body.village,
      subdistrict: req.body.subdistrict,
      religion: req.body.religion,
      marital_status: req.body.marital_status,
      occupation: req.body.occupation,
      nationality: req.body.nationality,
      expiry_date: req.body.expiry_date,
    };

    await db.collection('id_cards').doc(uid).update(data);

    res.status(200).json({
      status: 'OK',
      message: 'Successfully updated ID Card',
    });
  } catch (error) {
    res.status(400).json({
      status: 'Bad Request',
      message: error.message,
    });
  }
};

const deleteIdCard = async (req, res) => {
  try {
    const { uid } = req.params;

    await db.collection('id_cards').doc(uid).delete();

    res.status(200).json({
      status: 'OK',
      message: 'Successfully delete ID Card',
    });
  } catch (error) {
    res.status(400).json({
      status: 'Bad Request',
      message: error.message,
    });
  }
};

module.exports = {
  createIdCard, getIdCards, getIdCard, updateIdCard, deleteIdCard,
};
