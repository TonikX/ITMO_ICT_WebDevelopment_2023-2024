# Компоненты

### Работа с пользователем

#### Логин

```
<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  username: '',
  password: ''
})

function login(){
  instance.post('/system/login/', form.value).then(response => {
    if (response.status === 200){
      Token.setToken(response.data.access)
      router.push('/newspapers')
    }
  }
  ).catch(error => console.log(error))
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Вход</h2>
    <v-text-field label="Логин" v-model="form.username"></v-text-field>
    <v-text-field label="Пароль" v-model="form.password"></v-text-field>
    <v-btn @click="login">Войти</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```


#### Регистрация
```
<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";

const form = ref({
  username: '',
  type: '',
  password: '',
  password2: ''
})

function register(){
  instance.post('/system/register/', form.value).then(response => {
        if (response.status === 201){
          router.push('/newspapers')
        }
      }
  ).catch(error => console.log(error))
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Регистрация</h2>
      <v-text-field label="Логин" v-model="form.username"></v-text-field>
      <v-select
          label="Тип"
          v-model="form.type"
          :items="['A', 'P', 'PO', 'N']"
      ></v-select>
      <v-text-field label="Пароль" v-model="form.password"></v-text-field>
      <v-text-field label="Повторите пароль" v-model="form.password2"></v-text-field>
      <v-btn @click="register">Зарегистрироваться</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```

### Газета
#### Добавление 
```
<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  name: "",
  index: "",
  redactor_last_name: "",
  redactor_first_name: "",
  redactor_patronic: "",
  cost: 0
})

function create(){
  instance.post('/system/newspaper/', form.value, {
    headers: {
      'Authorization': `${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/newspapers')
        }
      }
  ).catch(error => console.log(error))
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить газету</h2>
      <v-text-field label="Имя" v-model="form.name"></v-text-field>
      <v-text-field label="Номер" v-model="form.index"></v-text-field>
      <v-text-field label="Фамилия редактора" v-model="form.redactor_last_name"></v-text-field>
      <v-text-field label="Имя редактора" v-model="form.redactor_first_name"></v-text-field>
      <v-text-field label="Отчество редактора" v-model="form.redactor_patronic"></v-text-field>
      <v-text-field label="Цена" v-model="form.cost"></v-text-field>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```

#### Список/удаление 
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const newspapers = ref([])

function getNewspapers(){
  instance.get('/system/newspaper/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          newspapers.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteNewspaper(id){
  instance.delete(`/system/newspaper/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getNewspapers()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getNewspapers()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Газеты</h2>
    <v-btn @click="router.push('/find-price/')">
      Найти по стоимости
    </v-btn>

    <template v-for="newspaper in newspapers" :key="newspaper.id">
    <v-card
        width="400"
        :title="`${newspaper.name} (id: ${newspaper.id})`"
        :subtitle="`${newspaper.redactor_last_name} ${newspaper.redactor_first_name} ${newspaper.redactor_patronic}`"
        :text="`Цена ${newspaper.cost}`"
    ><v-card-actions>
      <v-btn @click="router.push('/newspapers/' + newspaper.id)">
        Изменить
      </v-btn>
      <v-btn @click="deleteNewspaper(newspaper.id)">
        Удалить
      </v-btn>
    </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-newspaper')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>

