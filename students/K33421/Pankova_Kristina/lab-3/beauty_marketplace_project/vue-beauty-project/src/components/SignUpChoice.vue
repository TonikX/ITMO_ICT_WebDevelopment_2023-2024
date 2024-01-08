<template>
  <div>
    <div v-if="!showForm">
      <p>Are you a customer or a business owner?</p>
      <button @click="showCustomerForm">I am a customer</button>
      <button @click="showOwnerForm">I am an owner</button>
    </div>

    <RegistrationCustomerForm v-if="showForm === 'customer'" />
    <RegistrationOwnerForm v-if="showForm === 'owner'" />
  </div>
</template>

<script>
import RegistrationCustomerForm from './RegistrationCustomerForm.vue';
import RegistrationOwnerForm from './RegistrationOwnerForm.vue';

export default {
  components: {
    RegistrationCustomerForm,
    RegistrationOwnerForm
  },
  data() {
    return {
      showForm: null
    };
  },
  methods: {
    showCustomerForm() {
      this.showForm = 'customer';
    },
    showOwnerForm() {
      this.showForm = 'owner';
    }
  }
};
</script>
