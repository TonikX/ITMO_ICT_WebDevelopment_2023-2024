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
        :rules="[val => val && val.length > 0 || 'Required']"
      />

      <div>Don't have a profile yet? <q-btn outline size="sm" to="/register">Register</q-btn></div>

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
import { reactive, onMounted } from 'vue'
import { useUserStore } from '../stores/user'
import { useRouter, useRoute } from 'vue-router'

export default {
  setup() {
    const userStore = useUserStore()
    
    const router = useRouter()
    const route = useRoute()

    const formfields = reactive({
      'username': null,
      'password': null
    })

    onMounted(() => {
      if (route.query.username) {
        formfields.username = route.query.username
      }
    })

    return {
      formfields,

      async onSubmit() {
        const res = await userStore.login(formfields)
        if (res) {
          router.push({ path: '/' })
        }
      }
    }
  }
}
</script>