```
#### Отображение 
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  name: "",
  index: "",
  redactor_last_name: "",
  redactor_first_name: "",
  redactor_patronic: "",
  cost: 0
})

function getPaper(){
  instance.get(`/system/newspaper/${router.currentRoute.value.params.id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          form.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function savePaper(){
  const {id, ...rest} = form.value
  instance.patch(`/system/newspaper/${router.currentRoute.value.params.id}/`, rest, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          router.push('/newspapers')
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {
  getPaper()
})

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Газета</h2>
      <v-text-field label="Имя" v-model="form.name"></v-text-field>
      <v-text-field label="Номер" v-model="form.index"></v-text-field>
      <v-text-field label="Фамилия редактора" v-model="form.redactor_last_name"></v-text-field>
      <v-text-field label="Имя редактора" v-model="form.redactor_first_name"></v-text-field>
      <v-text-field label="Отчество редактора" v-model="form.redactor_patronic"></v-text-field>
      <v-text-field label="Цена" v-model="form.cost"></v-text-field>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```
#### Поиск по стоимости
```
<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref('')
const addresses = ref()

function create(){
  instance.post('/system/do/more-expensive-newspapers/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          addresses.value = response.data
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Найти по цене</h2>
      <v-text-field label="Цена" v-model="form"></v-text-field>
      <v-btn @click="create">Найти</v-btn>
    </div>
    <div v-if="error" class="text-red">
      Не найдено
    </div>
    <div v-else-if="addresses">
      <template v-for="printed in addresses" :key="printed">
        <v-card
            width="400"
            :title="printed.newspaper.name"
            :subtitle="`${printed.newspaper.redactor_last_name} ${printed.newspaper.redactor_first_name} ${printed.newspaper.redactor_patronic}`"
            :text="`Цена ${printed.newspaper.cost}`"
        >
          <v-card-actions>
            <v-btn>
              Отделение: {{ printed.post_office.num }}
            </v-btn>
          </v-card-actions>
        </v-card>
      </template>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```

### Почта
#### Добавление 
```
<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  num: "",
  address: "",
})

function create(){
  instance.post('/system/post-office/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/post-offices')
        }
      }
  ).catch(error => console.log(error))
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить отделение</h2>
      <v-text-field label="Номер" v-model="form.num"></v-text-field>
      <v-text-field label="Адресс" v-model="form.address"></v-text-field>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```

#### Список/удаление 
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const newspapers = ref([])

function getNewspapers(){
  instance.get('/system/post-office/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          newspapers.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteNewspaper(id){
  instance.delete(`/system/post-office/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getNewspapers()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getNewspapers()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Почтовые отделения</h2>
    <template v-for="newspaper in newspapers" :key="newspaper.id">
      <v-card
          width="400"
          :title="`№ ${newspaper.num} (id: ${newspaper.id})`"
          :text="`Адрес: ${newspaper.address}`"
      ><v-card-actions>
        <v-btn @click="router.push('/post-offices/' + newspaper.id)">
          Изменить
        </v-btn>
        <v-btn @click="deleteNewspaper(newspaper.id)">
          Удалить
        </v-btn>
      </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-post-office')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>

```
#### Отображение 
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  num: "",
  address: "",
})

function getPaper(){
  instance.get(`/system/post-office/${router.currentRoute.value.params.id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          form.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function savePaper(){
  const {id, ...rest} = form.value
  instance.patch(`/system/post-office/${router.currentRoute.value.params.id}/`, rest, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          router.push('/newspapers')
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {
  getPaper()
})

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Почтовое отделение</h2>
      <v-text-field label="Номер" v-model="form.num"></v-text-field>
      <v-text-field label="Адресс" v-model="form.address"></v-text-field>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```

### Типография

#### Добавление 
```
<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  name: "",
  address: "",
  max_capacity: "",
})

function create(){
  instance.post('/system/printer/', form.value,{
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/printers')
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить типографию</h2>
      <v-text-field label="Имя" v-model="form.name"></v-text-field>
      <v-text-field label="Адресс" v-model="form.address"></v-text-field>
      <v-text-field label="Максимальная производительность" v-model="form.max_capacity"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```

#### Список/удаление 
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const newspapers = ref([])

function getNewspapers(){
  instance.get('/system/printer/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          newspapers.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteNewspaper(id){
  instance.delete(`/system/printer/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getNewspapers()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getNewspapers()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Типографии</h2>
    <template v-for="newspaper in newspapers" :key="newspaper.id">
    <v-card
        width="400"
        :title="`${newspaper.name} (id: ${newspaper.id})`"
        :subtitle="`Адресс: ${newspaper.address}`"
        :text="`Максимальная производительность ${newspaper.max_capacity}`"
    ><v-card-actions>
      <v-btn @click="router.push('/printers/' + newspaper.id)">
        Изменить
      </v-btn>
      <v-btn @click="router.push('/printers/' + newspaper.id + '/report')">
        Смотреть отчет
      </v-btn>
      <v-btn @click="deleteNewspaper(newspaper.id)">
        Удалить
      </v-btn>
    </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-printer')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>

```
#### Отображение 
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  name: "",
  address: "",
  max_capacity: "",
})

function getPaper(){
  instance.get(`/system/printer/${router.currentRoute.value.params.id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          form.value = response.data
        }
      }
  ).catch(e => error.value = true )
}

