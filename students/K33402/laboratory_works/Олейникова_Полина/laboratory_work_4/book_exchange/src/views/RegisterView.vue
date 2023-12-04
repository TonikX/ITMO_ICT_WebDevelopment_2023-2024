<template>
  <q-page
    padding
    class="flex justify-center"
  >
    <q-form
      class="q-gutter-sm full-width"
      style="max-width: 400px"
      @submit="onSubmit"
    >
      <q-input
        v-model="formfields.username"
        filled
        label="Username *"
        lazy-rules
        :rules="[val => val && val.length > 0 || 'Required']"
      />
      <q-input
        v-model="formfields.password"
        filled
        label="Password *"
        lazy-rules
        type="password"
        :rules="[val => val && val.length > 7 || 'Minimum 8 characters']"
      />
      <q-input
        v-model="formfields.first_name"
        filled
        label="First name *"
        lazy-rules
        :rules="[val => val && val.length > 0 || 'Required']"
      />
      <q-input
        v-model="formfields.last_name"
        filled
        label="Last name *"
        lazy-rules
        :rules="[val => val && val.length > 0 || 'Required']"
      />
      <q-input
        v-model="formfields.phone_number"
        filled
        label="Phone number *"
        lazy-rules
        name="phone"
        :rules="[val => val && val.length > 0 || 'Required']"
      />
      <q-input
        v-model="formfields.email"
        filled
        label="Email *"
        lazy-rules
        name="email"
        :rules="[val => val && val.length > 0 || 'Required']"
      />
      <q-input
        v-model="formfields.birth_date"
        filled
        label="Date of Birth *"
        lazy-rules
        type="date"
        :rules="[val => val && val.length > 0 || 'Required']"
      />
      <q-input
        v-model="formfields.location"
        filled
        label="Location *"
        lazy-rules
        name="city"
        :rules="[val => val && val.length > 0 || 'Required']"
      />

      <div>Already have a profile? <q-btn outline size="sm" to="/login">Login</q-btn></div>


      <div>
        <q-btn
          label="Submit"
          type="submit"
          color="primary"
          class="full-width"
        />
      </div>
    </q-form>
  </q-page>
</template>

<script>
import { reactive } from 'vue'
import { useUserStore } from '../stores/user'
import { useRouter } from 'vue-router'

export default {
  setup() {
    const userStore = useUserStore()
    const router = useRouter()

    const formfields = reactive({
      'first_name': null,
      'last_name': null,
      'phone_number': null,
      'email': null,
      'birth_date': null,
      'location': null,
      'username': null,
      'password': null
    })

    return {
      formfields,

      async onSubmit() {
        const res = await userStore.register(formfields)
        if (res) {
          router.push({ path: '/login', query: { username: formfields.username } })
        }
      }
    }
  }
}
</script>
