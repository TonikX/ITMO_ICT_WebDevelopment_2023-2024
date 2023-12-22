<template>

  <div>
    <h1>Mountains</h1>
    <ul>
      <li v-for='mountain in mountains'>
        <h3>{{ mountain.name }} - {{ mountain.id }}</h3>
      </li>
    </ul>
    <div>
      <input v-model="filterValue" @input="applyFilter" />
      <input v-model="name" type="text" placeholder="name"/>
      <input v-model="state" type="text" placeholder="state"/>
      <input v-model="min_height" type="text" placeholder="min_height"/>
      <input v-model="max_height" type="text" placeholder="max_height"/>
      <button @click="applyFilter">Get</button>
      <ul>
        <li v-for="item in mountains" :key="item.id">{{ item.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import MountainsFilters from "./MountainsFilters.vue";
export default {
  name: "mountains",
  components: {MountainsFilters},
  data() {
    return {
      mountains: [''],
      name: '',
      state: '',
      max_height: '',
      min_height: '',
    }
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get('http://localhost:8000/alp/mountains/',
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.mountains = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async applyFilter() {
      const filter = `http://localhost:8000/alp/mountains/?name=${this.name}&state=${this.state}&min_height=${this.min_height}&max_height=${this.max_height}`
      const response = await axios.get(filter,//`http://localhost:8000/alp/mountains/?search=${this.filterValue}`,
        { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
      this.mountains = response.data;
    },

  },

  created() {
    this.getData();
  }
}
</script>

<style scoped>

</style>