function savePaper(){
  const {id, ...rest} = form.value
  instance.patch(`/system/printer/${router.currentRoute.value.params.id}/`, rest, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          router.push('/newspapers')
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {
  getPaper()
})

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Типография</h2>
      <v-text-field label="Имя" v-model="form.name"></v-text-field>
      <v-text-field label="Адрес" v-model="form.address"></v-text-field>
      <v-text-field label="Максимальная производительность" v-model="form.max_capacity"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```
#### Отчет
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)
const printer = ref(null)

function find() {
  instance.get(`/system/do/${router.currentRoute.value.params.id}/report/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200) {
          printer.value = response.data
        }
      }
  ).catch(e => error.value = true)
}

onMounted(() => {
  find()
})

</script>

<template>
  <v-app>
    <h2 class="w-50 mx-auto">Отчет о деятельности типографии</h2>
    <div class="w-50 mx-auto d-flex">
    </div>
    <div v-if="error" class="w-50 mx-auto">
      Данные не найдены
    </div>
    <div v-else-if="printer" class="w-50 mx-auto d-flex flex-column ga-4">
      <v-card
          class=""
          width="400"
      >
        <template v-slot:title>
          Самый продаваемый редактор
        </template>
        <v-card-text>
          {{ printer["most-sold-redactor"].redactor_last_name + ' ' + printer["most-sold-redactor"].redactor_first_name + ' ' + printer["most-sold-redactor"].redactor_patronic }}
        </v-card-text>
      </v-card>
      <v-card
          class=""
          width="400"
      >
        <template v-slot:title>
          Издаваемых газет:
        </template>
        <v-card-text>
          {{ printer.printed_here }}
        </v-card-text>
      </v-card>
      <h2>Что печатается</h2>
      <template v-for="printed in printer.show_printed" :key="printed.id">
        <v-card
            width="400"
            :title="printed.newspaper.name"
            :subtitle="`${printed.newspaper.redactor_last_name} ${printed.newspaper.redactor_first_name} ${printed.newspaper.redactor_patronic}`"
            :text="`Цена ${printed.newspaper.cost}`"
        >
          <v-card-actions>
            <v-btn>
              Количество: {{ printed.how_many_to_print }}
            </v-btn>
          </v-card-actions>
        </v-card>
      </template>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```
#### Поиск адресов
```
<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref('')
const addresses = ref()

function create(){
  instance.post('/system/do/find-addresses/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          addresses.value = response.data
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Найти адрес печати</h2>
      <v-text-field label="Название газеты" v-model="form"></v-text-field>
      <v-btn @click="create">Найти</v-btn>
    </div>
    <div v-if="error" class="text-red">
      Не найдено
    </div>
    <div v-else-if="addresses">
      <template v-for="address in addresses" :key="address">
        <v-card
            width="400"
            :title="address.address"
        ></v-card>
      </template>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```

### Печать газеты
#### Добавление 
```
<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  how_many_to_print: "",
  newspaper: "",
  printer: "",
})

