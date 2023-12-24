

<template>
  <v-row justify="center" >
    <v-col
      cols="12"
      sm="10"
      md="8"
      lg="6"
      align="center"


    >
      <v-card ref="form" max-width="350px" color="amber-lighten-3" style="top: 20%" >
        <v-card-text>
          <v-text-field
            ref="name"
            v-model="username"
            type="text"
            placeholder="username"
            required
          ></v-text-field>
          <v-text-field
            v-model="password"
            type="password"
            placeholder="password"
            required
          ></v-text-field>

        </v-card-text>
        <v-divider class="mt-12"></v-divider>
        <v-card-actions>
          <v-btn
            color="white"
            variant="text"
            @click="$router.push(`/`)">
            Cancel
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            variant="text"
            @click="setLogin"
          >
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import axios from "axios";
export default {
  name: "Login",
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    async setLogin() {
      try {
        const response = await axios.post('http://localhost:8000/auth/token/login',
          {username: this.username, password: this.password})
        sessionStorage.setItem('token', response.data.auth_token)
        sessionStorage.setItem('username', this.username)
        sessionStorage.setItem('password', this.password)
        await this.$router.push({name: "UserPage"})
        // this.mountains = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },

}
</script>

<style scoped>

</style>
