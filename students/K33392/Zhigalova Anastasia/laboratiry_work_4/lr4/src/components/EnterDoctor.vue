<template>
    <div>
      <h2>Войти как врач</h2>
      <form @submit="login">
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <div>
          <label for="password">Пароль:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <button type="submit">Войти</button>
      </form>
      <h3>Еще не зарегистрированы?</h3>
      <button><router-link to="/registerdoctor" >Зарегистрироваться как врач</router-link></button>
    </div>
  </template>
  
  <script>

  </script>
  