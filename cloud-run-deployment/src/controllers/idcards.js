const Firestore = require('@google-cloud/firestore');

const db = new Firestore();

const error_responses = require('error_responses');

const createIdCard = async (req, res) => {
  try {
    const { uid } = req.body;

    const data = {
      uid: req.body.uid,
      province: req.body.province,
      district: req.body.district,
      id_number: req.body.id_number,
      name: req.body.name,
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
      attachment: req.body.attachment,
    };

    await db.collection('id_cards').doc(uid).set(data);

    res.status(201).json({
      status: 'Created',
      message: 'The item/record was created successfully.',
    });
  } catch (error) {
    res.status(400).json(error_responses(400));
  }
};

const getIdCards = async (req, res) => {
  try {
    const { name } = req.query;

    const idCardsRef = db.collection('id_cards');
    const snapshot = await idCardsRef.get();

    let docs = snapshot.docs.map((doc) => doc.data());

    if (name) {
      docs = docs
        .filter((doc) => (
          doc.name.toLowerCase().includes(name.toLowerCase())
        ));
    }

    if (docs.length > 0) {
      res.status(200).json(docs);
    } else {
      res.status(404).json(error_responses(404));
    }
  } catch (error) {
    res.status(400).json(error_responses(400));
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
      res.status(404).json(error_responses(404));
    }
  } catch (error) {
    res.status(400).json(error_responses(400));
  }
};

const updateIdCard = async (req, res) => {
  try {
    const { uid } = req.params;

    const data = {
      uid: req.body.uid,
      province: req.body.province,
      district: req.body.district,
      id_number: req.body.id_number,
      name: req.body.name,
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
      attachment: req.body.attachment,
    };

    await db.collection('id_cards').doc(uid).update(data);

    res.status(200).json({
      status: 'OK',
      message: 'The item/record was updated successfully.',
    });
  } catch (error) {
    res.status(400).json(error_responses(400));
  }
};

const deleteIdCard = async (req, res) => {
  try {
    const { uid } = req.params;

    await db.collection('id_cards').doc(uid).delete();

    res.status(200).json({
      status: 'OK',
      message: 'The item/record was deleted successfully.',
    });
  } catch (error) {
    res.status(400).json(error_responses(400));
  }
};

module.exports = {
  createIdCard, getIdCards, getIdCard, updateIdCard, deleteIdCard,
};
