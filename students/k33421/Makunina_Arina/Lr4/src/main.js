import App from './App.vue';

import { createApp } from 'vue';
import { router, vuetify } from './helpers';
import { createPinia } from 'pinia';
import 'vuetify/dist/vuetify.min.css'

const app = createApp(App);

app.use(createPinia());
app.use(vuetify)
app.use(router);

app.mount('#app');
