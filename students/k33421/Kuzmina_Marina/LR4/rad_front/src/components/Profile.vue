<template>
  <div>
    <h2>Profile</h2>
    <p v-if="!isEditing">Username: {{ 'alina'+ user.username }} <button class="styled-button" @click="startEditing">Edit</button></p>
    <input v-if="isEditing" v-model="profile.username" />
    <h3>Books:</h3>
    <ul>
      <li v-for="userBookStatus in userBooks" :key="userBookStatus.book.id">
        {{ userBookStatus.book.title }} - {{ userBookStatus.status }}
      </li>
    </ul>
    <button class="styled-button" @click="updateProfile">{{ isEditing ? 'Save'  : 'Update Profile'}}</button>
  </div>
</template>


<style scoped>
.styled-button {
  background-color: #FFFFFF;
  color: #000000;
  padding: 10px 20px;
  border: 1px solid #ddd;
  cursor: pointer;
  border-radius: 7px;
  transition: transform 0.3s;
}
.styled-button:hover {
  transform: scale(1.1);
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: {},
      profile: {},
      userBooks: [],
      isEditing: false,
    };
  },
  mounted() {
    this.fetchProfileData();
    this.fetchUserBooks();
  },

  methods: {
    // fetchProfileData() {
    //   const token = localStorage.getItem('token');
    //   console.log(token);
    //   if (token) {
    //     const headers = {Authorization: `Token ${token}`};
    //     axios.get('http://localhost:8000/api/profile/', {headers})
    //       .then(response => {
    //         this.user = response.data;
    //       })
    //       .catch(error => {
    //         console.error('Error fetching user data:', error);
    //       });
    //   } else {
    //     console.warn('No token found. User might not be authenticated.');
    //   }
    // },
    fetchProfileData() {
      const token = localStorage.getItem('token');

      if (token) {
        const headers = {Authorization: `Token ${token}`};

        axios.get('http://localhost:8000/api/profile/', {headers})
          .then(response => {
            console.log(response.data);
            this.user = response.data;
          })
          .catch(error => {
            console.error('Error fetching user data:', error);


            if (error.response && error.response.status === 401) {
              console.warn('Unauthorized access. User is not authenticated.');
            }
          });
      } else {
        console.warn('No token found. User might not be authenticated.');
        // Дополнительные действия для случая отсутствия токена, например, перенаправление на страницу входа.
      }
    },

    fetchUserBooks() {
      const token = localStorage.getItem('token');
      if (token) {
        const headers = {Authorization: `Token ${token}`};
        axios.get('http://localhost:8000/api/user_books/', {headers})
          .then(response => {
            this.userBooks = response.data;
          })
          .catch(error => {
            console.error('Error fetching user books:', error);
          });
      } else {
        console.warn('No token found. User might not be authenticated.');
      }
    },

    updateProfile() {
      console.log('jopa');
      console.log(this.profile);
      axios.put('http://localhost:8000/api/profile/', this.profile)
        .then(response => {
          console.log(response.data);
          // Обновите данные пользователя после успешного обновления
          this.user = response.data;
          this.stopEditing();
        })
        .catch(error => {
          console.error(error);
        });
    },

    startEditing() {
      this.profile.username = this.user.username;
      this.isEditing = true;
    },

    stopEditing() {
      this.isEditing = false;
    },
  },
};

</script>

<style>
/* Стили по вашему усмотрению */
</style>


