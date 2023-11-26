<script setup>
import LogAuthBase from '../components/LogAuthBase.vue'
import RegistrationFields from '../components/forms/RegistrationForm.vue'
</script>

<template>
  <log-auth-base card_title="Create an account"
                 bottom_msg="Already have an account?"
                 bottom_button_title="Sign In"
                 bottom_button_href="/login">
    <registration-fields/>
  </log-auth-base>
</template>
