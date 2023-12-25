import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

export default new Vuetify({
    theme: {
        dark: false, // Включить темный режим
        themes: {
            light: {
                primary: '#2196F3', // Цвет основного акцента
                secondary: '#9C27B0', // Цвет вторичного акцента
                accent: '#FFC107', // Цвет акцента
                error: '#FF5252', // Цвет ошибки
                info: '#2196F3', // Цвет информации
                success: '#4CAF50', // Цвет успешного выполнения
                warning: '#FFC107', // Цвет предупреждения
            },
            dark: {
                primary: '#2196F3',
                secondary: '#9C27B0',
                accent: '#FFC107',
            },
        },
    },

    fonts: {
        family: 'Roboto',
    },
});
