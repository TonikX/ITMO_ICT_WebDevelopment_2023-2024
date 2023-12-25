# Лабораторная работа 4
## Цель лабораторной работы
Овладеть практическими навыками и умениями реализации клиентской части приложения средствами vue.js.
##Практическое задание
Порядок выполнения работы:
* Реализовать интерфейсы авторизации, регистрации и изменения учётных данных и настроить взаимодействие с серверной частью
* Реализовать клиентские интерфейсы и настроить взаимодействие с серверной частью
* Подключить vuetify или аналогичную библиотеку
##Описание работы (вариант 2)
Создать программную систему, предназначенную для работников библиотеки. Такая система должна обеспечивать хранение сведений об имеющихся в библиотеке книгах, о читателях библиотеки и читальных залах.

Для каждой книги в БД должны храниться следующие сведения: название книги, автор (ы), издательство, год издания, раздел, число экземпляров этой книги в каждом зале библиотеки, а также шифр книги и дата закрепления книги за читателем. Книги могут перерегистрироваться в другом зале.

## Реализация функционала
- Регистрация и авторизация от имени библиотекаря.
- Изменение данных (ФИО) библиотекаря.
- Просмотр всех книг.
- Просмотр всех экземпляров книг
- Закрепление книги за читателем.
- Открепление книги от читателя.

#### Homeview.vue
    <template>
      <v-app>
        <bar-layout>
          <v-btn v-if="auth" @click="LK()"
                 text
          > Личный кабинет
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn v-if="auth" @click="Books()"
                 text
          > Книги
          </v-btn>
          <v-btn v-if="auth" @click="goLogout()"
                 text
          > Выход
          </v-btn>
        </bar-layout>
        <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
          <br><br>
          <HomePage/>
        </v-main>
      </v-app>
    </template>
    
    <script>
    import BarLayout from '@/layouts/BarLayout.vue'
    import HomePage from '@/components/HomePage.vue'
    
    export default {
      name: 'HomeView',
      components: {BarLayout, HomePage},
      computed: {
        auth() {
          var auth
          if (localStorage.auth_token) {
            auth = true
          }
          return auth
        }
      },
      methods: {
        goLogout() {
          localStorage.clear()
          this.$router.push({name: 'Login'})
        },
        Books() {
          this.$router.push({name: 'Books'})
        },
        LK() {
          this.$router.push({name: 'Manager'})
        },
      }
    }
    </script>
    
#### Loginview.vue
    <template>
        <v-app>
          <bar-layout>
              <LoginBar />
            </bar-layout>
            <v-main class = "vh-100" style = "background-color: hsl(0, 0%, 96%);">
            <br><br><br><br><br>
            <h1 style="text-align: center;" > Вход в учетную запись  </h1>
            <br>
            <v-col cols="4" class="mx-auto">
            <v-card max-width = 600 color = "#f7f4ef">
              <v-row class = "py-2">
                <v-col cols="5" class="mx-auto">
                  <v-text-field
                    label="Username"
                    v-model="username"
                    name="username"
                    placeholder="username"
                  />
                </v-col>
                </v-row>
              <v-row>
                <v-col cols="5" class="mx-auto">
                  <v-text-field
                    label="Password"
                    v-model="password"
                    name="password"
                    type = password
                  />
                </v-col>
              </v-row>
              <v-col cols="5" class="mx-auto">
              <v-btn block color = "blue" @click.prevent = "login()"> Войти </v-btn>
              </v-col>
            </v-card>
          </v-col>
            </v-main>
            </v-app>
      </template>
      
      <script>
      import BarLayout from '@/layouts/BarLayout.vue'
      import LoginBar from '@/components/LoginBar.vue'
      import axios from 'axios'
      export default {
        name: 'LogIn',
        components:{ BarLayout, LoginBar},
        data () { 
              return {
                      username: '',
                      password: '',
                  }
          
              }
            ,
            methods: {
        async login() {
            const response = await axios.post('http://127.0.0.1:8000/auth/token/login/',
                  {
                    username: this.username,
                    password: this.password,
                  })
            if (response.data.auth_token) {
                localStorage.auth_token = response.data.auth_token
                window.location = '/home'
                
            }
              }
        
            }
          }
      </script>

