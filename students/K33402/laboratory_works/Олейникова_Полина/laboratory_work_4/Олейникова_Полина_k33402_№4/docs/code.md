## example form: create\update book
```
<template>
    <q-dialog
        ref="dialogRef"
        @hide="onDialogHide"
    >
        <q-card class="q-dialog-plugin">
            <q-card-section>
                <q-input
                    v-model="formfields.title"
                    filled
                    label="Title *"
                    lazy-rules
                    :rules="[val => val && val.length > 0 || 'Required']"
                />
                <q-input
                    v-model="formfields.author"
                    filled
                    label="Author *"
                    lazy-rules
                    :rules="[val => val && val.length > 0 || 'Required']"
                />
                <q-input
                    v-model="formfields.description"
                    filled
                    label="Description *"
                    lazy-rules
                    type="textarea"
                    :rules="[val => val && val.length > 0 || 'Required']"
                />
            </q-card-section>

            <q-card-actions align="right">
                <q-btn
                    color="primary"
                    label="OK"
                    @click="onSubmit"
                />
                <q-btn
                    color="primary"
                    label="Cancel"
                    @click="onCancelClick"
                />
            </q-card-actions>
        </q-card>
    </q-dialog>
</template>
  
<script>
import { reactive, onMounted } from 'vue'
import { useDialogPluginComponent } from 'quasar'
import { useBooksStore } from '../stores/books'

export default {
    props: {
        book: {
            type: Object,
            default: () => null
        },
        getBooks: {
            type: Function,
            default: () => { }
        }
    },

    emits: [
        ...useDialogPluginComponent.emits
    ],

    setup(props) {
        const { dialogRef, onDialogHide, onDialogCancel } = useDialogPluginComponent()

        const booksStore = useBooksStore()

        const formfields = reactive({
            'title': null,
            'author': null,
            'description': null
        })

        onMounted(() => {
            if (props.book) {
                formfields.title = props.book.title
                formfields.author = props.book.author
                formfields.description = props.book.description
            }
        })

        const onSubmit = async () => {
            let res = false
            if (props.book) {
                res = await booksStore.updateBook({ ...formfields, id: props.book.id })
            } else {
                res = await booksStore.addBook(formfields)
            }
            if (res) {
                props.getBooks()
                onDialogHide()
            }
        }

        return {
            formfields,
            onSubmit,

            dialogRef,
            onDialogHide,
            onCancelClick: onDialogCancel
        }
    }
}
</script>
```

## create instance axios

```
import axios from 'axios'
import { useUserStore } from '../stores/user'
import { errorHandler } from '../helpers/errorHandler'

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    headers: {
        'Content-type': 'application/json',
        'X-CSRFToken': 'oOdoOuaBF1xkIfVsP5PdGomSFnguDuybCWrtyJmYV3lHsGAnHtkTynEhwDRfDM3Z'
    }
})

api.interceptors.request.use(
    config => {
        const userStore = useUserStore()
        const { token } = userStore
        if (token) {
            config.headers['Authorization'] = `Token ${token}`
        }
        return config
    }
)

api.interceptors.response.use(
    response => response,
    error => {
        errorHandler(error)
        return Promise.reject(error)
    }
)

export { api }
```

## main.js with ui library connection
```
import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { Quasar, Notify, Dialog } from 'quasar'

// Import icon libraries
import '@quasar/extras/material-icons/material-icons.css'

// Import Quasar css
import 'quasar/src/css/index.sass'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(Quasar, { plugins: { Notify, Dialog } })
app.mount('#app')

```