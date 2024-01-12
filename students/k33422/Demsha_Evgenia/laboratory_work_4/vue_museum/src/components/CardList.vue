<template>
  <div class="card-list">
    <h1>Карточки в фонде</h1>
    <button @click="createCard">Создать карточку</button>
    <ul>
      <li v-for="card in cards" :key="card.id">
        <router-link :to="{ name: 'CardDetail', params: { id: card.id } }">{{ card.name }}</router-link>
        <p>Инвентарный номер: {{ card.inventory_number }}</p>
        <p>Страна: {{ card.country }}</p>
        <p>Год создания: {{ card.creation_year }}{{ card.is_year_exact ? '' : '?' }}</p>
        <p>Описание: {{ card.description }}</p>
        <img :src="card.image" alt="Card Image" height="400">
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CardList',
  data() {
    return {
      cards: [],
    };
  },
  methods: {
    createCard() {
    // Redirect to the create card page with the foundation ID parameter
      this.$router.push({ name: 'CardCreate', params: { fond_id: this.$route.params.fond_id } });
    },
    fetchCards() {
      // Fetch all museum cards from the API
      axios.get(`http://127.0.0.1:8000/api/foundations/${this.$route.params.fond_id}/cards/`)
        .then(response => {
          this.cards = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
  mounted() {
    // Fetch all museum cards when the component is mounted
    this.fetchCards();
  },
};
</script>


<style scoped>
.card-list {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  font-size: 36px;
  margin-bottom: 20px;
}

button {
  background-color: #0074D9;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
  margin-bottom: 20px;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  margin-bottom: 40px;
}

li a {
  font-size: 24px; /* increase font size of card name */
  text-decoration: none;
  color: #000;
}

p {
  margin: 0;
}

img {
  display: block;
  margin-top: 20px;
}
</style>