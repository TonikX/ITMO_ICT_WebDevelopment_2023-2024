## index.js (Router)

### Описание
`index.js` в директории router отвечает за настройку и управление маршрутизацией в приложении Vue с использованием Vue Router.

### Код

```javascript
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import AboutPage from '../components/AboutPage.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/about', component: AboutPage },
  // Другие маршруты...
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
```

### Функциональность
- **Определение маршрутов**: Настройка путей и соответствующих им компонентов.


