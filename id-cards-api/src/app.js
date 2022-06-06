const express = require('express');
const cors = require('cors');
const isAuthenticated = require('./middlewares/auth');
const idCards = require('./routes/idcards');

const app = express();
const port = process.env.PORT || 8080;

app.use(cors({ origin: '*', credentials: true }));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.get('/', (req, res) => {
  res.send('Hello from ID Cards API, C22-KY04.');
});

app.use('/id_cards', isAuthenticated, idCards);

app.listen(port, () => {
  console.log(`App is running on port ${port}`);
});
