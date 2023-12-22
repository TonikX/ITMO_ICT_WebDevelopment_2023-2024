<template>

  <div class="climbings-container">
    <h1>Восхождения</h1>
    <div v-for="climbing in climbings"> <!-- v-for - директива для отображения списка элементов на основе массива. -->
      <strong>Название:</strong> {{ climbing.name }}
      <div><strong>Даты:</strong> {{ climbing.start_date_plan }} - {{ climbing.finish_date_plan }}</div>
      <div><strong>Цена:</strong> {{ climbing.cost }}</div>
      <div><strong>Макс кол-во участников:</strong> {{ climbing.max_participants }}</div>
      <br/>
      <div>
        <button v-if="auth" @click="$router.push(`/climbings/${climbing.id}`)">Подробнее</button>
      </div>
      <br/><br/>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ClimbingsList",
  data() {
    return {
      climbings: ['']
    }
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get('http://localhost:8000/alp/climbings/',
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.climbings = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    auth() {
      if (sessionStorage.getItem("token")) {
        return true
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
