<template>
  <div>
    <h1>{{ club.name }}</h1>
    <h3>{{club.state}}, {{ club.city }}</h3>
    Члены клуба (всего {{ club.alpinists.length }}):
    <div v-for="alp in club.alpinists"> <!-- v-for - директива для отображения списка элементов на основе массива. -->
      <div><strong>Имя:</strong> {{ alp.first_name }} {{ alp.last_name }}</div>
    </div>
    <ClubMembershipForm v-if="!alpinism"
      v-bind:club="club"></ClubMembershipForm>
    <ClubMembershipDelete v-if="alpinism" v-bind:club="club"></ClubMembershipDelete>


  </div>
</template>

<script>
import axios from "axios";
import ClubMembershipForm from "../components/ClubMembershipForm.vue";
import ClubMembershipDelete from "../components/ClubMembershipDelete.vue";

export default {
  name: "Club",
  components: {ClubMembershipDelete, ClubMembershipForm},
  data() {
    return {
      club: '',
    }
  },
  methods: {
    async getData() {
      try {
        const club_id = this.$route.params.club_id;
        const response = await axios.get(`http://localhost:8000/alp/clubs/${club_id}`,
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.club = response.data;
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
