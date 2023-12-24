# Лабораторная работа 4

## Задание
Реализация клиентской части приложения средствами vue.js.

## Решение

### main.js

Создадим наше приложение, подключив к нему роутер и pinia для state management

```js
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const pinia = createPinia()
const app = createApp(App)
app.use(pinia)
app.use(router)

app.mount('#app')
```

### store/index.js
Создадим глобальное хранилище для пользовательских данных.
Нам они понадобятся для реализации входа, регистрации и профиля пользователя.

Для данной лабораторной работы нам понадобится хранение и получение пароля, имени пользователя и электронной почты

```js
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({ password: localStorage.getItem("password"), username: localStorage.getItem("username"), token: localStorage.getItem("auth_token") }),
  getters: {
    userData: (state) => state
  },
  actions: {
    login(username, password, token) {
      this.username = username
      this.password = password
      this.token = token
      localStorage.setItem("auth_token", token)
      localStorage.setItem("username", username)
      localStorage.setItem("password", password)
    }
  }
})
```

### api/index.js
Так как наш backend использует авторизацию при помощи токенов нам необходимо
добавить функцию, которая будет перед отправкой запроса добавлять `Authorization` header 
с токеном пользователя.

Я выбрал axios в качестве библиотеки для HTTP запросов
```js
import axios from 'axios'
const instance = axios.create({
  baseURL: 'http://localhost:8080',
  headers: {
    'Content-Type': 'application/json'
  },
})
instance.interceptors.request.use(function (cfg) {
  const authToken = localStorage.getItem("auth_token")
  if (authToken !== null && authToken !== "undefined") {
    cfg.headers.Authorization = `Token ${authToken}`

  }
  return cfg
}, function (error) {
  return Promise.reject(error)
})
export default instance
```

### views/AuthView.vue
В представлении страницы для авторизации нам необходимо реализовать два метода - один для входа, а другой для регистрации.
```js
<script>
import api from '@/api'
import router from '@/router'
import { useAuthStore } from '@/store/auth'
export default {
  data() {
    this.authStore = useAuthStore()
    return {
      signupData: {
        email: '',
        username: '',
        password: '',
      },
      loginData: {
        email: '',
        username: '',
        password: '',
      },
    }
  },
  methods: {
    login() {
      api
        .post('auth/token/login', {
          username: this.loginData.username,
          password: this.loginData.password,
        })
        .then((resp) => resp.data)
        .then((data) => {
          this.authStore.login(
            this.loginData.username,
            this.loginData.password,
            data.auth_token
          )
          router.push({ path: '/profile' })
        })
    },
    signup() {
      api
        .post('api/users/', {
          email: this.signupData.email,
          username: this.signupData.username,
          password: this.signupData.password,
        })
        .then((resp) => resp.data)
        .then((data) => {
          this.authStore.login(
            this.signupData.username,
            this.signupData.password,
            data.auth_token
          )
          router.push({ path: '/profile' })
        })
    },
  },
}
</script>

<template>
  <div class="login">
    <h3>Login</h3>
    <label for="username">Username</label>
    <input type="text" name="username" v-model="loginData.username" />
    <br />
    <br />
    <label for="password">Password</label>
    <input type="password" name="password" v-model="loginData.password" />
    <br />
    <br />
    <button v-on:click="login">Login</button>
  </div>
  <div class="signup">
    <h3>Sign Up</h3>
    <label for="email">Email</label>
    <input type="text" name="email" v-model="signupData.email" />
    <br />
    <br />
    <label for="username">Username</label>
    <input type="text" name="username" v-model="signupData.username" />
    <br />
    <br />
    <label for="password">Password</label>
    <input type="password" name="password" v-model="signupData.password" />
    <br />
    <br />
    <button v-on:click="signup">Sign Up</button>
  </div>
</template>
```

### views/ProfileView.vue

Далее нам необходимо реализовать представление для профиля пользователя, в котором
можно будет изменять данные пользователя.

Для начала нам необходимо добавить новый ViewSet на нашем сервере, чтобы 
мы могли получать данные о пользователе не только при помощи ключа, но и
при помощи имени пользователя

```python
class UsernameViewSet(viewsets.ViewSet):
  def partial_update(self, req:Request, pk=None):
    queryset = User.objects.all()
    user = get_object_or_404(queryset, username=pk)
    user.__dict__.update(req.data)
    user.save()
    return Response()
  def retrieve(self, _, pk=None):
    queryset = User.objects.all()
    serializer = MyUserSerializer(get_object_or_404(queryset, username=pk))
    return Response(serializer.data)
```

