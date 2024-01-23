<template>
  <div>
    <h1>{{ ascension.route}}</h1>
    <div><strong>Schedule:</strong> from {{ ascension.start_date }} till {{ ascension.planned_end_date }}</div>
    <div v-if="ascension.actual_end_date !== null"> <strong>Actual end date:</strong>  {{ ascension.actual_end_date }}</div>
    <div v-if="ascension.comment !== null"> <strong>Leader comment:</strong>  {{ ascension.comment }}</div>
    <a v-if="ascension.actual_end_date == null"> The ascension has not finished yet</a>
    <br><br>
    <h3>I want to update information a bit</h3>
    <button class="button button" @click="$router.push(`/alp/ascensions/update/${ascension.id}`)">update information</button>
    <button class="button1" @click=delData>delete that ascension</button>

  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Ascension",
  data() {
    return {
      ascension: '',
    }
  },
  methods: {
    async delData(){
      const ascension_id = this.$route.params.ascension_id;
      try{
        const response = await axios.delete(`http://localhost:8000/alp/ascensions/${ascension_id}`,
          {headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
      } catch (error) {
        console.log(error);
        await this.$router.push({name: 'Ascensions'});
      }
    },
    async getData() {
      try {
        const ascension_id = this.$route.params.ascension_id;
        const response = await axios.get(`http://localhost:8000/alp/ascensions/${ascension_id}`,
            { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.ascension = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    this.getData();
  }
}
</script>
<style scoped>


.button1 {
  padding: 2px 120px;
  text-align: center;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
  border-radius: 4px;
  width: 100%;
}

.button1 {
  background-color: #f7baba;
  color: black;
  border: 3px solid #f7baba;
}

.button1:hover {
  background-color: #ff4848;
  color: white;
}

</style>