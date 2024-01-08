import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: !!sessionStorage.getItem('token'),
  },
  mutations: {
    setAuthenticated(state, value) {
      state.isAuthenticated = value;
    },
  },
})