#### Registrationview.vue
    <template>
      <v-app>
        <bar-layout>
          <RegistrationBar/>
        </bar-layout>
        <main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
          <br><br><br><br><br>
          <h1 style="text-align: center;"> Регистрация библиотекарей </h1>
          <br>
          <v-col cols="6" class="mx-auto">
            <v-card max-width=800 color="#f7f4ef">
              <v-row class="py-2">
                <v-col cols="5" class="mx-auto">
                  <v-text-field
                    label="Логин"
                    v-model="signUpForm.username"
                    name="username"
                    placeholder="maria211"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="5" class="mx-auto">
                  <v-text-field
                    label="Имя"
                    v-model="signUpForm.first_name"
                    name="first_name"
                    placeholder="Мария"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="5" class="mx-auto">
                  <v-text-field
                    label="Фамилия"
                    v-model="signUpForm.last_name"
                    name="last_name"
                    placeholder="Антонова"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="5" class="mx-auto">
                  <v-text-field
                    label="Password"
                    v-model="signUpForm.password"
                    name="password"
                    type=password
                  />
                </v-col>
              </v-row>
              <v-col cols="5" class="mx-auto">
                <v-btn block color="blue" @click.prevent="register()"> Register</v-btn>
              </v-col>
            </v-card>
          </v-col>
        </main>
      </v-app>
    </template>
    
    <script>
    import BarLayout from '@/layouts/BarLayout.vue'
    import RegistrationBar from '@/components/RegistrationBar.vue'
    import axios from 'axios'
    
    export default {
      name: 'SignUp',
      components: {BarLayout, RegistrationBar},
      data: () => ({
        signUpForm: {
          username: '',
          password: '',
          first_name: '',
          last_name: ''
        }
      }),
      methods: {
        async register() {
          try {
            await axios.post('http://127.0.0.1:8000/users/', this.signUpForm)
            this.$router.push({name: 'Login'})
          } catch (e) {
            if (e.response.data.non_field_errors) {
              alert(e.response.data.non_field_errors)
            } else if (e.response.data.username) {
              alert('Логин: ' + e.response.data.username)
            } else if (e.response.data.password) {
              alert('Пароль: ' + e.response.data.password)
            } else if (e.response.data.first_name) {
              alert('Имя: ' + e.response.data.first_name)
            } else if (e.response.data.last_name) {
              alert('Фамилия: ' + e.response.data.last_name)
            } else {
              console.error(e.message)
            }
    
          }
        }
      }
    }
    </script>

#### Booksview.vue
    <template>
      <section>
        <v-app>
          <bar-layout>
            <AllBooks/>
          </bar-layout>
          <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
            <v-row class="mx-3.5">
              <v-col cols="4" class="mx-auto">
                <br><br>
                <div>
                  <h2>Каталог библиотеки</h2>
                  <v-card elevation="5"
                          outlined
                          class="my-2"
                          v-for="book in books" v-bind:key="book" v-bind:book="book">
                    <a @click.prevent="goBook(book.id)">{{ book.name }}</a>
                  </v-card>
                </div>
              </v-col>
            </v-row>
          </v-main>
        </v-app>
      </section>
    </template>
    
    <script>
    import BarLayout from '@/layouts/BarLayout.vue'
    import AllBooks from '@/components/AllBooks.vue'
    import axios from 'axios'
    
    export default {
      name: 'BookList',
      data() {
        return {
          books: ''
        }
      },
      created() {
        this.loadBooks()
      },
      components: {BarLayout, AllBooks},
    
      methods: {
        async loadBooks() {
          const response = await axios.get('http://127.0.0.1:8000/library/books/list/')
          this.books = response.data
        },
        goBook(bookID) {
    
          this.$router.push({name: 'Book', params: {id: bookID}})
        },
      }
    }
    </script>