function create(){
  instance.post('/system/printing-newspapers/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/printing')
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить печать</h2>
      <v-text-field label="Газета" v-model="form.newspaper"></v-text-field>
      <v-text-field label="Типография" v-model="form.printer"></v-text-field>
      <v-text-field label="Сколько печатать" v-model="form.how_many_to_print"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```

#### Список/удаление 
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const newspapers = ref([])

function getNewspapers(){
  instance.get('/system/printing-newspapers/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          newspapers.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteNewspaper(id){
  instance.delete(`/system/printing-newspapers/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getNewspapers()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getNewspapers()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Печати</h2>

    <v-btn @click="router.push('/find-where')">Найти поступления</v-btn>
    <v-btn @click="router.push('/find-address')">Найти, где издется газета</v-btn>

    <template v-for="newspaper in newspapers" :key="newspaper.id">
    <v-card
        width="400"
        :title="`(id: ${newspaper.id})`"
        :subtitle="`Газета: ${newspaper.newspaper.name}, Типография: ${newspaper.printer.address}`"
        :text="`Сколько печатать: ${newspaper.how_many_to_print}`"
    ><v-card-actions>
      <v-btn @click="router.push('/printing/' + newspaper.id)">
        Изменить
      </v-btn>
      <v-btn @click="deleteNewspaper(newspaper.id)">
        Удалить
      </v-btn>
    </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-printing')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>

```
#### Отображение 
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  how_many_to_print: "",
  newspaper: "",
  printer: "",
})

function getPaper(){
  instance.get(`/system/printing-newspapers/${router.currentRoute.value.params.id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          form.value = response.data
        }
      }
  ).catch(e => error.value = true )
}

function savePaper(){
  const {id, ...rest} = form.value
  instance.patch(`/system/printing-newspapers/${router.currentRoute.value.params.id}/`, rest, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          router.push('/printing')
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {
  getPaper()
})

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Печать</h2>
      <v-text-field label="Газета" v-model="form.newspaper"></v-text-field>
      <v-text-field label="Типография" v-model="form.printer"></v-text-field>
      <v-text-field label="Сколько печатать" v-model="form.how_many_to_print"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```
#### Где продается
```
<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  name:'',
  where_printed:''
})
const addresses = ref()

