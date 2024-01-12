<template>
  <div class="foundation-list">
    <h1>Все фонды</h1>
    <ul>
      <li v-for="foundation in foundations" :key="foundation.id">
        <router-link :to="{ name: 'CardList', params: { fond_id: foundation.id } }">{{ foundation.name }}</router-link>
        <span class="percentage">{{ foundation.percentage }}%</span>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'FoundationList',
  data() {
    return {
      foundations: [],
      percentage: 0,
    };
  },
  methods: {
    fetchFoundations() {
      // Fetch all foundations from the API
      axios.get('http://127.0.0.1:8000/api/foundations/list')
        .then(response => {
          this.foundations = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    fetchFoundationRatio() {
      axios.get('http://127.0.0.1:8000/api/foundations/ratio/')
        .then(response => {
          console.log(response.data); // check that the response data is correct
          this.foundations = this.foundations.map(foundation => {
            const ratio = response.data.find(ratio => ratio.id === foundation.id);
            console.log(ratio); // check that the ratio object is found correctly
            return {
              ...foundation,
              percentage: ratio ? ratio.percentage : 0,
            };
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
  mounted() {
    // Fetch all foundations and foundation ratios when the component is mounted
    this.fetchFoundations();
    this.fetchFoundationRatio();
  },
};
</script>

<style scoped>
.foundation-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 800px;
  margin: 0 auto;
}

h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #ccc;
}

li:last-child {
  border-bottom: none;
}

a {
  color: #007bff;
  text-decoration: none;
}

.percentage {
  font-weight: bold;
  margin-left: 1rem; /* add some margin to the left */
}
</style>
