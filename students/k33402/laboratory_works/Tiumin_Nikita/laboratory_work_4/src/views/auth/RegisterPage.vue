<template>
  <div class="container form-container">
    <h2>Register</h2>

    <form>
      <div class="mb-3">
        <label class="form-label">First name</label>
        <input
          type="text"
          name="first_name"
          v-model="user.first_name"
          class="form-control __input"
        >
        <span v-if="errors.first_name" class="form-container__error-message">{{ errors.first_name }}</span>
      </div>
      <div class="mb-3">
        <label class="form-label">Last name</label>
        <input
          type="text"
          name="last_name"
          v-model="user.last_name"
          class="form-control __input"
        >
        <span v-if="errors.last_name" class="form-container__error-message">{{ errors.last_name }}</span>
      </div>
      <div class="mb-3">
        <label class="form-label">Patronymic</label>
        <input
          type="text"
          name="patronymic"
          v-model="user.patronymic"
          class="form-control __input"
        >
        <span v-if="errors.patronymic" class="form-container__error-message">{{ errors.patronymic }}</span>
      </div>
      <div class="mb-3">
        <label class="form-label">Email address</label>
        <input
          type="email"
          name="email"
          v-model="user.email"
          class="form-control __input"
        >
        <span v-if="errors.email" class="form-container__error-message">{{ errors.email }}</span>
      </div>
      <div class="mb-3">
        <label class="form-label">Password</label>
        <input
          type="password"
          name="password"
          v-model="user.password"
          class="form-control __input"
        >
        <span v-if="errors.password" class="form-container__error-message">{{ errors.password }}</span>
      </div>
      <div class="mb-3">
        <label class="form-label">Repeat password</label>
        <input
          type="password"
          name="password_confirm"
          v-model="user.password_confirm"
          class="form-control __input"
        >
        <span v-if="errors.password_confirm" class="form-container__error-message">{{ errors.password_confirm }}</span>
      </div>
      <div class="form-container__buttons">
        <button @click.prevent="register" class="btn form-container__buttons__submit_button">Register</button>
        <a href="/login">Already registered?</a>
      </div>
    </form>
  </div>
</template>

<script>
import { mapStores } from 'pinia'
import useAuthStore from "../../pinia/auth";

export default {
  data: () => ({
    user: {
      first_name: '',
      last_name: '',
      patronymic: '',
      email: '',
      password: '',
      password_confirm: '',
    },
    errors: {
      first_name: '',
      last_name: '',
      patronymic: '',
      email: '',
      password: '',
      password_confirm: '',
    },
  }),

  computed: {
    ...mapStores(useAuthStore),
  },

  methods: {
    register() {
      this.clearErrors()
      let valid = true

      if (this.user.password !== this.user.password_confirm) {
        this.errors.password_confirm = 'Passwords do not match'
        valid = false
      }
      if (!this.user.first_name) {
        this.errors.first_name = 'First name field is required'
        valid = false
      }
      if (!this.user.last_name) {
        this.errors.last_name = 'Last name field is required'
        valid = false
      }
      if (!this.user.email) {
        this.errors.email = 'Email field is required'
        valid = false
      }

      if (!valid) return

      this.authStore.register(this.user)
    },

    clearErrors() {
      for (let el in this.errors) {
        this.errors[el] = ''
      }
    }
  },
}
</script>

<style scoped>
.form-container__error-message {
  color: var(--text-color);
}
</style>