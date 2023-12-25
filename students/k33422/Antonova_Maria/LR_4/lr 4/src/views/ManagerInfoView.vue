<template>
  <v-app>
    <bar-layout>
      <ManagerInfo/>
    </bar-layout>
    <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
      <v-row class="mx-3.5">
        <v-col cols="4" class="mx-auto">
          <br><br>
          <div>
            <v-card
              elevation="2"
              outlined
              class="my-2"
            >
              <v-card-title>
                <h2>Личный кабинет</h2>
              </v-card-title>

              <v-card-text>
                <div class="text--primary">
                  <b>Имя:</b> {{ this.manager.first_name }} <br>
                  <b>Фамилия:</b> {{ this.manager.last_name }} <br>
                  <b>Логин:</b> {{ this.manager.username }} <br>
                </div>
              </v-card-text>
            </v-card>
            <v-btn block color="green" light @click.prevent="goEdit">Редактировать профиль</v-btn>
          </div>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import ManagerInfo from '@/components/ManagerInfo.vue'
import axios from 'axios'

export default {
  name: 'ManagerLK',
  components: {BarLayout, ManagerInfo: ManagerInfo},
  data() {
    return {
      manager: {}
    }
  },
  created() {
    this.loadManagerData()
  },
  methods: {
    async loadManagerData() {
      const response = await axios
        .get('http://127.0.0.1:8000/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.auth_token}`
          }
        })
      this.manager = response.data
    },
    goEdit() {
      this.$router.push({name: 'EditManager'})
    }
  }
}
</script>
