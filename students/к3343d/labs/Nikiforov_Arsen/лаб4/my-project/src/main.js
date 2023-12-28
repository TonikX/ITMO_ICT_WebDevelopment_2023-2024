import { createApp } from 'vue'; 
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';
import { VueAxios } from 'vue-axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import BootstrapVue3 from 'bootstrap-vue-3';

const app = createApp(App);

axios.defaults.baseURL = 'http://localhost:8000'; // Настройка базового URL

app.use(router);
app.use(store);
app.use(BootstrapVue3);
app.use(VueAxios, axios);

const userToken = localStorage.getItem('userToken');
if (userToken) {
  store.commit('setUser', { token: userToken });
  axios.defaults.headers.common['Authorization'] = `Bearer ${userToken}`;
}

app.mount('#app');
