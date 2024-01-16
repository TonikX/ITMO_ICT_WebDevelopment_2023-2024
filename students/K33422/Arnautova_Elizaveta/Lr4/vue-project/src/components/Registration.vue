<template>
  <form @submit.prevent="hundleSubmit">
    <h1>Register</h1>

    <div class="from-group">
      <input type="text" class="form-control" v-model="first_name" placeholder="Name"/>
    </div>
    <br>

    <div class="from-group">
      <input type="text" class="form-control" v-model="last_name" placeholder="Surname"/>
    </div>
    <br>

    <div class="from-group">
      <input type="email" class="form-control" v-model="email" placeholder="Email (We solemnly swear not to send you spam)"/>
    </div>
    <br>

    <div class="from-group">
      <input type="text" class="form-control" v-model="username" placeholder="Username"/>
    </div>
    <br>

    <div class="from-group">
      <input type="password" class="form-control" v-model="password" placeholder="Password"/>
    </div>
    <br>

    <div class="from-group">
      <input type="password" class="form-control" v-model="password_confirm" placeholder="Password confirmation"/>
    </div>
    <br>

    <button class="button button">Register</button>
  </form>
</template>

<script>
import axios from "axios";
export default {
  name: "Registration",
  data() {
    return {
      first_name: '',
      last_name: '',
      email: '',
      username: '',
      password: '',
    }
  },
  methods: {
    async hundleSubmit() {
      const response = await axios.post('http://localhost:8000/auth/users/', {
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
        username: this.username,
        password: this.password,
      });
      console.log(response);
      await this.$router.push({name: 'Login'});
    }
  },
}
</script>
<style scoped>
</style>