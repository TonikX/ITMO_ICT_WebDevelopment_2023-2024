<template>
  <div class="card-create">
    <h1>Create New Card</h1>
    <form @submit.prevent="createCard">
      <div>
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="card.name" required>
      </div>
      <div>
        <label for="inventory_number">Inventory Number:</label>
        <input type="number" id="inventory_number" v-model="card.inventory_number" required>
      </div>
      <div>
        <label for="image">Image:</label>
        <input type="file" id="image" @change="onFileChange" accept="image/*">
      </div>
      <div>
        <label for="country">Country:</label>
        <input type="text" id="country" v-model="card.country">
      </div>
      <div>
        <label for="creation_year">Creation Year:</label>
        <input type="number" id="creation_year" v-model="card.creation_year" required>
      </div>
      <div>
        <label for="is_year_exact">Is Year Exact:</label>
        <input type="checkbox" id="is_year_exact" v-model="card.is_year_exact">
      </div>
      <div>
        <label for="description">Description:</label>
        <textarea id="description" v-model="card.description"></textarea>
      </div>
      <div>
        <button type="submit">Create</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CardCreate',
  data() {
    return {
      card: {
        name: '',
        inventory_number: '',
        author: '',
        image: null,
        country: '',
        creation_year: '',
        is_year_exact: false,
        description: '',
      },
      foundationId: this.$route.params.fond_id, // Get the foundation ID from the route parameter
    };
  },
  methods: {
    createCard() {
      const formData = new FormData();
      formData.append('name', this.card.name);
      formData.append('inventory_number', this.card.inventory_number);
      formData.append('author', this.card.author);
      formData.append('image', this.card.image);
      formData.append('country', this.card.country);
      formData.append('creation_year', this.card.creation_year);
      formData.append('is_year_exact', this.card.is_year_exact);
      formData.append('description', this.card.description);

      axios.post('http://127.0.0.1:8000/api/cards/create/', formData)
        .then(response => {
          // Create a CardToFoundation object after creating the Card object
          const cardId = response.data.id;
          const cardToFoundationData = {
            card: cardId,
            foundation: this.foundationId,
            start_date: new Date().toISOString().slice(0, 10), // Set the start date to the current date
          };
          axios.post('http://127.0.0.1:8000/api/card-to-foundation/', cardToFoundationData)
            .then(response => {
              // Redirect to the newly created card detail page
              this.$router.push({ name: 'CardDetail', params: { id: cardId } });
            })
            .catch(error => {
              console.log(error);
            });
        })
        .catch(error => {
          console.log(error);
        });
    },
    onFileChange(event) {
      this.card.image = event.target.files[0];
    },
  },
};
</script>

<style scoped>
.card-create {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 10px;
  font-weight: bold;
}

input[type="text"],
input[type="number"],
textarea {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  margin-bottom: 20px;
}

input[type="checkbox"] {
  margin-right: 10px;
}

button[type="submit"] {
  background-color: #0074D9;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
}
</style>