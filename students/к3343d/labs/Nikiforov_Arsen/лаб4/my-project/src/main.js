import { createApp } from 'vue'; 
import App from './App.vue';
import router from './router';
import store from './store'; //  хранилище Vuex
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import BootstrapVue3 from 'bootstrap-vue-3';
import VueAxios from 'vue-axios';

const app = createApp(App);

app.use(router);
app.use(store); // Vuex в приложении
app.use(BootstrapVue3);
app.use(VueAxios, axios);

// Проверка localStorage на наличие токена и его установка в состояние Vuex
const userToken = localStorage.getItem('userToken');
if (userToken) {
  store.commit('setUser', { token: userToken });
}

app.mount('#app');
