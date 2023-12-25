<script>
import router from '@/router'
import api from '@/api'
import { useAuthStore } from '@/store/auth'
export default {
  data() {
    this.authStore = useAuthStore()
    return {
      title: '',
      description: '',
      price: '',
    }
  },
  methods: {
    create() {
      api
          .post('clinic/services/', {
            Name: this.title,
            Description: this.description,
            Price: this.price
          })
          .then((_) => router.push({ path: '/services' }))
          .catch((_) => alert('Failed to create a service'))
    },
  },
}
</script>

<template>
  <h2>Create service</h2>
  <label for="title">Title</label>
  <br />
  <input type="text" name="title" v-model="title" />
  <br /><br />
  <label for="content">Description</label>
  <br />
  <textarea name="description" cols="30" rows="10" v-model="description"></textarea>
  <br /><br />
  <label for="content">Price</label>
  <br />
  <textarea name="price" cols="30" rows="10" v-model="price"></textarea>
  <br /><br />
  <button v-on:click="create">Create</button>
</template>