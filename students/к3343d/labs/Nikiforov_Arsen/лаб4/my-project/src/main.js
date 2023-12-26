import { createApp } from 'vue'; 
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';
import { VueAxios } from 'vue-axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import BootstrapVue3 from 'bootstrap-vue-3';

// Создание экземпляра приложения
const app = createApp(App);

// Использование плагинов
app.use(router);
app.use(store);
app.use(BootstrapVue3); // Использование BootstrapVue3 для Vue 3
app.use(VueAxios, axios);

// Монтирование приложения
app.mount('#app');