function create(){
  instance.post('/system/do/where-to-sell/', form.value,{
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          addresses.value = response.data
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Найти куда поступает</h2>
      <v-text-field label="Название газеты" v-model="form.name"></v-text-field>
      <v-text-field label="Где печатается" v-model="form.where_printed"></v-text-field>
      <v-btn @click="create">Найти</v-btn>
    </div>
    <div v-if="error" class="text-red">
      Не найдено
    </div>
    <div v-else-if="addresses">
        <v-card
            width="400"
            :title="`Отделение № ${addresses?.post_office_order.post_office.num}`"
        ></v-card>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```

### Заказ почты
#### Добавление 
```
<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";
import {tr} from "vuetify/locale";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  how_many_needed: "",
  newspaper: "",
  post_office: "",
})

function create(){
  error.value = false
  instance.post('/system/ordering-newspapers/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/orders')
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Создать заказ</h2>
      <v-text-field label="Отделение" v-model="form.post_office"></v-text-field>
      <v-text-field label="Газета" v-model="form.newspaper"></v-text-field>
      <v-text-field label="Сколько нужно" v-model="form.how_many_needed"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```

#### Список/удаление 
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const newspapers = ref([])

function getNewspapers(){
  instance.get('/system/ordering-newspapers/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          newspapers.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteNewspaper(id){
  instance.delete(`/system/ordering-newspapers/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getNewspapers()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getNewspapers()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Заказы</h2>
    <template v-for="newspaper in newspapers" :key="newspaper.id">
    <v-card
        width="400"
        :title="` (id: ${newspaper.id})`"
        :subtitle="`Почтовое отделение: ${newspaper.post_office}, Газета: ${newspaper.newspaper}`"
        :text="`Сколько нужно: ${newspaper.how_many_needed}`"
    ><v-card-actions>
      <v-btn @click="router.push('/newspapers/' + newspaper.id)">
        Изменить
      </v-btn>
      <v-btn @click="deleteNewspaper(newspaper.id)">
        Удалить
      </v-btn>
    </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-order')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>

```
#### Отображение 
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  name: "",
  index: "",
  redactor_last_name: "",
  redactor_first_name: "",
  redactor_patronic: "",
  cost: 0
})

function getPaper(){
  instance.get(`/system/newspaper/${router.currentRoute.value.params.id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          form.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function savePaper(){
  const {id, ...rest} = form.value
  instance.patch(`/system/newspaper/${router.currentRoute.value.params.id}/`, rest, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          router.push('/newspapers')
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {
  getPaper()
})

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Заказ</h2>
      <v-text-field label="Имя" v-model="form.name"></v-text-field>
      <v-text-field label="Номер" v-model="form.index"></v-text-field>
      <v-text-field label="Фамилия редактора" v-model="form.redactor_last_name"></v-text-field>
      <v-text-field label="Имя редактора" v-model="form.redactor_first_name"></v-text-field>
      <v-text-field label="Отчество редактора" v-model="form.redactor_patronic"></v-text-field>
      <v-text-field label="Цена" v-model="form.cost"></v-text-field>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```
### Доставка
#### Добавление 
```
<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  amount: "",
  printing_newspaper: "",
  post_office_order: "",
})

function create(){
  instance.post('/system/transporting/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/transporting')
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить перевозку</h2>
      <v-text-field label="Заказ" v-model="form.post_office_order"></v-text-field>
      <v-text-field label="Печть" v-model="form.printing_newspaper"></v-text-field>
      <v-text-field label="Количество" v-model="form.amount"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```

#### Список/удаление 
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const newspapers = ref([])

function getNewspapers(){
  instance.get('/system/transporting/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          newspapers.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteNewspaper(id){
  instance.delete(`/system/transporting/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getNewspapers()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getNewspapers()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Перевозки</h2>
    <v-btn @click="router.push('/lost-delivers')">Посмотреть список незакрытых заказов</v-btn>
    <template v-for="newspaper in newspapers" :key="newspaper.id">
    <v-card
        width="400"
        :title="`(id: ${newspaper.id})`"
        :subtitle="`Заказ: ${newspaper.post_office_order.id}, Печать: ${newspaper.printing_newspaper.id}`"
        :text="`Количество: ${newspaper.amount}`"
    ><v-card-actions>
      <v-btn @click="router.push('/transporting/' + newspaper.id)">
        Изменить
      </v-btn>
      <v-btn @click="deleteNewspaper(newspaper.id)">
        Удалить
      </v-btn>
    </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-transporting')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>

```
#### Отображение 
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  amount: "",
  printing_newspaper: "",
  post_office_order: "",
})

function getPaper(){
  instance.get(`/system/transporting/${router.currentRoute.value.params.id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          form.value = response.data
        }
      }
  ).catch(e => error.value = true )
}

function savePaper(){
  const {id, ...rest} = form.value
  instance.patch(`/system/transporting/${router.currentRoute.value.params.id}/`, rest, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          router.push('/transporting')
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {
  getPaper()
})

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Перевозка</h2>
      <v-text-field label="Заказ" v-model="form.post_office_order"></v-text-field>
      <v-text-field label="Печать" v-model="form.printing_newspaper"></v-text-field>
      <v-text-field label="Количество" v-model="form.amount"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

```

#### Поиск недостачь по заказам
```
<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const delivers = ref([])

function getDelivers(){
  instance.get('/system/do/lost-delivers/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          delivers.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getDelivers()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Список поставок</h2>
    <template v-for="deliver in delivers" :key="deliver.id">
      <v-card
          width="400"
          :title="deliver.id"
          :subtitle="`Отделение почты: ${deliver.post_office}`"
          :text="`Газета: ${deliver.newspaper}`"
      ><v-card-actions>
      </v-card-actions></v-card>
    </template>
  </div>
</template>

<style scoped>
</style>

```
