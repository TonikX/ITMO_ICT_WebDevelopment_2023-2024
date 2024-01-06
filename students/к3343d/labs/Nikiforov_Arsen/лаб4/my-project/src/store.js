import { createStore } from 'vuex';

export default createStore({
  state: {
    user: null, // Состояние пользователя
  },
  mutations: {
    setUser(state, userData) {
      state.user = userData; // Установка данных пользователя
    },
    
    clearUser(state) {
      state.user = {}; // очищаем данные пользователя
    },
  },
  actions: {
    logout({ commit }) {
      commit('clearUser'); // Вызов мутации для очистки пользователя
      
    }
  },
  getters: {
    isAuthenticated: state => !!state.user, // Проверка аутентификации
    user: state => state.user, // Получение данных пользователя
  },
});
