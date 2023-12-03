<template>
  <q-page padding>
    <template v-if="user">
      <div class="text-h5">{{ user.first_name }} {{ user.last_name }} ({{ user.username }})</div>
      <div>
        <q-icon name="phone" />
        {{ user.phone_number }}
      </div>
      <div>
        <q-icon name="email" />
        {{ user.email }}
      </div>
      <div>
        <q-icon name="place" />
        {{ user.location }}
      </div>
      <div>
        <q-icon name="event" />
        {{ date.formatDate(user.birth_date, 'YYYY-MM-DD') }}
      </div>
    </template>

    <q-btn
      color="primary"
      class="q-my-md q-mr-md"
      @click="openFormPassword"
    >
      Change password
    </q-btn>
    <q-btn
      color="primary"
      class="q-my-md q-mr-md"
      @click="openForm"
    >
      Change profile's data
    </q-btn>
    <q-btn
      v-if="formIsOpen != null"
      color="primary"
      class="q-my-md"
      @click="formIsOpen = null"
    >
      Close
    </q-btn>

    <q-form
      v-if="formIsOpen === 1"
      class="q-gutter-sm"
      @submit="changePassword"
    >
      <q-input
        v-model="formfieldsPassword.new_password"
        filled
        label="New password *"
        type="password"
        lazy-rules
        :rules="[val => val && val.length > 0 || 'Required']"
      />
      <q-input
        v-model="formfieldsPassword.current_password"
        filled
        label="Current password *"
        type="password"
        lazy-rules
        :rules="[val => val && val.length > 0 || 'Required']"
      />


      <div>
        <q-btn
          label="Submit"
          type="submit"
          color="primary"
        />
      </div>
    </q-form>

    <q-form
      v-if="formIsOpen === 2"
      class="q-gutter-sm"
      @submit="changeProfile"
    >
      <q-input
        v-model="formfieldsProfile.first_name"
        filled
        label="First name *"
        lazy-rules
        :rules="[val => val && val.length > 0 || 'Required']"
      />
      <q-input
        v-model="formfieldsProfile.last_name"
        filled
        label="Last name *"
        lazy-rules
        :rules="[val => val && val.length > 0 || 'Required']"
      />
      <q-input
        v-model="formfieldsProfile.phone_number"
        filled
        label="Phone number *"
        lazy-rules
        name="phone"
        :rules="[val => val && val.length > 0 || 'Required']"
      />
      <q-input
        v-model="formfieldsProfile.email"
        filled
        label="Email *"
        lazy-rules
        name="email"
        :rules="[val => val && val.length > 0 || 'Required']"
      />
      <q-input
        v-model="formfieldsProfile.birth_date"
        filled
        label="Date of Birth *"
        lazy-rules
        type="date"
        :rules="[val => val && val.length > 0 || 'Required']"
      />
      <q-input
        v-model="formfieldsProfile.location"
        filled
        label="Location *"
        lazy-rules
        name="city"
        :rules="[val => val && val.length > 0 || 'Required']"
      />


      <div>
        <q-btn
          label="Submit"
          type="submit"
          color="primary"
        />
      </div>
    </q-form>
  </q-page>
</template>
  
<script>
import { reactive, ref } from 'vue'
import { useUserStore } from '../stores/user'
import { storeToRefs } from 'pinia'
import { date } from 'quasar'

export default {
  setup() {
    const userStore = useUserStore()
    const { user } = storeToRefs(userStore)

    const formIsOpen = ref(null)

    const formfieldsProfile = reactive({
      'first_name': null,
      'last_name': null,
      'phone_number': null,
      'email': null,
      'birth_date': null,
      'location': null
    })

    const formfieldsPassword = reactive({
      'new_password': null,
      'current_password': null
    })

    const openForm = () => {
      formIsOpen.value = 2
      formfieldsProfile.first_name = user.value.first_name
      formfieldsProfile.last_name = user.value.last_name
      formfieldsProfile.phone_number = user.value.phone_number
      formfieldsProfile.email = user.value.email
      formfieldsProfile.location = user.value.location
      formfieldsProfile.birth_date = user.value.birth_date
    }

    const openFormPassword = () => {
      formIsOpen.value = 1
      formfieldsPassword.new_password = null
      formfieldsPassword.current_password = null
    }

    const changeProfile = async () => {
      const res = await userStore.updateProfile(formfieldsProfile)
      if (res) {
        formIsOpen.value = null
      }
    }

    const changePassword = async () => {
      const res = await userStore.updatePassword(formfieldsPassword)
      if (res) {
        formIsOpen.value = null
      }
    }

    return {
      formfieldsPassword,
      date,
      user,
      formIsOpen,
      formfieldsProfile,
      openForm,
      changeProfile,
      changePassword,
      openFormPassword
    }
  }
}
</script>
  