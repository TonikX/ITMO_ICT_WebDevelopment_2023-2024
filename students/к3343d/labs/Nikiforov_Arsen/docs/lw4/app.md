## App.vue

### Описание
`App.vue` является корневым компонентом Vue приложения. Он служит в качестве основного контейнера для других компонентов и управляет основной разметкой.

### Код

```vue
<template>
  <div class="app-container">
    <img alt="Vue logo" src="./assets/logo.png" class="logo">
    <div class="menu" v-if="showButtons">
      <h1>Добро пожаловать в наш отель!</h1>
      <button @click="showComponent = 'login'">Вход</button>
      <button @click="showComponent = 'registration'">Регистрация</button>
    </div>
    <LoginPage v-if="showComponent === 'login'" @show-user-profile="showUserProfile" />
    <RegistrationPage v-if="showComponent === 'registration'" />
    <UserProfile v-if="showComponent === 'userProfile'" @go-back="showMainButtons" />
  </div>
</template>

<script>
import RegistrationPage from './components/RegistrationPage.vue';
import LoginPage from './components/LoginPage.vue';
import UserProfile from './components/UserProfile.vue';

export default {
  name: 'App',
  components: {
    RegistrationPage,
    LoginPage,
    UserProfile
  },
  data() {
    return {
      showComponent: null,
      showButtons: true,
    };
  },
  methods: {
    showUserProfile() {
      this.showComponent = 'userProfile';
      this.showButtons = false;
    },
    showMainButtons() {
      this.showComponent = null;
      this.showButtons = true;
    }
  }
};
</script>
```

### Функциональность
- **Контейнер приложения**: Определяет базовую структуру приложения.
- **Router View**: Место для отображения содержимого маршрутов.

![Интерфейс пользователя](../img/lab4.png)
