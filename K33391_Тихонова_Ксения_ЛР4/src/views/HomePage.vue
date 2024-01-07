<template>
  <v-container>
    <v-row justify="center">
        <v-card class="welcome-section" v-if="isLoggedIn">
          <v-card-title class="headline">Добро пожаловать на сайт зоопарка WebZOO!</v-card-title>
          <v-card-text>
            Вы можете использовать панель навигации, чтобы перейти на другие страницы.
          </v-card-text>
        </v-card>

        <v-card class="login-section" v-else>
          <v-card-title class="headline">Вы не вошли в систему.</v-card-title>
          <v-card-text>
            Пожалуйста, войдите в систему, чтобы увидеть больше информации.
          </v-card-text>
        </v-card>

      
        <v-card class="zoo_entree">
          <img src="../assets/zoo_entree.jpg" alt="zoo_entree" height="400" width="600">
        </v-card>
    
    </v-row>
  </v-container>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const isLoggedIn = ref(localStorage.getItem('access_token') !== null);

    return {
      isLoggedIn,
    };
  },
};
</script>

<style scoped>

.container {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.welcome-section,
.login-section {
  display: flex;
  flex-direction: column;
    top: 20px;
  max-width: 800px;
    margin: 0 auto;
    text-align: center;
  background-color: #f7f7f7;
  border-radius: 10px;
  padding: 20px;
  margin-top: 20px;
  margin-bottom: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.headline { 
  font-size: 1.5em;
  margin-bottom: 20px;
  color: #333;
}



</style>
