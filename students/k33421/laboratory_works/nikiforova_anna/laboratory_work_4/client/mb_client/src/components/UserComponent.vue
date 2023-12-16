<template>
  <v-container>
    <v-card>
      <v-row>
        <v-col cols="6" md="3">
          <v-avatar size="250" class="my-custom-avatar">
            <v-img :src="user.profile_picture" alt="User Profile" class="my-custom-image" max-height="200"></v-img>
          </v-avatar>
        </v-col>

        <v-col cols="6" md="4">
          <v-card-title class="headline">{{ user.first_name }} {{ user.last_name }}</v-card-title>
          <v-card-subtitle>{{ user.username }}</v-card-subtitle>

          <v-list>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Email:</v-list-item-title>
                <v-list-item-subtitle>{{ user.email }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Биография:</v-list-item-title>
                <v-list-item-subtitle>{{ user.profile_info || 'Не указана' }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list>
          <v-card-actions>
            <v-btn @click="openEditDialog" class="mr-4">Редактировать</v-btn>
            <v-btn @click="deleteUser" color="error">Удалить</v-btn>
          </v-card-actions>
        </v-col>
      </v-row>
    </v-card>

    <v-dialog v-model="editDialog" max-width="500">
      <v-card>
        <v-card-title>Редактирование профиля</v-card-title>
        <v-card-text>
          <EditUserComponent :user="user" @changes-saved="updateUserData"/>
        </v-card-text>
        <v-card-actions>
          <v-btn @click="closeEditDialog" class="ml-2">Закрыть</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </v-container>
</template>

<script>
import axios from 'axios';
import EditUserComponent from '@/components/EditUserComponent.vue';

export default {
  props: {
    user: Object,
  },
  components: {EditUserComponent},
  data() {
    return {
      editDialog: false,
    };
  },
  methods: {
    openEditDialog() {
      this.editDialog = true;
    },
    closeEditDialog() {
      this.editDialog = false;
    },
    updateUserData(updatedUser) {
      this.user = updatedUser;
      this.closeEditDialog();
    },
    deleteUser() {
      const isConfirmed = window.confirm('Вы уверены, что хотите удалить свой аккаунт? Это действие необратимо.');

      if (isConfirmed) {
        const token = localStorage.getItem('token');
        if (token) {
          const headers = {Authorization: `Token ${token}`};
          axios.delete(this.$websiteURL + '/auth/users/me/', {headers})
            .then(() => {
              console.log('User deleted successfully');
            })
            .catch(error => {
              console.error('Error deleting user:', error);
            });
        } else {
          console.warn('No token found. User might not be authenticated.');
        }
      } else {
        console.log('User canceled deletion');
      }
    },
  },
};
</script>

<style scoped>
.my-custom-avatar {
  padding: 20px;
}

.my-custom-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
