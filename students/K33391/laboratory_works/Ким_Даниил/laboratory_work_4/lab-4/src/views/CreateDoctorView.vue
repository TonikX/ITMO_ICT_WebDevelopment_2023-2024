<script>
import router from '@/router'
import api from '@/api'
import { useAuthStore } from '@/store/auth'
export default {
  data() {
    this.authStore = useAuthStore()
    return {
      name: '',
      surname: '',
      specialization: '',
      contacts: '',
    }
  },
  methods: {
    create() {
      api
          .post('clinic/doctors/', {
            Name: this.title,
            Surname: this.surname,
            Specialization: this.specialization,
            Contacts: this.contacts
          })
          .then((_) => router.push({ path: '/doctors' }))
          .catch((_) => alert('Failed to create a doctor'))
    },
  },
}
</script>

<template>
  <h2>Create doctor</h2>
  <label for="title">Name</label>
  <br />
  <input type="text" name="name" v-model="name" />
  <br /><br />
  <label for="content">Surname</label>
  <br />
  <textarea name="surname" cols="30" rows="10" v-model="surname"></textarea>
  <br /><br />
  <label for="content">Specialization</label>
  <br />
  <textarea name="specialization" cols="30" rows="10" v-model="specialization"></textarea>
  <br /><br />
  <label for="content">Contacts</label>
  <br />
  <textarea name="contacts" cols="30" rows="10" v-model="contacts"></textarea>
  <br /><br />
  <button v-on:click="create">Create</button>
</template>