

<template>
  <!-- ваш шаблон -->
  <button @click="fetchWarriors">Загрузить воинов</button>
  <div v-for="warrior in warriors" :key="warrior.name">
    {{ warrior.name }}
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      warriors: []
    };
  },
  methods: {
    fetchWarriors() {
      axios.get('http://localhost:3000/api/warriors')
        .then(response => {
          this.warriors = response.data;
        })
        .catch(error => console.error(error));
    }
  },
  mounted() {
    this.fetchWarriors();
  }
};
</script>


<style>
/* ваш стиль */
</style>
