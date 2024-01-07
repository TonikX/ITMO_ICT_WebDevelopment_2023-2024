import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';  

import '@coreui/coreui/dist/css/coreui.min.css'
import "bootstrap/dist/css/bootstrap.min.css";

const app = createApp(App);

app.config.globalProperties.$axios = axios;
app.use(router);

app.mount('#app');
