<template>
  <v-app>
    <bar-layout>
      <RegistrationBar/>
    </bar-layout>
    <main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
      <br><br><br><br><br>
      <h1 style="text-align: center;"> Регистрация библиотекарей </h1>
      <br>
      <v-col cols="6" class="mx-auto">
        <v-card max-width=800 color="#f7f4ef">
          <v-row class="py-2">
            <v-col cols="5" class="mx-auto">
              <v-text-field
                label="Логин"
                v-model="signUpForm.username"
                name="username"
                placeholder="maria211"
              />
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="5" class="mx-auto">
              <v-text-field
                label="Имя"
                v-model="signUpForm.first_name"
                name="first_name"
                placeholder="Мария"
              />
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="5" class="mx-auto">
              <v-text-field
                label="Фамилия"
                v-model="signUpForm.last_name"
                name="last_name"
                placeholder="Антонова"
              />
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="5" class="mx-auto">
              <v-text-field
                label="Password"
                v-model="signUpForm.password"
                name="password"
                type=password
              />
            </v-col>
          </v-row>
          <v-col cols="5" class="mx-auto">
            <v-btn block color="blue" @click.prevent="register()"> Register</v-btn>
          </v-col>
        </v-card>
      </v-col>
    </main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import RegistrationBar from '@/components/RegistrationBar.vue'
import axios from 'axios'

export default {
  name: 'SignUp',
  components: {BarLayout, RegistrationBar},
  data: () => ({
    signUpForm: {
      username: '',
      password: '',
      first_name: '',
      last_name: ''
    }
  }),
  methods: {
    async register() {
      try {
        await axios.post('http://127.0.0.1:8000/users/', this.signUpForm)
        this.$router.push({name: 'Login'})
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
        } else if (e.response.data.username) {
          alert('Логин: ' + e.response.data.username)
        } else if (e.response.data.password) {
          alert('Пароль: ' + e.response.data.password)
        } else if (e.response.data.first_name) {
          alert('Имя: ' + e.response.data.first_name)
        } else if (e.response.data.last_name) {
          alert('Фамилия: ' + e.response.data.last_name)
        } else {
          console.error(e.message)
        }

      }
    }
  }
}
</script>
