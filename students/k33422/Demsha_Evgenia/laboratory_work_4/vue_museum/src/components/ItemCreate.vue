<template>
  <div class="item-create">
    <h1>Create New Item</h1>
    <form @submit.prevent="createItem">
      <div>
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="item.name" required>
      </div>
      <div>
        <label for="number">Number:</label>
        <input type="number" id="number" v-model="item.number" required>
      </div>
      <div>
        <label for="description">Description:</label>
        <textarea id="description" v-model="item.description"></textarea>
      </div>
      <div>
        <label for="image">Image:</label>
        <input type="file" id="image" @change="onFileChange" accept="image/*">
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
  name: 'ItemCreate',
  data() {
    return {
      item: {
        name: '',
        description: '',
        image: null,
        number: '',
        card: this.$route.query.card,
      },
    };
  },
  methods: {
    createItem() {
      const formData = new FormData();
      formData.append('name', this.item.name);
      formData.append('description', this.item.description);
      formData.append('number', this.item.number);
      formData.append('card', this.item.card);
      formData.append('image', this.item.image);

      axios.post('http://127.0.0.1:8000/api/items/create/', formData)
        .then(() => {
          this.$router.back();
        })
        .catch(error => {
          console.log(error);
        });
    },
    onFileChange(event) {
      this.item.image = event.target.files[0];
    },
  },
};
</script>


<style scoped>

.item-create {
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

input[type="file"] {
  margin-top: 10px;
  margin-bottom: 20px;
}

button[type="submit"] {
  background-color: #0074D9;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
}
</style>

