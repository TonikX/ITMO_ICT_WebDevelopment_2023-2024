<template>
  <div class="newspaper-list">
    <h1 class="list-title">Список газет</h1>
    <button class="back-button" @click="goToMainPage">На главную</button>
    <ul class="list-container">
      <router-link
        v-for="newspaper in newspapers"
        :key="newspaper.id"
        :to="{ name: 'NewsPaperDetails', params: { id: newspaper.id, newspaper: newspaper }}"
        class="list-item"
      >
        {{ newspaper.title }}
      </router-link>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      newspapers: [],
    };
  },
  methods: {
    async fetchNewspapers() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/newspapers/');
        this.newspapers = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async refreshList() {
      await this.fetchNewspapers();
    },
    goToMainPage() {
      this.$router.push({ name: 'MainPage' });
    },
  },
  created() {
    this.fetchNewspapers();
  },
};
</script>

<style scoped>
.newspaper-list {
  text-align: center;
  padding: 20px;
}

.list-title {
  font-size: 24px;
  margin-bottom: 20px;
  color: #333;
}

.list-container {
  list-style: none;
  padding: 0;
  margin: 0;
}

.list-item {
  display: block;
  padding: 15px 20px;
  margin: 15px 0;
  font-size: 18px;
  border: 1px solid #3498db;
  border-radius: 30px;
  text-decoration: none;
  color: #333;
  transition: background-color 0.3s;
}

.list-item:hover {
  background-color: #3498db;
  color: #fff;
}

.back-button {
  padding: 15px 20px;
  font-size: 18px;
  border: 1px solid #3498db;
  border-radius: 30px; /* Изменено на 30px */
  background-color: transparent;
  color: #3498db;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.back-button:hover {
  background-color: #3498db;
  color: #fff;
}
</style>
