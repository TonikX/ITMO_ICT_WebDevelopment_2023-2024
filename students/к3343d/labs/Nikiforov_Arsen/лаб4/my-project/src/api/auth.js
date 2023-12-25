// src/api/auth.js

import axios from 'axios';

const API_URL = 'http://localhost:8000/hotel_api/'; 

export function registerUser(userData) {
  return axios.post(`${API_URL}register/`, userData);
}
