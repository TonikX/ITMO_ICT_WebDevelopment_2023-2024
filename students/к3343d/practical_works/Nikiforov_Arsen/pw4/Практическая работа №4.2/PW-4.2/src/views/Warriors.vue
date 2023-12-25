<template>
  <div class="app">
    <h1>Портал информации о войнах в онлайн РПГ</h1>
    <button @click="fetchWarriors">Получить список воинов</button>
    <warrior-form @warriorAdded="fetchWarriors" />
    <div v-for="warrior in warriors" :key="warrior.id">
      <div>Имя: {{ warrior.name }}</div>
      <div>Расса: {{ warrior.race }}</div>
    </div>
  </div>
</template>

<script>
import WarriorForm from "@/components/WarriorForm.vue";
import axios from "axios";

export default {
  components: {
    WarriorForm,
  },
  data() {
    return {
      warriors: [],
    };
  },
  methods: {
    fetchWarriors() {
      axios.get("http://localhost:3000/api/warriors") // Измените порт на тот, который вы указали в сервере
        .then(response => {
          this.warriors = response.data;
        })
        .catch(error => console.error(error));
    },
  },
  mounted() {
    this.fetchWarriors();
  },
};
</script>

<style>
/* Стилизация по  усмотрению */
</style>
