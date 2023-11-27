<script setup>
import LogAuthBase from '../components/LogAuthBase.vue'
import LoginForm from '../components/forms/LoginForm.vue'
</script>

<template>
  <log-auth-base card_title="Log into the account"
                 bottom_msg="Don't have an account?"
                 bottom_button_title="Sign Up"
                 bottom_button_href="/register">
    <login-form/>
  </log-auth-base>
</template>

