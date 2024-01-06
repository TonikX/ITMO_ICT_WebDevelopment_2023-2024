const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors({
  origin: 'http://localhost:5173', 
}));
app.use(express.json());

// Предполагаем, что у вас есть массив воинов для хранения данных
let warriors = [];

// Маршрут для получения списка воинов
app.get('/api/warriors', (req, res) => {
  res.json(warriors);
});

// Маршрут для создания нового воина
app.post('/api/warriors/create', (req, res) => {
  const newWarrior = req.body;
  warriors.push(newWarrior);
  res.status(201).send('Warrior created successfully');
});

const PORT = 3000; // Установите желаемый порт
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
