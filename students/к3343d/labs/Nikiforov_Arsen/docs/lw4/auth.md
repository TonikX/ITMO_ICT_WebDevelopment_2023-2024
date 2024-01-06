
## auth.js

`auth.js` - это модуль, отвечающий за аутентификацию и авторизацию пользователей в приложении.

#### Структура кода
```javascript
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
```

#### Методы

1. **login**
   - **Описание**: Аутентификация пользователя.
   - **Параметры**: `user` - объект пользователя с полями `username` и `password`.
   - **Использование**: `authService.login(user)`

