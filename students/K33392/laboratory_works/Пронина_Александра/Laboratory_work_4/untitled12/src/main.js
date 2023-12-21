import { createApp } from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import router from './router'; // Импортируйте ваш роутер из соответствующего файла
import store from './store'; // Импортируйте ваше хранилище из соответствующего файла

const app = createApp(App);
app.use(router); // Используйте ваш роутер
app.use(vuetify);
app.use(store); // Используйте ваше хранилище
app.mount('#app');