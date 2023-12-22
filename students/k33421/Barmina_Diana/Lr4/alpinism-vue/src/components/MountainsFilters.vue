<template>
  <div>
    <input v-model="filterValue" @input="applyFilter" />
    <input v-model="name" type="text" placeholder="name"/>
    <input v-model="state" type="text" placeholder="state"/>
    <input v-model="min_height" type="text" placeholder="min_height"/>
    <input v-model="max_height" type="text" placeholder="max_height"/>
    <button @click="applyFilter">Get</button>
    <ul>
      <li v-for="item in items" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MountainsFilters",
  data() {
    return {
      items: [],
      filterValue: '',
      name: '',
      state: '',
      max_height: '',
      min_height: '',
    };
  },
  async created() {
    const response = await axios.get('http://localhost:8000/alp/mountains/',
      { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});

    this.items = response.data;
  },
  computed: {
    filteredItems() {
      return this.items.filter(item => item.name.includes(this.filterValue));
    },
  },
  methods: {
    async applyFilter() {
      const filter = `http://localhost:8000/alp/mountains/?name=${this.name}&state=${this.state}&min_height=${this.min_height}&max_height=${this.max_height}`
      const response = await axios.get(filter,//`http://localhost:8000/alp/mountains/?search=${this.filterValue}`,
        { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
      this.items = response.data;
    },
  },
}
</script>

<style scoped>

</style>
