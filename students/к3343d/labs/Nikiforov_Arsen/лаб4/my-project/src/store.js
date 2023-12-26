import { reactive } from 'vue';

export const state = reactive({
  user: null, // Здесь будут храниться данные о пользователе
});

export const mutations = {
  setUser(state, user) {
    state.user = user;
  },
  clearUser(state) {
    state.user = null;
  }
};
