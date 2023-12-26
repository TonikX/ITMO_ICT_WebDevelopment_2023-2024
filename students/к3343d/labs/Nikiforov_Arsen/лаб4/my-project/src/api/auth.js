// src/api/auth.js

import axios from 'axios';

const API_URL = 'http://localhost:8000/hotel_api/';

export function registerUser(userData) {
  return axios.post(`${API_URL}register/`, userData);
}

export function loginUser(userData) {
  return axios.post(`${API_URL}login/`, userData);
}


export function userProfile(userData) {
  return axios.post(`${API_URL}user-profile/`, userData);
}

export function logoutUser() {
  // Здесь должен быть код для выхода пользователя.

}
