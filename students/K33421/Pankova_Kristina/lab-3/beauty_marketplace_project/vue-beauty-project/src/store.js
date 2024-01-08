// store.js
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isAuthenticated: false,
    user: null
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
           commit('setUser', response.data.user);
         })
         .catch(error => {
           console.error('Login failed', error);
         });
    },
    logout({ commit }) {
      // Make the API call to log out the user
      // If logout is successful, set isAuthenticated to false and clear user data
      // For example:
       axios.post('http://127.0.0.1:8000/salon/api/login/')
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
