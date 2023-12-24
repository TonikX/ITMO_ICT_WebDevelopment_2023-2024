<template>
  <HelloWorld/>
  <div class="py-12 text-center">
    <h2>Моя страница</h2>
  </div>
  <v-container>

    <v-row>
      <v-col cols="12">

        <v-card>
          <v-card-title >{{ user.first_name }} {{ user.last_name }}</v-card-title>



          <v-card-text >Username: {{ user.username }}</v-card-text>
          <v-divider></v-divider>

          <v-row>
            <v-col cols="12" >
              <v-card-subtitle ><br>Личная информация <br><br>
                Уровень подготовки: {{ user.experience_level }}<br>
                Дата рождения: {{ user.birth_date }}<br><br>
                Телефон: {{ user.phone_number }}<br>
                Электронная почта: {{ user.email }}<br>
                Паспортные данные: {{ user.document }}<br>
                Адрес проживания: {{ user.address }}</v-card-subtitle>
            </v-col>
          </v-row>
          <div class="py-4 pl-4 text-left">
            <UserUpdate v-bind:user="user"></UserUpdate>
          </div>
        </v-card>

      </v-col>
    </v-row>
  </v-container>
  <Participatings/>
</template>

<script>
import axios from "axios";
import HelloWorld from "@/components/HelloWorld.vue";
import Participatings from "@/views/Participatings.vue";
import UserUpdate from "@/components/UserUpdate.vue";

export default {
  name: "UserPage",
  components: {UserUpdate, Participatings, HelloWorld},
  data() {
    return {
      user: '',
    }
  },
  methods: {
    async getUserData() {
      try {
        const response = await axios.get('http://localhost:8000/alp/auth/users/me',
          {headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.user = response.data;
        sessionStorage.setItem('user_id', this.user.id)
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    this.getUserData();
  }
}
</script>

<style scoped>

</style>
