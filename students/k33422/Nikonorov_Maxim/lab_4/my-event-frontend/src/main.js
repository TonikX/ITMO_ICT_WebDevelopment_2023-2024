import { createApp } from 'vue';
import { createStore } from 'vuex'
import App from './App.vue';
import router from './router';
import axios from 'axios';  

const store = createStore({
    state: {
      isAuthenticated: !!sessionStorage.getItem('token'),
    },
    mutations: {
      setAuthenticated(state, value) {
        state.isAuthenticated = value;
      },
    },
  })

import '@coreui/coreui/dist/css/coreui.min.css'
import "bootstrap/dist/css/bootstrap.min.css";

const app = createApp(App);

app.config.globalProperties.$axios = axios;
app.use(router);

app.use(store).mount('#app');
