## 1. main.js

### Описание
`main.js` - это точка входа в приложение Vue. Он инициализирует приложение Vue и подключает глобальные библиотеки, такие как Vue Router и Vuex Store.

### Код

```javascript
import { createApp } from 'vue'; 
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';
import BootstrapVue3 from 'bootstrap-vue-3';
import VueAxios from 'vue-axios';

const app = createApp(App);

app.use(router);
app.use(store);
app.use(BootstrapVue3);
app.use(VueAxios, axios);

app.mount('#app');
```

### Функциональность
- **Инициализация Vue**: Создает экземпляр Vue приложения.
- **Подключение роутера и хранилища**: Интеграция Vue Router и Vuex для маршрутизации и управления состоянием.
- **Подключение библиотек**: Интеграция BootstrapVue и Axios.

