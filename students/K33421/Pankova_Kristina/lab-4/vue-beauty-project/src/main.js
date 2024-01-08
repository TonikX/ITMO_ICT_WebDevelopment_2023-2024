import { createApp } from 'vue'
import App from './App.vue'
import './assets/main.css'
import router from "./router";
import axios from 'axios';

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})


import { createStore } from 'vuex'

// Create a new store instance.
const store = createStore({
  state: {
    isAuthenticated: false,
    user: ''
  },
  mutations: {
    setAuthentication(state, status) {
      state.isAuthenticated = status;
    },
    setUser(state, user) {
      state.user = user;
    }
  },
  actions: {
    login({ commit }, userData) {
      // Make the API call to authenticate the user
      // If authentication is successful, set isAuthenticated to true and store user data
      // For example:
       axios.post('http://127.0.0.1:8000/salon/api/login/', userData)
         .then(response => {
           commit('setAuthentication', true);
           console.log(response);
           commit('setUser', response.data);
         })
         .catch(error => {
           console.error('Login failed', error);
         });
    },
    logout({ commit }) {
      // Make the API call to log out the user
      // If logout is successful, set isAuthenticated to false and clear user data
      // For example:
       axios.post('http://127.0.0.1:8000/salon/api/logout/')
         .then(() => {
           commit('setAuthentication', false);
           commit('setUser', null);
         })
         .catch(error => {
           console.error('Logout failed', error);
         });
    }
  }
});


createApp(App).use(router).use(store).use(vuetify).mount('#app');



