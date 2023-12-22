# MyAppointments.vue

![](images/7.png)
![](images/8.png)

``` 
<template>
<div class="appointment-form-container">
  <h2>Запись на прием</h2>
  <form @submit.prevent="getProfile" class="appointment-form">

    <label for="date_time">Дата и время приема:</label><br>
    <input type="datetime-local" id="date_time" v-model="appointmentData.date_time"><br>
    
    <label for="diagnosis">Диагноз, заполняется врачом после приема:</label><br>
    <input type="text" id="diagnosis" v-model="appointmentData.diagnosis"><br>

    <label for="current_condition">Симптомы:</label><br>
    <input type="text" id="current_condition" v-model="appointmentData.current_condition"><br>

    <label for="treatment_recommendations">Рекомендации, заполняются врачом после приема:</label><br>
    <input type="text" id="treatment_recommendations" v-model="appointmentData.treatment_recommendations"><br>

    <label for="doctor">Врач:</label><br>
      <select v-model="appointmentData.doctor">
        <option v-for="doctor in doctors" :key="doctor.id" :value="doctor.id">{{ doctor.last_name }}</option>
      </select><br>
      
      <label for="patient">Пациент:</label><br>
      <select v-model="appointmentData.patient">
        <option v-for="patient in patients" :key="patient.id" :value="patient.id">{{ patient.last_name }}</option>
      </select><br>
      
      <label for="cabinet">Кабинет:</label><br>
      <select v-model="appointmentData.cabinet">
        <option v-for="cabinet in cabinets" :key="cabinet.id" :value="cabinet.id">{{ cabinet.name }}</option>
      </select><br>

    <input type="submit" value="Записаться">
    
  </form>

  <button @click="goto">Посмотреть мои записи</button>
</div>

</template>

<style scoped>
.appointment-form-container {
  max-width: 500px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

h2 {
  text-align: center;
  color: #333;
  margin-bottom: 20px;
}

.appointment-form label {
  display: block;
  margin-bottom: 5px;
  color: #333;
  font-weight: bold;
}

.appointment-form input[type="text"],
.appointment-form input[type="datetime-local"],
.appointment-form select {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.appointment-form input[type="submit"] {
  width: 100%;
  padding: 10px 15px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.appointment-form input[type="submit"]:hover {
  background-color: #45a049;
}
</style>

  
<script>
import router from '@/router';
import axios from 'axios';

export default {
  data() {
    return {
        doctors: [], 
        patients: [], 
        cabinets: [],
        token: null,
        appointmentData: {
          date_time: '',
          diagnosis: '',
          current_condition: '',
          treatment_recommendations: '',
          doctor: '',
          patient: '',
          cabinet: '',
      },
    };
  },
  mounted() {
    this.loginAndGetToken().then(() => {
      if (this.token) {
        this.getDoctors();
        this.getPatients();
        this.getCabinets();
      } else {
        console.error('Токен не получен. Проверьте учетные данные и повторите попытку.');
      }
    });
},
  methods: {
    async loginAndGetToken() {
  try {
    const userData = JSON.parse(localStorage.getItem('userData'));
    if (!userData || !userData.username || !userData.password) {
      console.error('Данные пользователя не найдены в localStorage.');
      return;
    }
    console.log('Отправка данных для аутентификации:', userData); 

    const response = await axios.post('http://127.0.0.1:8000/auth/token/login/', {
      username: userData.username,
      password: userData.password,
    });

    if (response.data && response.data.auth_token) {
      this.token = response.data.auth_token;
    } else {
      console.error('Токен не найден в ответе сервера:', response.data);
    }
  } catch (error) {
    console.error('Ошибка при получении токена:', error.response ? error.response.data : error);
  }
  
},
    
    getDoctors() {
    axios.get('http://127.0.0.1:8000/api/doctors/', {
      headers: {
        Authorization: `Token ${this.token}`
      }
    })
    .then(response => {
      this.doctors = response.data;
    })
    .catch(error => {
      console.error('Ошибка при получении списка врачей:', error);
    });
  },
  getPatients() {
    axios.get('http://127.0.0.1:8000/api/patients/', {
      headers: {
        Authorization: `Token ${this.token}`
      }
    })
    .then(response => {
      this.patients = response.data;
    })
    .catch(error => {
      console.error('Ошибка при получении списка пациентов:', error);
    });
  },
  getCabinets() {
    axios.get('http://127.0.0.1:8000/api/cabinets/', {
      headers: {
        Authorization: `Token ${this.token}`
      }
    })
    .then(response => {
      this.cabinets = response.data;
    })
    .catch(error => {
      console.error('Ошибка при получении списка кабинетов:', error);
    });
  },
    getProfile() {
      axios.get('http://127.0.0.1:8000/api/appointments/', {
        headers: {
          Authorization: `Token ${this.token}`,
        }
      })
      .then(response => {
        this.date_time = response.data.date_time;
        this.diagnosis = response.data.diagnosis;
        this.current_condition = response.data.current_condition;
        this.treatment_recommendations = response.data.treatment_recommendations;
        this.doctor = response.data.doctor;
        this.patient = response.data.patient;
        this.cabinet = response.data.cabinet;
        this.saveProfile();
        router.push('/registerdoctor');

      })
      .catch(error => {
        console.error('Ошибка:', error);
      });
    },
    saveProfile() {
    console.log('Отправляемые данные:', this.appointmentData); 
    axios.post('http://127.0.0.1:8000/api/appointments/', this.appointmentData, { 
    headers: {
      Authorization: `Token ${this.token}` 
    }
  })
  .then(response => {
    this.date_time = response.data.date_time;
    this.diagnosis = response.data.diagnosis;
    this.current_condition = response.data.current_condition;
    this.treatment_recommendations = response.data.treatment_recommendations;
    this.doctor = response.doctor;
    this.patient = response.data.patient;
    this.cabinet = response.data.cabinet;
  })
  .catch(error => {
    console.error('Ошибка:', error);
  })

    },
  goto(){
    router.push('/registerdoctor');
  },
}
}

</script>
```