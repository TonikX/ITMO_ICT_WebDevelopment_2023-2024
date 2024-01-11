<template>
  <div class="container">
    <div class="profile-info">
      <h2>Ваш профиль</h2>
      <div>Почта: {{ userData.email }}</div>
      <div>Логин: {{ userData.username }}</div>
    </div>

    <div class="profile-settings">
      <div class="settings-panel">
        <button @click="toggleSettingsPanel">Настройки профиля ▼</button>

        <div v-show="showSettingsPanel" class="settings-dropdown">
          <button @click="toggleChangePasswordForm">Сменить пароль</button>
          <button @click="toggleChangeUsernameForm">Сменить имя пользователя</button>
        </div>
      </div>

      <div v-if="showChangePasswordForm" class="change-password-form">
        <form @submit.prevent="changePassword">
          <label for="currentPassword">Нынешний пароль:</label>
          <input type="password" v-model="currentPassword" required />

          <label for="newPassword">Новый пароль:</label>
          <input type="password" v-model="newPassword" required />

          <button type="submit">Сменить пароль</button>
        </form>
      </div>

      <div v-if="showChangeUsernameForm" class="change-username-form">
        <form @submit.prevent="changeUsername">
          <label for="currentPassword">Нынешний пароль:</label>
          <input type="password" v-model="currentPassword" required />
          <label for="newUsername">Новое имя пользователя:</label>
          <input type="text" v-model="newUsername" required />

          <button type="submit">Сменить логин</button>
          
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      showChangePasswordForm: false,
      showChangeUsernameForm: false,
      showSettingsPanel: false,
      currentPassword: '',
      newPassword: '',
      newUsername: '',
      userData: {},
    };
  },
  mounted() {
    this.fetchUserData();
  },
  methods: {
    async fetchUserData() {
      console.log('Fetching user data...');

      try {
        const response = await axios.get('/auth/users/me/', {
          headers: {
            'Authorization': `Token ${localStorage.getItem('access_token')}`,
          },
        });
        this.userData = response.data;
        console.log('User data:', this.userData);
      } catch (error) {
        console.error('Error fetching user data:', error.response.data);
      }
    },
    async changePassword() {
      try {
        const response = await axios.post('/auth/users/set_password/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('access_token')}`,
          },
          new_password: this.newPassword,
          current_password: this.currentPassword,
        });

        console.log('Password changed successfully:', response.data);
        window.location.reload();
      } catch (error) {
        console.error('Password change failed:', error.response.data);
      }
    },
    async changeUsername() {
      console.log(this.currentPassword, 'username', this.newUsername)
      try {
        const response = await axios.post('/auth/users/set_username/', {
      current_password: this.currentPassword,
      new_username: this.newUsername,
    }, {
      headers: {
        'Authorization': `Token ${localStorage.getItem('access_token')}`,
      },
});


        console.log('Username changed successfully:', response.data);
        window.location.reload();
      } catch (error) {
        console.error('Username change failed:', error.response.data);
      }
    },
    toggleSettingsPanel() {
      this.showSettingsPanel = !this.showSettingsPanel;
    },
    toggleChangePasswordForm() {
      this.showChangePasswordForm = !this.showChangePasswordForm;
    },
    toggleChangeUsernameForm() {
      this.showChangeUsernameForm = !this.showChangeUsernameForm;
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.profile-info {
  background-color: #f7f7f7;
  border-radius: 10px;
  padding: 20px;
  margin: 20px 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  }

.profile-info h2 {
  color: #333;
  margin: 0 0 20px;
}


.settings-panel {
  margin-bottom: 20px;
}

.settings-dropdown {
  display: flex;
  flex-direction: column;
}

button {
  background-color: #3bbc55;
  color: #ffffff;
  padding: 10px;
  margin: 10px;
  border: none;
  cursor: pointer;
  font-size: 1em;
  border-radius: 4px;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

label {
  margin-bottom: 5px;
}

input {
  margin-bottom: 10px;
  padding: 10px;
  font-size: 1em;
}

</style>
