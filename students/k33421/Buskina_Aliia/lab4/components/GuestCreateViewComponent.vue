<template>
  <div class="guest-create">
    <h2>Create Guest</h2>
    <form @submit.prevent="createGuest">
      <label for="name">Name:</label>
      <input type="text" v-model="name" required />

      <label for="surname">Surname:</label>
      <input type="text" v-model="surname" required />

      <label for="hometown">Hometown:</label>
      <input type="text" v-model="hometown" required />

      <button type="submit">Create Guest</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      surname: '',
      hometown: '',
    };
  },
  methods: {
    async createGuest() {
      try {
        await this.$http.post('http://127.0.0.1:8000/api/create_guest/', {
          name: this.name,
          surname: this.surname,
          hometown: this.hometown,
        });
        alert('Guest created successfully!');
      } catch (error) {
        console.error('Error creating guest:', error.message || error);
      }
    },
  },
};
</script>

<style scoped>
.guest-create {
  max-width: 400px;
  margin: 0 auto;
}
</style>
