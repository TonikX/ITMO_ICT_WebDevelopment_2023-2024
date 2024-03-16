<template>
  <div>
    <h2>Профиль пользователя</h2>
    <form @submit.prevent="updateProfile">
      <!-- Форма для обновления профиля -->
      <!-- Для демонстрации, пусть будет только email -->
      <div>
        <label for="email">Новый email:</label>
        <input id="email" v-model="user.email" type="email" required>
      </div>
      <button type="submit">Обновить</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'UserProfile',
  data() {
    return {
      user: {
        email: '' // предполагается, что email получен после входа в систему
      }
    }
  },
  methods: {
    async updateProfile() {
      try {
        // Здесь должен быть код для отправки обновленных данных на сервер
        // Например: await axios.patch('/api/user', this.user)
        alert('Профиль обновлен');
      } catch (error) {
        console.error(error);
        // Обработка ошибок
      }
    }
  }
}
</script>


<style scoped>

</style>