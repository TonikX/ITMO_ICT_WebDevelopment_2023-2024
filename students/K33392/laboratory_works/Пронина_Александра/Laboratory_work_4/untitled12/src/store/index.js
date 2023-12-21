import { createStore } from 'vuex';

export default createStore({
    state() {
        return {
            isAuthenticated: false, // Переменная для отслеживания аутентификации пользователя
            user: null, // Информация о текущем пользователе
            books: [], // Список книг
            cart: [], // Корзина покупок
            reviews: [], // Список отзывов
            favorites: [], // Избранные книги пользователя
            // Другие переменные состояния, которые вам могут понадобиться
        };
    },
    mutations: {
        // Примеры мутаций для изменения состояния
        SET_AUTHENTICATED(state, isAuthenticated) {
            state.isAuthenticated = isAuthenticated;
        },
        SET_USER(state, user) {
            state.user = user;
        },
        SET_BOOKS(state, books) {
            state.books = books;
        },
        // Другие мутации по мере необходимости
    },
    actions: {
        // Примеры действий для внесения изменений в состояние через мутации
        login({ commit }, userData) {
            // Логика аутентификации, отправка запроса на бэкенд и т.д.
            // Пример использования мутаций для обновления состояния
            commit('SET_AUTHENTICATED', true);
            commit('SET_USER', userData);
        },
        fetchBooks({ commit }) {
            // Логика загрузки списка книг с бэкенда
            // Пример использования мутаций для обновления состояния
            const books = []; // Предположим, что здесь есть данные о книгах с бэкенда
            commit('SET_BOOKS', books);
        },
        // Другие действия по мере необходимости
    },
    modules: {
        // Если ваше приложение требует модульную структуру, вы можете добавить модули здесь
    }
});
