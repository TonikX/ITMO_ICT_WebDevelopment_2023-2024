<template>
  <div class="profile">
    <h1>Профиль пациента</h1>
    <div v-if="showProfileForm">
      <div class="profile-details">
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>Имя пользователя:</strong> {{ username }}</p>
        <p><strong>Пароль:</strong> {{ password }}</p>
        <p><strong>Имя:</strong> {{ firstName }}</p>
        <p><strong>Фамилия:</strong> {{ lastName }}</p>
        <p><strong>Отчество:</strong> {{ patronymic }}</p>
        <p><strong>Дата рождения:</strong> {{ birthDate }}</p>
        <p><strong>Номер медицинской карты:</strong> {{ medicalCardNumber }}</p>
      </div>
    </div>
    
    

    <div v-else>
    
    <form @submit.prevent="getToken">
    

      <label for="first_name">Имя:</label>
      <input type="text" id="first_name" v-model="firstName">
      
      <label for="last_name">Фамилия:</label>
      <input type="text" id="last_name" v-model="lastName">
      
      <label for="middle_name">Отчество:</label>
      <input type="text" id="middle_name" v-model="patronymic">
      
      <label for="date_of_birth">Дата рождения:</label>
      <input type="date" id="date_of_birth" v-model="birthDate">
      
      <label for="medical_card_number">Номер медицинской карты:</label>
      <input type="text" id="medical_card_number" v-model="medicalCardNumber">
    
      <button type="submit">Сохранить</button>


    </form>
  </div>
  <button type="submit" @click="editProfile()">Отредактировать</button>
  </div>
  <button type="button" @click="logout()" class="logout-button">Выйти из профиля</button>
</template>

<style scoped>
.profile {
  max-width: 500px;
  margin: 40px auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

h1 {
  color: #333;
  margin-bottom: 20px;
}

.profile-details, form {
  margin-top: 20px;
}

.profile-details p, form label {
  margin-bottom: 10px;
  color: #333;
}

strong {
  font-weight: bold;
}

button {
  margin-top: 30px; 
}


input[type="text"],
input[type="date"] {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  padding: 10px 15px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #45a049;
}

.logout-button {
  width: 200px;
  padding: 10px 15px;
  background-color: #f44336;
  margin-left: 650px;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
  margin-top: 0px;
  margin-bottom: 20px;
}

.logout-button:hover {
  background-color: #d32f2f;
}


</style>

<script>
import axios from 'axios';
import router from '@/router';

export default {
  data() {
    return {
      email: '',
      username: '',
      password: '',
      firstName: '',
      lastName: '',
      patronymic: '',
      birthDate: '',
      medicalCardNumber: '',
      showProfileForm: false, 
    }
  },
  mounted() {
    const userData = JSON.parse(localStorage.getItem('userData'));
    if (userData) {
      this.id = userData.id;
      this.email = userData.email;
      this.username = userData.username;
      this.password = userData.password;
      this.firstName = userData.firstName; 
      this.lastName = userData.lastName;
      this.patronymic = userData.patronymic;
      this.birthDate = userData.birthDate;
      this.medicalCardNumber = userData.medicalCardNumber;
    }
  },
  methods: {
    getProfile() {
      const token = localStorage.getItem('token');
      axios.get('http://127.0.0.1:8000/api/patients/', {
        headers: {
          Authorization: `Token ${token}`,
        }
      })
      .then(response => {
        this.id = response.data.id;
        this.firstName = response.data.first_name;
        this.lastName = response.data.last_name;
        this.patronymic = response.data.middle_name;
        this.birthDate = response.data.date_of_birth;
        this.medicalCardNumber = response.data.medical_card_number;
        this.showProfileForm = true;

      })
      .catch(error => {
        console.error('Ошибка:', error);
      });
    },
    getToken() {
      axios.post('http://127.0.0.1:8000/auth/token/login', {
        password: this.password,
        username: this.username

      })
      .then(response => {
        const token = response.data.auth_token;
        this.saveToken(token);
        this.getProfile();
        this.saveProfile();
      })
      .catch(error => {
        console.error('Ошибка:', error);
      });
    },
    saveToken(token) {
        localStorage.setItem('token', token);
    },
    toggleEditForm() {
    this.editProfile();
    this.showProfileForm = !this.showProfileForm;
  },
    saveProfile() {
    const token = localStorage.getItem('token');
    axios.post('http://127.0.0.1:8000/api/patients/', {
    first_name: this.firstName,
    last_name: this.lastName,
    middle_name: this.patronymic,
    date_of_birth: this.birthDate,
    medical_card_number: this.medicalCardNumber
  }, {
    headers: {
      Authorization: `Token ${token}` 
    }
  })
  .then(response => {
    this.id = response.data.id;
    this.firstName = response.data.first_name;
    this.lastName = response.data.last_name;
    this.patronymic = response.data.middle_name;
    this.birthDate = response.data.date_of_birth;
    this.medicalCardNumber = response.data.medical_card_number;

    localStorage.setItem('userData', JSON.stringify({
        id: this.id,
        email: this.email,
        username: this.username,
        password: this.password,
        firstName: this.firstName, 
        lastName: this.lastName,
        patronymic: this.patronymic,
        birthDate: this.birthDate,
        medicalCardNumber: this.medicalCardNumber
      }));
  })
  .catch(error => {
    console.error('Ошибка:', error);
  })

    },
            
editProfile() {
  const token = localStorage.getItem('token');
  const userData = JSON.parse(localStorage.getItem('userData'));
  const id = userData.id;
  axios.put(`http://127.0.0.1:8000/api/patients/${id}/`, {
        first_name: this.firstName,
        last_name: this.lastName,
        middle_name: this.patronymic,
        date_of_birth: this.birthDate,
        medical_card_number: this.medicalCardNumber
      }, {
        headers: {
          Authorization: `Token ${token}`,
        }
      })
      .then(response => {
        this.firstName = response.data.first_name;
        this.lastName = response.data.last_name;
        this.patronymic = response.data.middle_name;
        this.birthDate = response.data.date_of_birth;
        this.medicalCardNumber = response.data.medical_card_number;
      })
      .catch(error => {
        console.error('Ошибка:', error);
      })
  },

  logout() {
      localStorage.removeItem('token');
      localStorage.removeItem('userData');

      this.email = '';
      this.username = '';
      this.password = '';
      this.firstName = '';
      this.lastName = '';
      this.patronymic = '';
      this.birthDate = '';
      this.medicalCardNumber = '';
      this.showProfileForm = false;
      router.push('/home');
    },
}
}

</script>