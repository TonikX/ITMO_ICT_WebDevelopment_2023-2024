import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    profileData: {},
  },
  mutations: {
    setProfileData(state, data) {
      state.profileData = data;
    },
  },
});
