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
    this.authStore.userData.bio = ''
    return this.authStore.userData
  },
  methods: {
    updateUserData() {
      api.patch(`api/username/${this.username}/`, {
        email: this.email,
        username: this.username,
        bio: this.bio,
      })
    },
  },

  beforeMount() {
    api
      .get(`api/username/${this.username}`)
      .then((resp) => resp.data)
      .then((data) => {
        console.log(data)
        this.username = data.username
        this.email = data.email
        this.bio = data.bio
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
    <label for="bio">Bio</label>
    <br />
    <textarea name="bio" cols="30" rows="3" v-model="bio"></textarea>
    <br /><br />
    <button v-on:click="updateUserData">Update</button>
  </div>
</template>

<style scoped>
.userInfo {
  padding-top: 20px;
}
</style>