####Bookview.vue
    <template>
      <section>
        <v-app>
          <bar-layout>
            <OneBook/>
          </bar-layout>
          <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
            <v-row class="mx-3.5">
              <v-col cols="5" class="mx-auto">
                <br><br>
                <div>
                  <v-card
                    v-if="book"
                    elevation="2"
                    outlined
                    class="my-5"
                  >
                    <v-card-title>
                      <h2>{{ this.book.title }}</h2>
                    </v-card-title>
    
                    <v-card-text>
                      <div class="text--primary">
                        <b>Авторы:</b> {{ this.book.author }}<br>
                        <b>Издательство:</b> {{ this.book.publisher }} <br>
                        <b>Библиотечный номер:</b> {{ this.book.id }} <br>
                        <br>
                        <b>Экземпляры книги:</b>
                        <ul>
                          <li v-for="book_instance in this.book.book_instances" v-bind:key="book_instance"
                              v-bind:book_instance="book_instance">
    
                            <b>Год издания:</b> {{ book_instance.year }}<br>
                            <b>Секция:</b> {{ book_instance.section }}<br>
                            <b>Артикул:</b> {{ book_instance.code }}<br>
                            <v-btn v-if="!book_instance.takenId" color="primary" light
                                   @click="onSelectReader(book_instance.id)">Выдать книгу
                            </v-btn>
                            <v-card
                              v-else
                              elevation="2"
                              outlined
                              class="my-2">
                              <v-card-text>
                                <div class="text--primary">Книга сейчас читается</div>
                              </v-card-text>
                              <v-spacer></v-spacer>
                              <v-btn block color="red" light @click="onReturnBook(book_instance)">Вернуть книгу в библиотеку</v-btn>
                            </v-card>
                            <br>
                          </li>
                        </ul>
                      </div>
                    </v-card-text>
                  </v-card>
    
    
                </div>
              </v-col>
            </v-row>
          </v-main>
        </v-app>
      </section>
      <v-dialog v-if="givingBook" :model-value="true" @close="givingBook = null">
        <div style="padding: 20px">
          <v-card>
            <v-list density="compact">
              <v-list-subheader>Читатели</v-list-subheader>
              <select v-model="givingBook.reader" style="outline: 1px solid black">
                <option disabled :value="null">Выберите читателя</option>
                <option
                  v-for="r in readers"
                  :key="r.id"
                  :value="r"
                >
                  {{ r.name }}
                </option>
              </select>
            </v-list>
            <v-spacer></v-spacer>
            <div v-if="givingBook.reader">
              <v-btn color="primary" @click="onGivingBook">Выдать</v-btn>
            </div>
          </v-card>
        </div>
      </v-dialog>
    </template>
    
    
    <script>
    import BarLayout from '@/layouts/BarLayout.vue'
    import OneBook from '@/components/OneBook.vue'
    import axios from 'axios'
    import {th} from "vuetify/locale";
    
    export default {
      name: 'BookView',
      components: {BarLayout, OneBook},
      data() {
        return {
          book: null,
          readers: null,
          takenBooks: null,
          givingBook: null,
          bookInstancesById: {}
        }
      },
      async created() {
        [this.book, this.takenBooks] = await Promise.all([
          axios.get('http://127.0.0.1:8000/library/books/' + this.$route.params.id).then(r => r.data),
          axios.get('http://127.0.0.1:8000/library/taking_book/list/').then(r => r.data)
        ])
        for (const item of this.book.book_instances) {
          item.takenId = null
          this.bookInstancesById[item.id] = item
        }
        for (const tb of this.takenBooks) {
          if (this.bookInstancesById[tb.book_instance]) {
            this.bookInstancesById[tb.book_instance].takenId = tb.id
          }
        }
      },
      methods: {
        async onReturnBook(book_instance) {
          await axios.delete('http://127.0.0.1:8000/library/taking_book/' + book_instance.takenId)
          book_instance.takenId = null
        },
        async onSelectReader(bookId) {
          if (!this.readers) {
            const response = await axios.get('http://127.0.0.1:8000/library/readers/list/')
            this.readers = response.data
          }
          this.givingBook = {
            bookId,
            reader: null
          }
        },
        async onGivingBook() {
          const date = new Date()
          const pad = (n) => String(n).padStart(2, '0')
          const ymd = `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}`
          const response = await axios.post('http://127.0.0.1:8000/library/taking_book/', {
            book_instance: this.givingBook.bookId,
            reader: this.givingBook.reader.id,
            data_issue: ymd
          }).then(r => r.data)
          this.bookInstancesById[response.book_instance].takenId = response.id
          this.givingBook = null
        }
      }
    }
    </script>


#### ManagerInfoview.vue
    <template>
      <v-app>
        <bar-layout>
          <ManagerInfo/>
        </bar-layout>
        <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
          <v-row class="mx-3.5">
            <v-col cols="4" class="mx-auto">
              <br><br>
              <div>
                <v-card
                  elevation="2"
                  outlined
                  class="my-2"
                >
                  <v-card-title>
                    <h2>Личный кабинет</h2>
                  </v-card-title>
    
                  <v-card-text>
                    <div class="text--primary">
                      <b>Имя:</b> {{ this.manager.first_name }} <br>
                      <b>Фамилия:</b> {{ this.manager.last_name }} <br>
                      <b>Логин:</b> {{ this.manager.username }} <br>
                    </div>
                  </v-card-text>
                </v-card>
                <v-btn block color="green" light @click.prevent="goEdit">Редактировать профиль</v-btn>
              </div>
            </v-col>
          </v-row>
        </v-main>
      </v-app>
    </template>
    
    <script>
    import BarLayout from '@/layouts/BarLayout.vue'
    import ManagerInfo from '@/components/ManagerInfo.vue'
    import axios from 'axios'
    
    export default {
      name: 'ManagerLK',
      components: {BarLayout, ManagerInfo: ManagerInfo},
      data() {
        return {
          manager: {}
        }
      },
      created() {
        this.loadManagerData()
      },
      methods: {
        async loadManagerData() {
          const response = await axios
            .get('http://127.0.0.1:8000/users/me/', {
              headers: {
                Authorization: `Token ${localStorage.auth_token}`
              }
            })
          this.manager = response.data
        },
        goEdit() {
          this.$router.push({name: 'EditManager'})
        }
      }
    }
    </script>


##Вывод
В рамках данной лабораторной работы были получены навыки по реализации клиентской части приложения средствами vue.js. Был получен опыт по реализации клиентской части библиотеки.
