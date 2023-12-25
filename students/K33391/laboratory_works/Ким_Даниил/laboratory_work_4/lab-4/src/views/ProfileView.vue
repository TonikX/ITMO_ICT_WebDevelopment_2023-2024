<script>
import { useAuthStore } from '@/store/auth'
import router from '@/router'
import api from '@/api'
export default {
  data() {
    this.authStore = useAuthStore()
    if (this.authStore.userData.username === '') {
      router.push({ path: '/auth' })
      return
    }
    this.authStore.userData.email = ''
    return this.authStore.userData
  },
  methods: {
    updateUserData() {
      api.put(`auth/users/me/`, {
        email: this.email,
        username: this.username,
      })
    },
  },

  beforeMount() {
    api
        .get(`auth/users/me/`)
        .then((resp) => resp.data)
        .then((data) => {
          console.log(data)
          this.username = data.username
          this.email = data.email
        })
  },
}
</script>

<template>
  <div class="userInfo">
    <label for="username">Username</label>
    <br />
    <input type="text" name="username" v-model="username" />
    <br /><br />
    <label for="email">Email</label>
    <br />
    <input type="email" name="email" v-model="email" />
    <br /><br />
    <button v-on:click="updateUserData">Update</button>
  </div>
</template>

<style scoped>
.userInfo {
  padding-top: 20px;
}
</style>