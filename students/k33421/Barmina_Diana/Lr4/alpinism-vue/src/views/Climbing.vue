<template>
  <div>
    <h1>{{ climbing.name }}</h1>
    <h3>{{climbing.start_date_plan}} - {{ climbing.finish_date_plan }}</h3>
    <h4 @click="$router.push(`/clubs/${climbing.club_id.id}`)">Клуб-организатор: {{ climbing.club_id.name }} </h4>
    <h4>Цель восхождения: {{ climbing.mountain_id.name }}</h4>
    <h5>Макс. кол-во участников: {{ climbing.max_participants }}  Цена: {{ climbing.cost }} Уровень: {{ climbing.level }}</h5>
    <p>Описание: {{ climbing.description }}</p>
    Участники:
    <div v-for="alp in climbing.alpinists"> <!-- v-for - директива для отображения списка элементов на основе массива. -->
      <div><strong>Имя Фамилия:</strong> {{ alp.first_name }} {{ alp.last_name }}</div>
    </div>
    <ParticipatingForm v-if="!alpinism"
                        v-bind:climbing="climbing"></ParticipatingForm>
    <ParticipatingDelete v-if="alpinism" v-bind:climbing="climbing"></ParticipatingDelete>

  </div>
</template>

<script>
import axios from "axios";
import ParticipatingForm from "../components/ParticipatingForm.vue";
import ParticipatingDelete from "../components/ParticipatingDelete.vue";

export default {
  name: "Climbing",
  components: {ParticipatingDelete, ParticipatingForm},
  data() {
    return {
      climbing: '',
    }
  },
  methods: {
    async getData() {
      try {
        const climbing_id = this.$route.params.climbing_id;
        console.log(climbing_id)
        const response = await axios.get(`http://localhost:8000/alp/climbings/${climbing_id}`,
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.climbing = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    alpinism() {
      let array = [];
      let alpinists = this.climbing.alpinists;
      if (alpinists.length < this.climbing.max_participants) {
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
    alpinism2() {
      let array = [];
      let alpinists = this.climbing.alpinists;

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
