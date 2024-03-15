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
                  label="Login"
                  v-model="signUpForm.username"
                  name="username"
                  placeholder="Enter your username"
              />
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="5" class="mx-auto">
              <v-text-field
                  label="Name"
                  v-model="signUpForm.first_name"
                  name="first_name"
                  placeholder="Like Vasya"
              />
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="5" class="mx-auto">
              <v-text-field
                  label="Last name"
                  v-model="signUpForm.last_name"
                  name="last_name"
                  placeholder="Pupkin"
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
            <v-btn block @click.prevent="register()"> Register</v-btn>
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
import instance from "@/domain/instance";
import LibraryApi from "@/domain/api";
import libraryApi from "@/domain/api";

export default {
  name: 'RegistrationView',
  components: {BarLayout, RegistrationBar, LibraryApi},
  data: () => ({
    signUpForm: {
      first_name: '',
      last_name: '',
      username: '',
      password: '',
    }
  }),
  methods: {
    async register() {
      try {
        await libraryApi.register(this.signUpForm)
        this.$router.push({name: 'Login'})
      } catch (e) {
        console.error(e.message)
      }
    }
  }
}
</script>
