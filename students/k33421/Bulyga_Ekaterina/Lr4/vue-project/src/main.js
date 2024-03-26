import {createApp} from 'vue'
import {createPinia} from 'pinia'
import App from './App.vue'
import router from './router'
import {useMainStore} from '@/stores/main.js'
import Axios from 'axios'
import stores from './stores'

import './css/main.css'

// Init Pinia
const pinia = createPinia()

// Create Vue app
createApp(App).use(pinia).use(router).use(stores).mount('#app')

// Init main store
const mainStore = useMainStore(pinia)

// Fetch sample data
// mainStore.fetchSampleClients()
// mainStore.fetchSampleHistory()

// Dark mode
// Uncomment, if you'd like to restore persisted darkMode setting, or use `prefers-color-scheme: dark`. Make sure to uncomment localStorage block in src/stores/darkMode.js
import {useDarkModeStore} from './stores/darkMode'

const darkModeStore = useDarkModeStore(pinia);

if (localStorage['darkMode'] === '1') {
  darkModeStore.set(true)
} else {
  darkModeStore.set(false)
}

// Default title tag
const defaultDocumentTitle = 'Страхование'

// Set document title from route meta
router.afterEach((to) => {
  document.title = to.meta?.title
    ? `${to.meta.title} — ${defaultDocumentTitle}`
    : defaultDocumentTitle
})
