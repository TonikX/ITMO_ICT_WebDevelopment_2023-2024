<template>
  <div class="hire-staff">
    <h2>Hire Staff</h2>
    <form @submit.prevent="hireStaff">
      <label for="name">Name:</label>
      <input type="text" v-model="name" required />

      <label for="surname">Surname:</label>
      <input type="text" v-model="surname" required />

      <button type="submit">Hire Staff</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      surname: '',
    };
  },
  methods: {
    async hireStaff() {
      try {
        await this.$http.post('http://127.0.0.1:8000/api/hire_staff/', {
          name: this.name,
          surname: this.surname,
        });
        alert('Staff hired successfully!');
      } catch (error) {
        console.error('Error hiring staff:', error.message || error);
      }
    },
  },
};
</script>

<style scoped>
.hire-staff {
  max-width: 400px;
  margin: 0 auto;
}
</style>
