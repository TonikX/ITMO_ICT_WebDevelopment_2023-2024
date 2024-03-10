<template>
  <div class="container">
    <div class="profile-info">
      <h2>Profile</h2>
      <div class="info-item"><strong>Login:</strong> {{ userData.username }}</div>
      <div class="info-item"><strong>Email:</strong> {{ userData.email }}</div>
    </div>

    <div class="profile-settings">
      <div class="settings-panel">
        <button @click="toggleSettingsPanel">Change User Data</button>

        <div v-show="showSettingsPanel" class="settings-dropdown">
          <button @click="toggleChangeUsernameForm">Change Username</button>
          <button @click="toggleChangePasswordForm">Change Password</button>
        </div>
      </div>

      <div v-if="showChangePasswordForm" class="change-form">
        <form @submit.prevent="changePassword" class="form">
          <label for="currentPassword">Current Password:</label>
          <input type="password" v-model="currentPassword" required />

          <label for="newPassword">New Password:</label>
          <input type="password" v-model="newPassword" required />

          <button type="submit">Change Password</button>
        </form>
      </div>

      <div v-if="showChangeUsernameForm" class="change-form">
        <form @submit.prevent="changeUsername" class="form">
          <label for="currentPassword">Current Password:</label>
          <input type="password" v-model="currentPassword" required />

          <label for="newUsername">New Username:</label>
          <input type="text" v-model="newUsername" required />

          <button type="submit">Change Username</button>
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
          new_password: this.newPassword,
          current_password: this.currentPassword,
        }, {
          headers: {
            'Authorization': `Token ${localStorage.getItem('access_token')}`,
          },
        });

        console.log('Password changed successfully:', response.data);
        this.showChangePasswordForm = false;
      } catch (error) {
        console.error('Password change failed:', error.response.data);
      }
    },
    async changeUsername() {
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
        this.showChangeUsernameForm = false;
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
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.profile-info {
  margin-bottom: 20px;
}

.info-item {
  margin-bottom: 10px;
}

.profile-settings {
  border-top: 1px solid #ddd;
  padding-top: 20px;
}

.settings-panel {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.settings-dropdown {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center the buttons */
}

.change-form {
  margin-top: 20px;
}

.form {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 5px;
}

input {
  margin-bottom: 10px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  padding: 10px;
  background-color: #5a5a5a;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 10px; /* Add margin for spacing between buttons */
}

button:hover {
  background-color: #212121;
}
</style>