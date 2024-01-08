<template>
    <UserComponent />
  <div>
    <div v-if="!showComponent">
      <button @click="showSignIn">Sign in</button>
      <button @click="showSignUp">Sign up</button>
      <button @click="showSalons">Show Salons</button>

    </div>

    <div v-if="showComponent === 'signIn'">
      <SignIn />
    </div>

    <div v-if="showComponent === 'signUp'">
      <SignUpChoice />
    </div>

    <div v-if="showComponent === 'salons'">
      <Salons />
    </div>


    <button v-if="showComponent" @click="goBack">Go back</button>
  </div>
</template>

<style>
button {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  margin: 5px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

</style>

<script>
import SignIn from './SignIn.vue';
import SignUpChoice from './SignUpChoice.vue';
import UserComponent from './UserComponent.vue';
import Salons from '@/views/Salons.vue';

export default {
  components: {
    SignIn,
    SignUpChoice,
    UserComponent,
    Salons
  },
  data() {
    return {
      showComponent: null
    };
  },
  methods: {
    showSignIn() {
      this.showComponent = 'signIn';
    },
    showSignUp() {
      this.showComponent = 'signUp';
    },
    showSalons() {
      this.showComponent = 'salons';
    },

    goBack() {
      this.showComponent = null;
    }
  }
};
</script>
