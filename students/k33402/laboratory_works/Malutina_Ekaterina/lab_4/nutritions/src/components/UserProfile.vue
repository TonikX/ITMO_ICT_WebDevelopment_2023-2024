<template>
  <main class="container-fluid w-auto align-items-center row vh-100">
    <h2>Профиль пользователя</h2>
    <form @submit.prevent="updateProfile">
      <div>
        <label for="email">Новый email:</label>
        <input id="email" v-model="user.email" type="email" required>
      </div>
      <button type="submit">Обновить</button>
    </form>
  </main>
</template>

<script>
export default {
  name: 'UserProfile',
  data() {
    return {
      user: {
        email: ''
      }
    }
  },
  methods: {
    async updateProfile() {
      try {
        alert('Профиль обновлен');
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>


<style scoped>

</style>