После этого можно реализовать логику обращения к серверу и отображения данных на странице.
Метод beforeMount вызывается прямо перед подключением компонента
```js
<script>
import { useAuthStore } from '@/store/auth'
import router from '@/router'
import api from '@/api'
export default {
  data() {
    this.authStore = useAuthStore()
    if (this.authStore.userData.username === '') {
      router.push({ path: '/auth' })
      return
    }
    this.authStore.userData.email = ''
    this.authStore.userData.bio = ''
    return this.authStore.userData
  },
  methods: {
    updateUserData() {
      api.patch(`api/username/${this.username}/`, {
        email: this.email,
        username: this.username,
        bio: this.bio,
      })
    },
  },

  beforeMount() {
    api
      .get(`api/username/${this.username}`)
      .then((resp) => resp.data)
      .then((data) => {
        console.log(data)
        this.username = data.username
        this.email = data.email
        this.bio = data.bio
      })
  },
}
</script>

<template>
  <div class="userInfo">
    <label for="username">Username</label>
    <br />
    <input type="text" name="username" v-model="username" />
    <br /><br />
    <label for="email">Email</label>
    <br />
    <input type="email" name="email" v-model="email" />
    <br /><br />
    <label for="bio">Bio</label>
    <br />
    <textarea name="bio" cols="30" rows="3" v-model="bio"></textarea>
    <br /><br />
    <button v-on:click="updateUserData">Update</button>
  </div>
</template>

<style scoped>
.userInfo {
  padding-top: 20px;
}
</style>
```

### views/PostsView.vue
Создадим представление для публикаций пользователей
```js
<script>
import api from '@/api'
import Post from '@/components/Post.vue'
import router from '@/router'
export default {
  data() {
    return { posts: [] }
  },
  components: {
    Post,
  },
  methods: {
    getPosts() {
      api
        .get('api/posts/')
        .then((resp) => resp.data)
        .then((data) => (this.posts = data))
        .catch(() => alert('Failed to fetch posts'))
    },
    newPost() {
      router.push({ path: '/newpost' })
    },
  },
  beforeMount() {
    this.getPosts()
  },
}
</script>

<template>
  <br />
  <button v-on:click="newPost">New post</button>
  <ol class="posts">
    <Post v-for="post in posts" :post="post" :key="post.id" />
  </ol>
</template>
```

В данном представлении мы используем компонент `Post.vue`, который выглядит следующим образом

```js
<script>
import router from '@/router'
export default {
  name: 'post',
  props: ['post'],
  methods: {
    openPost() {
      router.push({ path: `/posts/${this.post.id}` })
    },
  },
}
</script>

<template>
  <li class="post" v-on:click="openPost">
    <h3>{{ post.title }}</h3>
    <p>by {{ post.author.username }} at {{ post.created_at }}</p>
  </li>
</template>

<style scoped>
.post {
  cursor: pointer;
}
</style>
```

### views/PostView.vue

Также, на каждый пост можно нажать и посмотреть его содержание и комментарии.
Для этого нам необходимо создать представление
```js
<script>
import api from '@/api'
import CommentsView from './CommentsView.vue'
export default {
  data() {
    return { post: { id: this.$route.params.id, title: '', content: '' } }
  },
  beforeMount() {
    api
      .get(`api/posts/${this.post.id}`)
      .then((resp) => resp.data)
      .then((data) => (this.post = data))
      .catch((_) => alert('Failed to fetch post'))
  },
  components: [CommentsView],
  components: { CommentsView },
}
</script>

<template>
  <h1>{{ post.title }}</h1>
  <textarea name="content" cols="30" rows="10" readonly>{{
    post.content
  }}</textarea>
  <CommentsView :post="post" />
</template>
```

### views/CommentsView.vue
У каждого поста есть список комментарием, которые определен представлением
```js
<script>
import api from '@/api'
import router from '@/router'
import Comment from '@/components/Comment.vue'
import { RouterLink } from 'vue-router'
export default {
  props: ['post'],
  data() {
    return { post: this.$props.post, comments: [] }
  },
  methods: {
    newComment() {
      router.push({ path: `/posts/${this.post.id}/newcomment` })
    },
  },
  beforeMount() {
    api
      .get(`api/post_comments/${this.post.id}`)
      .then((resp) => resp.data)
      .then((data) => (this.comments = data))
      .catch((_) => alert('Failed to fetch comments'))
  },
  components: [Comment],
  components: { Comment, RouterLink },
}
</script>

<template>
  <h3>Comments</h3>
  <button v-on:click="newComment">New comment</button>
  <Comment v-for="comment in comments" :comment="comment" :key="comment.id" />
</template>
```