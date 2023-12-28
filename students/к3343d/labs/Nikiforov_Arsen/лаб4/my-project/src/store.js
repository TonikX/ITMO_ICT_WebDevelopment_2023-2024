import { createStore } from 'vuex';

export default createStore({
  state: {
    user: null,
  },
  mutations: {
    setUser(state, userData) {
      console.log('Updating user data:', userData);
      state.user = userData;
    },
    clearUser(state) {
      state.user = null;
    },
  },
  getters: {
    isAuthenticated: state => !!state.user,
    user: state => state.user,
  },
});



