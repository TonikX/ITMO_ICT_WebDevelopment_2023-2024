

import express from 'express';
import cors from 'cors';


const app = express();
app.use(cors());

const port = 3000;

app.use(express.json());

const warriors = [
  { name: 'Aragorn', race: 'Human' },
  { name: 'Legolas', race: 'Elf' }
];

app.get('/api/warriors', (req, res) => {
  res.json(warriors);
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
