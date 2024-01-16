import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

app.mount('#app')

// import VSpoiler from 'v-spoiler';
// import 'v-spoiler/dist/v-spoiler.css';
// app.component('VSpoiler', VSpoiler);