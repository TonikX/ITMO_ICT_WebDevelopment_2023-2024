<template>
  <v-form @submit.prevent="saveChanges">
    <v-text-field v-model="editedUser.last_name" label="Фамилия"></v-text-field>
    <v-text-field v-model="editedUser.first_name" label="Имя"></v-text-field>
    <v-text-field v-model="editedUser.email" label="Email"></v-text-field>
    <v-text-field v-model="editedUser.profile_info" label="Биография"></v-text-field>
    <v-file-input v-model="newProfilePicture" accept="image/*" label="Обновить фото профиля"></v-file-input>
    <v-btn type="submit" color="primary">Сохранить</v-btn>
  </v-form>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    user: Object,
  },
  data() {
    return {
      editedUser: { ...this.user },
      newProfilePicture: null, // To store the new file input value
    };
  },
  methods: {
    saveChanges() {
      const token = localStorage.getItem('token');
      if (token) {
        const headers = { Authorization: `Token ${token}` };

        const formData = new FormData();
        Object.keys(this.editedUser).forEach(key => {
          if (key !== 'profile_picture') {
            formData.append(key, this.editedUser[key]);
          }
        });

        if (this.newProfilePicture) {
          formData.append('profile_picture', this.newProfilePicture);
        }

        if (!this.profile_info) {
          formData.profile_info = '';
        }

        axios.patch(this.$websiteURL + `/auth/users/me/`, formData, { headers })
          .then(response => {
            console.log('User data updated successfully:', response.data);
            this.$emit('changes-saved', response.data);
          })
          .catch(error => {
            console.error('Error updating user data:', error);
          });
      } else {
        console.warn('No token found. User might not be authenticated.');
      }
    },
  },
};
</script>
