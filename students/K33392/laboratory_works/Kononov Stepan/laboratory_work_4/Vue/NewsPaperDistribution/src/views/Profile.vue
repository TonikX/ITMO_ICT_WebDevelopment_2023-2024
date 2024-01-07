<template>
  <div class="container mt-5">
    <h2>Профиль пользователя {{ userInfo.username }}</h2>

    <div class="mb-3">
      <label for="firstName" class="form-label">Имя:</label>
      <input type="text" class="form-control" id="firstName" v-model="newFirstName" />
    </div>

    <div class="mb-3">
      <label for="lastName" class="form-label">Фамилия:</label>
      <input type="text" class="form-control" id="lastName" v-model="newLastName" />
    </div>

    <div class="mb-3">
      <label for="middleName" class="form-label">Отчество:</label>
      <input type="text" class="form-control" id="middleName" v-model="newMiddleName" />
    </div>

    <button @click="updateProfile" class="btn btn-primary">Сохранить изменения</button>
  </div>
  <theme-switcher></theme-switcher>
</template>

<script>
import ThemeSwitcher from "@/components/ThemeSwitcher.vue";

export default {
  components: {ThemeSwitcher},
  data() {
    return {
      userInfo: {},
      newFirstName: '',
      newLastName: '',
      newMiddleName: '',
    };
  },
  mounted() {
    this.getUserInfo();
  },
  methods: {
    async getUserInfo() {
      try {
        const response = await fetch('http://127.0.0.1:8000/auth/users/me/', {
          method: 'GET',
          headers: {
            'Authorization': `Token ${localStorage.getItem('authToken')}`,
          },
        });

        const data = await response.json();

        this.userInfo = data;
        this.newFirstName = data.first_name || '';
        this.newLastName = data.last_name || '';
        this.newMiddleName = data.middle_name || '';
      } catch (error) {
        console.error('Ошибка при получении информации о пользователе', error);
      }
    },
    async updateProfile() {
      try {
        const response = await fetch('http://127.0.0.1:8000/auth/users/me/', {
          method: 'PATCH',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${localStorage.getItem('authToken')}`,
          },
          body: JSON.stringify({
            first_name: this.newFirstName,
            last_name: this.newLastName,
            middle_name: this.newMiddleName,
          }),
        });

        const data = await response.json();

        console.log('Профиль успешно обновлен', data);

        this.getUserInfo();
      } catch (error) {
        console.error('Ошибка при обновлении профиля', error);
      }
    },
  },
};
</script>

