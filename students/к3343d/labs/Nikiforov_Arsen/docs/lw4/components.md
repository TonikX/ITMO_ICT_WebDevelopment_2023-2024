# Основные Vue компоненты проекта управления отелем

## 1. RegistrationPage.vue

### Описание
Этот компонент отвечает за регистрацию новых пользователей в системе управления отелем. Он предоставляет форму, в которую пользователи вводят свои данные для создания новой учетной записи.

### Код

```vue
<template>
  <div>
    <h2>Регистрация</h2>
    <form @submit.prevent="register">
      <div class="input-wrapper">
        <input type="text" v-model="userData.username" placeholder="Имя пользователя">
      </div>
      <div class="input-wrapper">
        <input type="password" v-model="userData.password" placeholder="Пароль">
      </div>
      <button type="submit">Зарегистрироваться</button>
    </form>
    <div v-if="registrationSuccess" class="success-message">
      Регистрация прошла успешно! Теперь вы можете войти.
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userData: {
        username: '',
        email: '',
        password: ''
      },
      registrationSuccess: false,
    };
  },
  methods: {
    async register() {
      // Здесь код для регистрации пользователя
    }
  }
};
</script>

<style scoped>
/* Стили компонента */
</style>
```

### Функциональность
- **Получение данных**: Сбор данных из формы через `v-model`.
- **Регистрация**: Обработка отправки формы и регистрация пользователя.
- **Отображение состояния**: Показ сообщения об успешной регистрации.

## 2. LoginPage.vue

### Описание
Компонент `LoginPage.vue` предоставляет интерфейс для входа в систему. Пользователи могут ввести свое имя пользователя и пароль, чтобы получить доступ к своим аккаунтам.

### Код

```vue
<template>
  <form @submit.prevent="login">
    <h2>Вход</h2>
    <div class="input-wrapper">
      <input type="text" v-model="userData.username" placeholder="Имя пользователя">
    </div>
    <div class="input-wrapper">
      <input type="password" v-model="userData.password" placeholder="Пароль">
    </div>
    <button type="submit">Войти</button>
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
  </form>
</template>

<script>
export default {
  data() {
    return {
      userData: {
        username: '',
        password: '',
      },
      errorMessage: '',
    };
  },
  methods: {
    async login() {
      // Здесь код для входа пользователя
    }
  }
};
</script>

<style scoped>
/* Стили компонента */
</style>
```

### Функциональность
- **Вход**: Аутентификация пользователя и обработка ошибок входа.
- **Управление состоянием**: Отображение сообщений об ошибках.

## 3. UserProfile.vue

### Описание
`UserProfile.vue` - это компонент, который отображает информацию о пользователе и предоставляет интерфейс для управления профилем после входа в систему.

### Код

```vue
<template>
  <div>
    <h2>Добро пожаловать в систему управления отелем, {{ username }}!</h2>
    <div class="navigation-links">
      <!-- Ссылки и кнопки для управления профилем -->
    </div>
    <!-- Контент для отображения информации и управления профилем -->
  </div>
</template>

<script>
export default {
  computed: {
    username() {
      // Возвращает имя текущего пользователя
    }
  },
  methods: {
    // Методы для управления профилем
  }
};
</script>

<style scoped>
/* Стили компонента */
</style>
```

### Функциональность
- **Отображение информации**: Показывает имя пользователя и предоставляет навигационные ссылки.
- **Управление профилем**: Функции для изменения профильной информации или выхода из системы.

Эти три компонента обеспечивают основные функции системы управления отелем, такие как регистрация, вход и управление профилем пользователя.