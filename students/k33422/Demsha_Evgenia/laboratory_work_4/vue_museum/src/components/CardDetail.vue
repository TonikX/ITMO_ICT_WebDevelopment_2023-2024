<template>
  <div class="CardDetail">
    <h1>{{ card.name }}</h1>
    <button @click="addItem">Добавить предмет</button>
    <ul>
      <li v-for="item in items" :key="item.id">
        <p>{{ item.name }}</p>
        <p>{{ item.description }}</p>
        <img :src="item.image" alt="Item Image" height="400">
        <br>
        <select v-model="selectedExhibition">
          <option disabled value="">Выберите выставку</option>
          <option v-for="exhibition in exhibitions" :key="exhibition.id">{{ exhibition.name }}</option>
        </select>
        <button @click="sendToExhibition(item)">Отправить на выставку</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'CardDetail',
  data() {
    return {
      card: {},
      items: [],
      exhibitions: [],
      selectedExhibition: '',
    };
  },
  methods: {
    fetchCard() {
      axios.get(`http://127.0.0.1:8000/api/cards/${this.$route.params.id}/`)
        .then(response => {
          this.card = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    fetchItems() {
      axios.get(`http://127.0.0.1:8000/api/cards/${this.$route.params.id}/items/`)
        .then(response => {
          this.items = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    fetchExhibitions() {
      axios.get('http://127.0.0.1:8000/api/exhibitions/list')
        .then(response => {
          this.exhibitions = response.data.map(exhibition => ({
            id: exhibition.id,
            name: exhibition.name,
          }));
        })
        .catch(error => {
          console.log(error);
        });
    },
    addItem() {
      this.$router.push({ name: 'ItemCreate', query: { card: this.card.id } });
    },
    sendToExhibition(item) {
      const selectedExhibition = this.exhibitions.find(e => e.name === this.selectedExhibition);
      if (selectedExhibition) {
        const data = {
          item: item.id,
          exhibition: selectedExhibition.id,
          send_date: new Date().toISOString().slice(0, 10),
        };
        axios.post('http://127.0.0.1:8000/api/item-to-exhibition/', data)
          .then(response => {
            console.log(response.data);
          })
          .catch(error => {
            console.log(error);
          });
      } else {
          alert("Выставка " + this.selectedExhibition + " не найдена.");
      }
    },
  },
  mounted() {
    this.fetchCard();
    this.fetchItems();
    this.fetchExhibitions();
  },
};
</script>


<style>
.CardDetail {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.CardDetail h1 {
  font-size: 36px;
  margin-bottom: 10px;
}

.CardDetail button {
  padding: 4px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  margin-bottom: 10px;
}

.CardDetail button:hover {
  cursor: pointer;
}

.CardDetail ul {
  list-style-type: none;
  padding: 0;
}

.CardDetail li {
  margin-bottom: 20px;
}

.CardDetail p {
  margin: 0;
}

.CardDetail img {
  margin-top: 10px;
  max-width: 100%;
}
</style>


