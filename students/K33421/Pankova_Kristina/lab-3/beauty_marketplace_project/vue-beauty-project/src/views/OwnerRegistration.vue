<template>
  <div class="app">
      <user-component></user-component>
      <h1 class="title">Sign up: </h1>
    <registration-owner-form class="form" />
  </div>
</template>

<style>

.app {
  font-family: Arial, sans-serif;
  padding: 20px;
}

.title {
  color: #333;
  font-size: 24px;
  margin-bottom: 20px;
}

.button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.form {
  margin-bottom: 20px;
}

.list {
  border: 1px solid #ccc;
  padding: 10px;
}
</style>

<script>
import RegistrationOwnerForm from "@/components/RegistrationOwnerForm.vue";
import UserComponent from '@/components/UserComponent.vue';
import axios from "axios";

export default {
 components: {
   RegistrationOwnerForm, UserComponent
 },
}
</script>

