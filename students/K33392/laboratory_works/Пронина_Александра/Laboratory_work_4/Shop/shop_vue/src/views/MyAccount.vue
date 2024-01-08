<template>
    <div class="page-my-account">
      <!-- ... -->
  
      <div class="column is-12">
        <h2 class="subtitle">Изменить данные профиля</h2>
  
        <form @submit.prevent="updateProfile">
          <div class="field">
            <label class="label">Имя</label>
            <div class="control">
              <input type="text" class="input" v-model="username">
            </div>
          </div>
  
          <div class="field">
            <label class="label">Email</label>
            <div class="control">
              <input type="email" class="input" v-model="email">
            </div>
          </div>
  
          <div class="field">
            <label class="label">Другие поля...</label>
            <!-- Добавьте другие поля для редактирования данных профиля -->
          </div>
  
          <div class="field">
            <div class="control">
              <button type="submit" class="button is-primary">Сохранить</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import OrderSummary from '@/components/OrderSummary.vue'
  
  export default {
    name: 'MyAccount',
    components: {
      OrderSummary
    },
    data() {
      return {
        orders: [],
        username: '', // Добавьте поля для данных профиля
        email: '' // Добавьте поля для данных профиля
      }
    },
    mounted() {
      // ...
      this.loadUserData()
    },
    methods: {
      // ...
  
      async loadUserData() {
        this.$store.commit('setIsLoading', true)
        try {
          const response = await axios.get('/api/v1/users/${this.id}/'); // API endpoint для получения данных пользователя
          const userData = response.data;
          this.username = userData.username; // Присваивание данных из ответа сервера полям данных профиля
          this.email = userData.email; // Присваивание данных из ответа сервера полям данных профиля
          // Присвойте другие данные профиля, если они есть
        } catch (error) {
          console.error('Ошибка при загрузке данных профиля', error);
        }
        this.$store.commit('setIsLoading', false)
      },
  
      async updateProfile() {
  this.$store.commit('setIsLoading', true)
  try {
    const response = await axios.put(`/api/v1/users/${this.id}/`, { 
      username: this.username,
      email: this.email,
      // Добавим позже другие поля для обновления данных профиля
    });
    console.log('Данные профиля успешно обновлены', response.data);
    //  логика после успешного обновления данных профиля
  } catch (error) {
    console.error('Ошибка при обновлении данных профиля', error);
  }
  this.$store.commit('setIsLoading', false)
}
    }
  }
  </script>
  