# Отчёт по лабораторной работе

**Цель:**  познакомится с базовыми конструкциями JavaScript.

**Оборудование:** компьютерный класс.

## Практическое задание

Порядок выполнения работы:

Я установила поддержку CORS (Cross-Origin Resource Sharing) в Django-проекте, что позволяет веб-серверу безопасно взаимодействовать с фронтендом, находящимся на другом порту.

1. Добавила corsheaders в INSTALLED_APPS.
2. Добавила CorsMiddleware в MIDDLEWARE.
3. Настроила CORS_ALLOWED_ORIGINS.
4. Установила CORS_ALLOW_CREDENTIALS.

![img.png](img.png)
![img_1.png](img_1.png)

### App.vue

#### Описание

Файл `App.vue` представляет собой основной компонент приложения.

#### Структура

```html
<template>
  <router-view />
</template>
```

В данном файле используется главный шаблон `<router-view />`, который предназначен для отображения компонентов в соответствии с текущим маршрутом.

```javascript
<script setup>
  //
</script>
```

В секции `<script setup>` может содержаться настройка логики компонента, однако в данном коде эта секция оставлена пустой.

### main.js

#### Описание

Файл `main.js` является точкой входа в приложение.

#### Зависимости

```javascript
import App from './App.vue';
import { createApp } from 'vue';
import { router, vuetify } from './helpers';
import { createPinia } from 'pinia';
import 'vuetify/dist/vuetify.min.css'
```

Импортируются необходимые зависимости, такие как `App` компонент, библиотека Vue, настройки маршрутизатора (`router`), настройки Vuetify (`vuetify`) и библиотека для управления состоянием приложения с использованием Pinia (`createPinia`).

#### Создание приложения

```javascript
const app = createApp(App);
```

Создается экземпляр приложения с использованием `createApp`, и используется компонент `App`.

#### Использование плагинов

```javascript
app.use(createPinia());
app.use(vuetify)
app.use(router);
```

Подключаются необходимые плагины: Pinia для управления состоянием, Vuetify для стилизации компонентов и маршрутизатор для навигации.

#### Монтирование приложения

```javascript
app.mount('#app');
```

Приложение монтируется в элемент с идентификатором `#app` в DOM.

### auth.store.js

#### Описание

Файл `auth.store.js` содержит определение хранилища состояния и действий для управления аутентификацией в приложении.

#### Зависимости

```javascript
import { defineStore } from 'pinia';
import { fetchWrapper, router } from '@/helpers';
```

Импортируются необходимые зависимости, такие как `defineStore` из библиотеки Pinia и вспомогательные функции `fetchWrapper` и `router`.

#### Базовый URL

```javascript
const baseUrl = `${import.meta.env.VITE_API_URL}`;
```

Устанавливается базовый URL для взаимодействия с сервером. URL берется из переменной окружения `VITE_API_URL`.

#### Определение хранилища

```javascript
export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    access: JSON.parse(localStorage.getItem('access')),
    refresh: JSON.parse(localStorage.getItem('refresh')),
    role: JSON.parse(localStorage.getItem('role')),
  }),
```

Определяется хранилище состояния `useAuthStore` с полями `access`, `refresh` и `role`, которые инициализируются из локального хранилища.

#### Действия (Actions)

##### Метод `login`

```javascript
  actions: {
    async login(username, password) {
      try {
        const data = await fetchWrapper.post(`${baseUrl}/auth/jwt/create/`, {username: username, password: password});
        this.access = data.access;
        this.refresh = data.refresh;

        localStorage.setItem('access', JSON.stringify(data.access));
        localStorage.setItem('refresh', JSON.stringify(data.refresh));

        await router.push('/');
      } catch (error) {
        throw error;
      }
    },
```

Метод `login` выполняет аутентификацию пользователя, отправляя запрос на сервер для получения токенов доступа и обновления. Данные токенов сохраняются в состоянии и локальном хранилище. В случае ошибки, ошибка пробрасывается дальше.

##### Метод `logout`

```javascript
    async logout() {
      this.access = null;
      this.refresh = null;
      this.role = null;

      localStorage.removeItem('access');
      localStorage.removeItem('refresh');
      localStorage.removeItem('role');

      await router.push('/login');
    },
```

Метод `logout` очищает данные о доступе, обновлении и роли пользователя. Сохраненные данные удаляются из локального хранилища, и пользователь перенаправляется на страницу входа.

##### Метод `update_role`

```javascript
    async update_role() {
      const role = await fetchWrapper.get(`${baseUrl}/user/role/`);
      this.role = role.role;

      localStorage.setItem('role', JSON.stringify(role.role));
    }
  }
});
```

Метод `update_role` обновляет роль пользователя, отправляя запрос на сервер. Полученная роль сохраняется в состоянии и локальном хранилище.

