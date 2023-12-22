<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div>
        <nav>
          <ul>
            <li><router-link to="/main">Главная</router-link></li>
            <li><router-link to="/doctorslist">Врачи клиники</router-link></li>
            <li><router-link to="/appointments">Мои записи</router-link></li>
            <li><router-link to="/profilepatient">Мой профиль</router-link></li>
          </ul>
        </nav>
    </div>
  </template>
  
  <style scoped>
  nav {
    background-color: #4CAF50; 
    padding: 10px 0;
    text-align: center;
  }
  
  nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
  }
  
  nav ul li {
    display: inline;
    margin-right: 20px;
  }
  
  nav ul li a {
    text-decoration: none;
    color: white; 
    font-size: 18px;
    padding: 5px 10px;
    border-radius: 5px;
    transition: background-color 0.3s, color 0.3s;
  }
  
  nav ul li a:hover {
    background-color: white; 
    color: #4CAF50; 
  }
  </style>