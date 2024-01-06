## store.js

### Описание
`store.js` используется для создания глобального хранилища состояний с помощью Vuex. Это позволяет компонентам приложения обмениваться данными и состояниями.

### Код

```javascript
import { createStore } from 'vuex';

export default createStore({
  state: {
    user: null,
  },
  mutations: {
    setUser(state, userData) {
      state.user = userData;
    },
    clearUser(state) {
      state.user = null;
    },
  },
  getters: {
    isAuthenticated: state => !!state.user,
    user: state => state.user,
  },
});
```

### Функциональность
- **Состояние**: Хранение информации о пользователе.
- **Мутации**: Обновление состояния пользователя.
- **Геттеры**: Получение данных о состоянии аутентификации и пользователя.