### helpers

#### vuetify.js

Описание:
- Файл `vuetify.js` содержит настройки Vuetify для стилизации компонентов приложения.

- Импортируются стили и необходимые компоненты из Vuetify.

- Создается экземпляр Vuetify с определенной цветовой схемой и шрифтом.

#### router.js

```javascript
import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores';
import { LoginComponent, RegisterComponent, ScheduleComponent } from "@/components";
import { DispatcherHome, SubDeanHome, TeachersList, Unauth, GroupList } from "@/views";

const routes = [
  // ... (определение маршрутов)
];

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, from, next) => {
  // ... (обработка переходов между маршрутами)
});

```

Описание:
- Файл `router.js` определяет маршруты и настройки маршрутизатора Vue.

- Используется библиотека Vue Router для управления маршрутизацией.

- Перед каждым переходом проверяется аутентификация пользователя и его роль для обеспечения правильного отображения страниц.

#### fetch-wrapper.js

```javascript
import { useAuthStore } from '@/stores';

export const fetchWrapper = {
  get: request('GET'),
  post: request('POST'),
  put: request('PUT'),
  delete: request('DELETE')
};

const logout = async () => {
  // ... (обработка выхода из системы)
}

function request(method) {
  // ... (формирование HTTP-запроса)
}

async function authHeader(url) {
  // ... (формирование заголовков запроса с учетом аутентификации)
}

async function handleResponse(response) {
  // ... (обработка ответа от сервера)
}
```

Описание:
- Файл `fetch-wrapper.js` содержит утилиту `fetchWrapper` для выполнения HTTP-запросов с использованием токена доступа.

- Внутренние функции обеспечивают формирование заголовков запроса, обработку ответа и выход из системы в случае неудачи.

- Используется хранилище состояния `useAuthStore` для получения информации об аутентификации пользователя.

#### **LoginComponent.vue:**
- Компонент для страницы входа.
- Содержит форму с полями для ввода имени пользователя и пароля.

- Ввод имени пользователя и пароля подвергается валидации.
- Выводит сообщения об ошибках при неверном вводе.

- При успешном вводе осуществляется попытка входа через `authStore`.
- Выводит сообщения об ошибках в случае неудачной попытки.

- Кнопка для перехода на страницу регистрации.

#### **RegisterComponent.vue:**
- Компонент для страницы регистрации.
- Содержит форму с полями для ввода имени пользователя и пароля.

- Ввод имени пользователя и пароля подвергается валидации.
- Выводит сообщения об ошибках при неверном вводе.

- При успешной регистрации осуществляется попытка входа через `authStore`.
- Выводит сообщения об ошибках в случае неудачной попытки.

- Кнопка для перехода на страницу входа.

#### **ScheduleComponent.vue:**
- Компонент для отображения расписания для определенной группы и семестра.
- Позволяет просматривать, добавлять, редактировать и удалять записи в расписании.

- Загружает расписание, данные о временных слотах, аудиториях, предметах и преподавателях с сервера.

- Группирует и отображает расписание по дням недели.
- Позволяет редактировать, удалять и добавлять новые записи в расписание.

#### **DispatcherHome.vue:**
- Главная страница диспетчера.
- Позволяет диспетчеру выбрать группу и семестр для просмотра расписания.

- При выборе группы и семестра диспетчер переходит на страницу расписания для выбранной группы и семестра.

- Отображает расписание с возможностью выбора группы и семестра.
- Позволяет диспетчеру выйти из системы.

#### **SubDeanHome.vue:**
- Главная страница заместителя декана.
- Предоставляет доступ к просмотру списка преподавателей и учебных групп.

- Позволяет заместителю декана перейти к списку преподавателей или учебных групп.
- Позволяет заместителю декана выйти из системы.

#### **GroupList.vue:**
- Компонент для отображения списка групп с возможностью просмотра студентов в каждой группе.

- Загружает список групп с сервера.

- Позволяет просмотреть студентов в каждой группе.
- Отображает средний балл группы.

#### **TeachersList.vue:**
- Компонент для отображения списка преподавателей с возможностью добавления, удаления и просмотра.

- Загружает список преподавателей с сервера.

- Позволяет заместителю декана добавлять новых преподавателей и удалять существующих.

#### **Unauth.vue:**
- Компонент для отображения страницы с сообщением об отсутствии доступа.

- Предлагает вернуться к странице входа при отсутствии необходимых прав.

### Видеоматериалы:

**Интерфейсы:** https://drive.google.com/file/d/1zpHDdmbslCaQwBvVeO1MlLVD9RTLjuYm/view?usp=drivesdk

**Разбор кода:** https://drive.google.com/file/d/1ea5ELxy5yotrJOdFza3gGGvlGvhSXng2/view?usp=drivesdk 