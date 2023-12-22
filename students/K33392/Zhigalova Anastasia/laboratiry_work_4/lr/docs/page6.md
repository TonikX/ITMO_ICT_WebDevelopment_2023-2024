# TheWelcome.vue

![](images/10.png)

``` 
<template>
  <div class="container">
    <img alt="Vue logo" class="logo" src="@/assets/logo.png" />
    <div class="content">
      <h1>Добро пожаловать!</h1>
      <button @click="loginAsPatient">Войти как пациент</button>
    </div>
  </div>
</template>

<script>
import EnterPatientView from '../views/EnterPatientView.vue';

export default {
  methods: {
    loginAsPatient() {
      console.log('Вход как пациент');
      this.$router.push({ path: '/enterpatient', name: 'enterpatient', component: EnterPatientView });
    },
  },
};
</script>

<style scoped>
.container {
  text-align: center;
  padding: 20px;
}

.logo {
  width: 180px;
  height: 150px;
  margin-bottom: 20px;
}

.content {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: inline-block;
}

h1 {
  color: #333;
  margin-bottom: 20px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #45a049;
}
</style>
```