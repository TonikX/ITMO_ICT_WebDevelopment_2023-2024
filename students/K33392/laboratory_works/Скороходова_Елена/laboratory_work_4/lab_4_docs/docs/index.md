##Main

Этот код представляет собой точку входа в приложение.
Здесь происходит импорт функции createApp для создания экземпляра приложения Vue.
Также импорт компонента App из файла App.vue - корневой компонент приложения, 
импорт объекта маршрутизатора из файла router, импорт функции createVuetify из библиотеки Vuetify, 
импорт стилей Vuetify из файла vuetify.min.css.

Далее создается экземпляр приложения с использованием функции createApp, передавая ей компонент App, 
создается экземпляр Vuetify с использованием функции createVuetify. 
Подключаем маршрутизатор к корневому экземпляру Vue.
Монтируем приложение в DOM элемент с идентификатором #app. 
Это запускает приложение Vue и отображает его в указанном DOM элементе.


    import { createApp } from 'vue';
    import App from './App.vue';
    import router from './router';
    import { createVuetify } from 'vuetify';
    import 'vuetify/dist/vuetify.min.css';
    
    const app = createApp(App);
    
    const vuetify = createVuetify();
    
    app.use(router);
    app.use(vuetify);
    app.mount('#app');
