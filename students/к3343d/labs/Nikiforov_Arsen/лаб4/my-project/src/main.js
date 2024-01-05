import { createApp } from 'vue'; 
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import BootstrapVue3 from 'bootstrap-vue-3';
import VueAxios from 'vue-axios';
import { createVuetify } from 'vuetify';
import 'vuetify/styles';

const app = createApp(App);
const vuetify = createVuetify();

app.use(router);
app.use(store);
app.use(BootstrapVue3);
app.use(VueAxios, axios);
app.use(vuetify);

const userToken = localStorage.getItem('userToken');
if (userToken) {
  store.commit('setUser', { token: userToken });
}

app.mount('#app');
