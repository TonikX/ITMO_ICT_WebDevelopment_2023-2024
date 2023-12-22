<template>
    <div class="profile">
      <h1>Профиль пациента</h1>
      <div class="profile">
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>Имя пользователя:</strong> {{ username }}</p>
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>Имя:</strong> {{ first_name }}</p>
        <p><strong>Фамилия:</strong> {{ last_name }}</p>
        <p><strong>Отчество:</strong> {{ middle_name }}</p>
        <p><strong>Дата рождения:</strong> {{ date_of_birth }}</p>
        <p><strong>Номер медицинской карты:</strong> {{ medical_card_number }}</p>
      </div>
      
    </div>
  </template>

<style scoped>
 .profile {
      max-width: 400px;
      margin: 0 auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    h1 {
      text-align: center;
    }

    .profile-details {
      margin-top: 20px;
    }

    strong {
      font-weight: bold;
    }

    p {
      margin-bottom: 10px;
    }

    label {
      display: block;
      margin-bottom: 5px;
    }

    input[type="text"],
    input[type="date"] {
      width: 100%;
      padding: 5px;
      border-radius: 3px;
      border: 1px solid #ccc;
    }

    button[type="submit"] {
      display: block;
      width: 100%;
      padding: 10px;
      background-color: #007bff;
      color: #fff;
      border-radius: 3px;
      border: none;
      cursor: pointer;
      margin-top: 20px;
    }
</style>

<script>

export default {
  data() {
    return {
      email: '',
      username: '',
      first_name: '',
      lastName: '',
      patronymic: '',
      birthDate: '',
      medicalCardNumber: '',
    }
  },
  mounted() {
    const userData = JSON.parse(localStorage.getItem('userData'));
    if (userData) {
      this.email = userData.email;
      this.username = userData.username;
      this.first_name = userData.first_name;
      this.last_name = userData.last_name;
      this.middle_name = userData.middle_name;
      this.date_of_birth = userData.date_of_birth;
      this.medical_card_number = userData.medical_card_number;
     
    }
  },
}
</script>