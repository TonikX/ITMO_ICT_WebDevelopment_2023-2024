<template>
  <HelloWorld/>
  <v-container>

    <v-row>
      <v-col cols="12">

        <v-card>
          <v-card-title >{{ club.name }}</v-card-title>



          <v-card-text > {{ club.state }}, {{ club.city}}</v-card-text>
          <v-divider></v-divider>

          <v-row>
            <v-col cols="6" >
              <v-card-subtitle ><br>Контактные данные<br><br>
                Менеджер: {{ club.contact_person }}<br>
                Телефон: {{ club.phone_number }}<br>
                Электронная почта: {{ club.email }}</v-card-subtitle>
            </v-col>
          </v-row>
          <br><v-divider></v-divider>
          <v-row>
            <v-col cols="6" v-for="alp in alpinists">
              <v-card-text><br>Член клуба<br><br>
                {{ alp.first_name }} {{ alp.last_name }}<br>
                Уровень подготовки: {{ alp.experience_level }}<br>
                </v-card-text>
            </v-col>
          </v-row>
          <br/><v-divider></v-divider>
          <br><v-card-actions>
            <v-spacer></v-spacer>
            <ClubMembershipForm v-if="!alpinism"
                                v-bind:club="club"></ClubMembershipForm>
            <ClubMembershipDelete v-if="alpinism" v-bind:club="club"></ClubMembershipDelete>
          </v-card-actions>
          <br>
        </v-card>

      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import ClubMembershipForm from "../components/ClubMembershipForm.vue";
import ClubMembershipDelete from "../components/ClubMembershipDelete.vue";
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Club",
  components: {HelloWorld, ClubMembershipDelete, ClubMembershipForm},
  data() {
    return {
      club: '',
      alpinists: [],
    }
  },
  methods: {
    async getData() {
      try {
        const club_id = this.$route.params.club_id;
        const response = await axios.get(`http://localhost:8000/alp/clubs/${club_id}`,
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.club = response.data;
        this.alpinists = response.data.alpinists;
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    alpinism() {
      let array = [];
      let alpinists = this.club.alpinists;
      for (const alp in alpinists) {
        array.push(alpinists[alp].id);
      }
      let user = sessionStorage.getItem("user_id")
      for (let i in array) {
        if (array[i] == user) {
          return true
        }
      }

    }
  },
  mounted() {
    this.getData();
  }
}
</script>

<style scoped>

</style>
