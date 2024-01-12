Здесь я оставлю только код с комментариями, ибо описывать весь функционал крайне долго и муторно.

About.vue
    
    <template>
      <div class="about">
        <h1>(Здесь может быть описание книжного магазина)
        </h1>
      <h3> </h3>
    <h3>Интернет-магазин «Книжный в Нижнем» – один из ведущих в Нижнем книжных магазинов. Здесь вы можете купить книги всех направлений и стилей по выгодным ценам с бесплатной доставкой!
    
      </h3>
      </div>
    </template>

Cart.vue

    <template>
        <!-- Основной контейнер страницы корзины -->
        <div class="page-cart">
            <!-- Обертка для колонок в многоколоночной сетке -->
            <div class="columns is-multiline">
                <!-- Заголовок страницы -->
                <div class="column is-12">
                    <h1 class="title">Корзина</h1>
                </div>
    
                <!-- Блок с товарами в корзине -->
                <div class="column is-12 box">
                    <!-- Таблица для отображения товаров в корзине, отображается только если в корзине есть товары -->
                    <table class="table is-fullwidth" v-if="cartTotalLength">
                        <thead>
                            <!-- Заголовки столбцов таблицы -->
                            <tr>
                                <th>Товар</th>
                                <th>Цена</th>
                                <th>Количество</th>
                                <th>Итого</th>
                                <th></th>
                            </tr>
                        </thead>
    
                        <tbody>
                            <!-- Компонент CartItem используется для отображения каждого товара в корзине -->
                            <CartItem
                                v-for="item in cart.items"
                                v-bind:key="item.product.id"
                                v-bind:initialItem="item"
                                v-on:removeFromCart="removeFromCart" />
                        </tbody>
                    </table>
    
                    <!-- Сообщение, отображаемое, если корзина пуста -->
                    <p v-else>Ничего нет в корзине...</p>
                </div>
    
                <!-- Блок с общей информацией о корзине и кнопкой для перехода к оформлению заказа -->
                <div class="column is-12 box">
                    <h2 class="subtitle">Итого</h2>
    
                    <!-- Отображение общей стоимости и количества товаров в корзине -->
                    <strong>{{ cartTotalPrice.toFixed(2) }}руб</strong>, {{ cartTotalLength }} единиц(а)
    
                    <hr>
    
                    <!-- Кнопка для перехода к оформлению заказа -->
                    <router-link to="/cart/checkout" class="button is-dark">Далее</router-link>
                </div>
            </div>
        </div>
    </template>
    
    <script>
    import axios from 'axios'
    import CartItem from '@/components/CartItem.vue'
    import { reactive } from 'vue';
    
    export default {
        name: 'Cart',  // Название компонента
        components: {
            CartItem  // Регистрация компонента CartItem
        },
        data() {
            return {
                cart: {
                    items: []
                }
            }
        },
        mounted() {
           // this.cart = reactive(this.$store.state.cart);
           this. cart = this.$store.state.cart;
    
        },
        methods: {
            // Метод для удаления товара из корзины
            removeFromCart(item) {
                this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
            }
        },
        computed: {
            // Вычисляемое свойство для общего количества товаров в корзине
            cartTotalLength() {
                return this.cart.items.reduce((acc, curVal) => {
                    return acc += curVal.quantity
                }, 0)
            },
            // Вычисляемое свойство для общей стоимости товаров в корзине
            cartTotalPrice() {
                return this.cart.items.reduce((acc, curVal) => {
                    return acc += curVal.product.price * curVal.quantity
                }, 0)
            },
        }
    }
    </script>

Category.vue:

    <template>
        <!-- Основной контейнер страницы категории -->
        <div class="page-category">
            <!-- Обертка для колонок в многоколоночной сетке -->
            <div class="columns is-multiline">
                <!-- Заголовок страницы с именем текущей категории -->
                <div class="column is-12">
                    <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
                </div>
    
                <!-- Компонент ProductBox используется для отображения каждого товара в категории -->
                <ProductBox 
                    v-for="product in category.products"
                    v-bind:key="product.id"
                    v-bind:product="product" />
            </div>
        </div>
    </template>
    
    <script>
    import axios from 'axios'
    import { toast } from 'bulma-toast'
    
    import ProductBox from '@/components/ProductBox'
    
    export default {
        name: 'Category',  // Название компонента
        components: {
            ProductBox  // Регистрация компонента ProductBox
        },
        data() {
            return {
                category: {
                    products: []  // Инициализация свойства category с массивом товаров
                }
            }
        },
        mounted() {
            this.getCategory()  // Вызов метода getCategory при монтировании компонента
        },
        watch: {
            $route(to, from) {
                // Слежение за изменениями маршрута, если текущий маршрут - категория, вызываем метод getCategory
                if (to.name === 'Category') {
                    this.getCategory()
                }
            }
        },
        methods: {
            // Асинхронный метод для получения данных о категории с сервера
            async getCategory() {
                // Извлечение slug категории из параметра маршрута
                const categorySlug = this.$route.params.category_slug
    
                // Установка состояния загрузки в true
                this.$store.commit('setIsLoading', true)
    
                // Запрос на сервер для получения данных о категории
                axios
                    .get(`/api/v1/products/${categorySlug}/`)
                    .then(response => {
                        // Обновление данных категории в свойстве
                        this.category = response.data
    
                        // Установка заголовка страницы
                        document.title = this.category.name + ' | Книги'
                    })
                    .catch(error => {
                        // Обработка ошибки и вывод сообщения пользователю
                        console.log(error)
    
                        toast({
                            message: 'Что-то пошло не так, пожалуйста, попробуйте позже(',
                            type: 'is-danger',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                    })
    
                // Установка состояния загрузки в false после завершения запроса
                this.$store.commit('setIsLoading', false)
            }
        }
    }
    </script>

Checkout.vue

        <template>
        <!-- Основной контейнер страницы оформления заказа -->
        <div class="page-checkout">
            <!-- Обертка для колонок в многоколоночной сетке -->
            <div class="columns is-multiline">
                <!-- Заголовок страницы -->
                <div class="column is-12">
                    <h1 class="title">Доставка</h1>
                </div>
    
                <!-- Блок с информацией о товарах в корзине -->
                <div class="column is-12 box">
                    <!-- Таблица для отображения товаров -->
                    <table class="table is-fullwidth">
                        <thead>
                            <tr>
                                <th>Товар</th>
                                <th>Цена</th>
                                <th>Количество</th>
                                <th>Итого</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Цикл для отображения каждого товара в корзине -->
                            <tr v-for="item in cart.items" :key="item.product.id">
                                <td>{{ item.product.name }}</td>
                                <td>${{ item.product.price }}</td>
                                <td>{{ item.quantity }}</td>
                                <td>${{ getItemTotal(item).toFixed(2) }}</td>
                            </tr>
                        </tbody>
                        <tfoot>
                            <!-- Итоговая строка в таблице с общей стоимостью и количеством товаров -->
                            <tr>
                                <td colspan="2">Итого</td>
                                <td>{{ cartTotalLength }}</td>
                                <td>{{ cartTotalPrice.toFixed(2) }}руб</td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
    
                <!-- Блок с деталями доставки -->
                <div class="column is-12 box">
                    <!-- Подзаголовок блока -->
                    <h2 class="subtitle">Детали доставки</h2>
                    <!-- Подсказка для пользователя -->
                    <p class="has-text-grey mb-4">* Все поля должны быть заполнены</p>
    
                    <!-- Две колонки с полями для ввода информации о доставке -->
                    <div class="columns is-multiline">
                        <!-- Первая колонка с полями для ввода имени, фамилии, email и телефона -->
                        <div class="column is-6">
                            <!-- Каждое поле ввода -->
                            <div class="field">
                                <label>Имя*</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="first_name">
                                </div>
                            </div>
    
                            <!-- Аналогично для фамилии, email и телефона -->
                            <!-- ... -->
                        </div>
    
                        <!-- Вторая колонка с полями для ввода адреса, индекса и номера дома -->
                        <div class="column is-6">
                            <!-- Каждое поле ввода -->
                            <div class="field">
                                <label>Адрес*</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="address">
                                </div>
                            </div>
    
                            <!-- Аналогично для индекса и номера дома -->
                            <!-- ... -->
                        </div>
                    </div>
    
                    <!-- Горизонтальная линия-разделитель -->
                    <hr>
                    <!-- Блок для ввода данных банковской карты (не реализовано в данном коде) -->
                    <div id="card-element" class="mb-5"></div>
                    <!-- Кнопка для эмуляции оплаты (не реальная оплата) -->
                    <button class="button is-primary" @click="simulatePayment">Оплатить</button>
                </div>
            </div>
        </div>
    </template>
    
    <script>
    // Импорт библиотек и настроек
    import axios from 'axios'
    
    export default {
        // Название компонента
        name: 'Checkout',
        // Данные компонента
        data() {
            return {
                // Объект корзины с товарами
                cart: {
                    items: []
                },
                // Объекты для работы с платежами (Stripe, не реализовано в данном коде)
                stripe: {},
                card: {},
                // Переменные для ввода данных о доставке
                first_name: '',
                last_name: '',
                email: '',
                phone: '',
                address: '',
                zipcode: '',
                place: '',
                // Массив для хранения ошибок валидации
                errors: []
            }
        },
        // Хук жизненного цикла компонента - момент, когда компонент монтируется в DOM
        mounted() {
            // Установка заголовка страницы
            document.title = 'Checkout | Книги'
            // Получение данных о корзине из хранилища Vuex
            this.cart = this.$store.state.cart
        },
        // Методы компонента
        methods: {
            // Метод для вычисления общей стоимости товара
            getItemTotal(item) {
                return item.quantity * item.product.price
            },
            // Метод для эмуляции платежа (не реальная оплата)
            simulatePayment() {
                // Очистка массива ошибок перед валидацией
                this.errors = []
    
                // Валидация данных о доставке
                if (this.first_name === '') {
                    this.errors.push('Поле "Имя" обязательно для заполнения!')
                }
    
                // Аналогично для фамилии, email, телефона, адреса, индекса, номера дома
                // ...
    
                // Если нет ошибок в валидации
                if (!this.errors.length) {
                    // Установка состояния загрузки в true (в реальном проекте это могло бы быть асинхронным запросом на сервер)
                    this.$store.commit('setIsLoading', true)
    
                    // Имитация запроса к серверу Stripe с задержкой в 2 секунды
                    setTimeout(async () => {
                        // Эмуляция успешного платежа
                        this.$store.commit('clearCart')
                        localStorage.setItem('paymentSuccess', 'true')
                        this.$router.push('/cart/success')
                        // Установка состояния загрузки в false после завершения запроса
                        this.$store.commit('setIsLoading', false)
                    }, 2000) // Задержка в 2 секунды
                }
            },
        },
        // Вычисляемые свойства компонента
        computed: {
            // Вычисление общей стоимости корзины
            cartTotalPrice() {
                return this.cart.items.reduce((acc, curVal) => {
                    return (acc += curVal.product.price * curVal.quantity)
                }, 0)
            },
            // Вычисление общего количества товаров в корзине
            cartTotalLength() {
                return this.cart.items.reduce((acc, curVal) => {
                    return (acc += curVal.quantity)
                }, 0)
            }
        }
    }
    </script>

FavouriteBooks.vue
    
    <template>
      <!-- Компонент для отображения избранных книг -->
      <div class="favorite-products">
        <!-- Заголовок страницы -->
        <h1 class="title">Избранные книги</h1>
    
        <!-- Проверка наличия избранных книг -->
        <div v-if="favoriteProducts.length === 0">
          <!-- Сообщение о том, что избранных книг нет -->
          <p>У вас пока нет избранных книг.</p>
        </div>
    
        <!-- Если есть избранные книги -->
        <div v-else>
          <!-- Цикл для отображения каждой избранной книги -->
          <div v-for="product in favoriteProducts" :key="product.id" class="column is-3">
            <!-- Карточка с избранной книгой -->
            <div class="box">
              <!-- Изображение книги -->
              <figure class="image mb-4">
                <img :src="product.get_thumbnail" alt="Product Thumbnail">
              </figure>
              <!-- Название книги -->
              <h3 class="is-size-4">{{ product.name }}</h3>
              <!-- Цена книги -->
              <p class="is-size-6 has-text-grey">{{ product.price }}руб.</p>
              <!-- Кнопка для добавления/удаления из избранного -->
              <button @click="toggleFavorite(product)" class="button is-danger mt-4">
                {{ product.is_favorite ? 'Убрать из избранных' : 'Добавить в избранное' }}
              </button>
              <!-- Кнопка для перехода к подробной информации о книге -->
              <router-link :to="product.get_absolute_url" class="button is-dark mt-2">Подробнее</router-link>
            </div>
          </div>
        </div>
      </div>
    </template>
    
    <script>
    // Импорт библиотеки для HTTP-запросов
    import axios from 'axios';
    
    export default {
      // Название компонента
      name: 'FavouriteBooks',
      // Данные компонента
      data() {
        return {
          // Массив для хранения избранных книг
          favoriteProducts: [],
        };
      },
      // Хук жизненного цикла компонента - срабатывает при создании компонента
      created() {
        // Вызов метода для получения избранных книг
        this.getFavoriteProducts();
      },
      // Методы компонента
      methods: {
        // Асинхронный метод для получения избранных книг с сервера
        async getFavoriteProducts() {
          try {
            // Выполнение HTTP-запроса на получение избранных книг
            const response = await axios.get('/api/v1/favorite-products');
            // Обновление данных избранных книг в компоненте
            this.favoriteProducts = response.data;
          } catch (error) {
            // Обработка ошибок при выполнении запроса
            console.error('Ошибка при получении избранных книг', error);
          }
        },
        // Асинхронный метод для переключения статуса избранного книги
        async toggleFavorite(product) {
          try {
            // Выполнение HTTP-запроса на изменение статуса избранного
            const response = await axios.patch(`/api/v1/products/${product.id}/toggle-favorite/`);
            // Обновление статуса избранного в данных книги
            product.is_favorite = response.data.is_favorite;
          } catch (error) {
            // Обработка ошибок при выполнении запроса
            console.error('Ошибка при изменении статуса избранного', error);
          }
        },
      },
    };
    </script>
    
    <style scoped>
    /* Стили, применяемые только к данному компоненту */
    .image {
      margin-top: -1.25rem;
      margin-left: -1.25rem;
      margin-right: -1.25rem;
    }
    </style>

Home.vue

    <template>
      <!-- Домашняя страница -->
      <div class="home">
        <!-- Секция с главным заголовком страницы -->
        <section class="hero is-medium is-dark mb-6">
          <!-- Центрированный текст внутри секции -->
          <div class="hero-body has-text-centered">
            <!-- Заголовок с приветствием на странице -->
            <p class="title mb-6">
              Добро пожаловать!
            </p>
            <!-- Подзаголовок (в данном случае пустой) -->
            <p class="subtitle">
            </p>
          </div>
        </section>
    
        <!-- Раздел с колонками, содержащими последние продукты -->
        <div class="columns is-multiline">
          <!-- Колонка на всю ширину -->
          <div class="column is-12">
            <!-- Заголовок для последних продуктов -->
            <h2 class="is-size-2 has-text-centered">Последнее</h2>
          </div>
    
          <!-- Итерация по последним продуктам и отображение каждого в виде ProductBox -->
          <ProductBox 
            v-for="product in latestProducts"
            v-bind:key="product.id"
            v-bind:product="product"/>
        </div>
      </div>
    </template>
    
    <script>
    // Импорт библиотеки для HTTP-запросов
    import axios from 'axios'
    
    // Импорт компонента ProductBox
    import ProductBox from '@/components/ProductBox'
    
    export default {
      // Название компонента
      name: 'Home',
      // Данные компонента
      data() {
        return {
          // Массив для хранения последних продуктов
          latestProducts: []
        }
      },
      // Компоненты, используемые внутри Home
      components: {
        name:'ProductBox'
      },
      // Хук жизненного цикла компонента - срабатывает после монтирования компонента на страницу
      mounted() {
        // Вызов метода для получения последних продуктов
        this.getLatestProducts()
        // Установка заголовка страницы (в данном случае закомментировано)
        // document.title = 'Домашняя | Книги'
      },
      // Методы компонента
      methods: {
        // Асинхронный метод для получения последних продуктов с сервера
        async getLatestProducts() {
          // Установка флага загрузки данных
          this.$store.commit('setIsLoading', true)
    
          // Выполнение HTTP-запроса на получение последних продуктов
          await axios
            .get('/api/v1/latest-products/')
            .then(response => {
              // Обновление данных последних продуктов в компоненте
              this.latestProducts = response.data
            })
            .catch(error => {
              // Обработка ошибок при выполнении запроса
              console.log(error)
            })
    
          // Сброс флага загрузки данных
          this.$store.commit('setIsLoading', false)
        }
      }
    }
    </script>

LogIn.vue:

    <template>
        <!-- Страница входа -->
        <div class="page-log-in">
            <!-- Контейнер сетки из колонок -->
            <div class="columns">
                <!-- Центрированная колонка шириной 4 из 12 смещенная на 4 из 12 -->
                <div class="column is-4 is-offset-4">
                    <!-- Заголовок страницы -->
                    <h1 class="title">Вход</h1>
    
                    <!-- Форма для ввода данных пользователя -->
                    <form @submit.prevent="submitForm">
                        <!-- Поле ввода имени пользователя -->
                        <div class="field">
                            <label>Имя пользователя</label>
                            <div class="control">
                                <input type="text" class="input" v-model="username">
                            </div>
                        </div>
    
                        <!-- Поле ввода пароля -->
                        <div class="field">
                            <label>Пароль</label>
                            <div class="control">
                                <input type="password" class="input" v-model="password">
                            </div>
                        </div>
    
                        <!-- Оповещение об ошибках, отображается при наличии ошибок -->
                        <div class="notification is-danger" v-if="errors.length">
                            <!-- Итерация по массиву ошибок и их отображение -->
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
    
                        <!-- Кнопка для отправки формы -->
                        <div class="field">
                            <div class="control">
                                <button class="button is-dark">Войти</button>
                            </div>
                        </div>
    
                        <!-- Горизонтальная линия -->
                        <hr>
    
                        <!-- Ссылка на страницу регистрации -->
                        или <router-link to="/sign-up">нажмите тут</router-link>, чтобы зарегистрироваться!
                    </form>
                </div>
            </div>
        </div>
    </template>
    
    <script>
    // Импорт библиотеки для HTTP-запросов
    import axios from 'axios'
    
    // Экспорт компонента страницы входа
    export default {
        // Название компонента
        name: 'LogIn',
        // Данные компонента
        data() {
            return {
                // Переменные для хранения имени пользователя, пароля и ошибок
                username: '',
                password: '',
                errors: []
            }
        },
        // Хук жизненного цикла компонента - срабатывает после монтирования компонента на страницу
        mounted() {
            // Установка заголовка страницы
            document.title = 'Вход | Книги'
        },
        // Методы компонента
        methods: {
            // Асинхронный метод для отправки данных формы на сервер
            async submitForm() {
                // Очистка заголовка авторизации перед отправкой запроса
                axios.defaults.headers.common["Authorization"] = ""
    
                // Удаление токена из локального хранилища
                localStorage.removeItem("token")
    
                // Формирование данных формы для отправки на сервер
                const formData = {
                    username: this.username,
                    password: this.password
                }
    
                // Выполнение HTTP-запроса на сервер для получения токена
                await axios
                    .post("/api/v1/token/login/", formData)
                    .then(response => {
                        // Извлечение токена из ответа сервера
                        const token = response.data.auth_token
    
                        // Обновление токена в хранилище состояния приложения
                        this.$store.commit('setToken', token)
                        
                        // Установка токена в заголовок авторизации для последующих запросов
                        axios.defaults.headers.common["Authorization"] = "Token " + token
    
                        // Сохранение токена в локальном хранилище
                        localStorage.setItem("token", token)
    
                        // Переход на страницу корзины или на другую страницу, указанную в параметрах запроса
                        const toPath = this.$route.query.to || '/cart'
                        this.$router.push(toPath)
                    })
                    .catch(error => {
                        // Обработка ошибок при выполнении запроса
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else {
                            this.errors.push('Что-то пошло не так, попробуйте снова(')
                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }
    </script>

MyAccount.vue:

    <template>
      <!-- Страница "Мой профиль" -->
      <div class="page-my-account">
        <!-- Контейнер сетки из колонок -->
        <div class="columns is-multiline">
          <!-- Широкая колонка, занимающая всю ширину -->
          <div class="column is-12">
            <!-- Заголовок страницы -->
            <h1 class="title">My account</h1>
          </div>
    
          <!-- Колонка с формой для изменения данных профиля -->
          <div class="column is-12">
            <!-- Подзаголовок -->
            <h2 class="subtitle">Изменить данные профиля</h2>
            
            <!-- Форма для ввода новых данных профиля -->
            <form @submit.prevent="updateProfile">
              <!-- Поле ввода имени пользователя -->
              <div class="field">
                <label class="label">Имя</label>
                <div class="control">
                  <input type="text" class="input" v-model="username">
                </div>
              </div>
    
              <!-- Поле ввода электронной почты -->
              <div class="field">
                <label class="label">Email</label>
                <div class="control">
                  <input type="email" class="input" v-model="email">
                </div>
              </div>
    
              <!-- Здесь могут быть добавлены другие поля для изменения данных профиля -->
    
              <!-- Кнопка сохранения изменений -->
              <div class="field">
                <div class="control">
                  <button type="submit" class="button is-primary">Сохранить</button>
                </div>
              </div>
            </form>
          </div>
    
          <!-- Колонка с кнопкой для выхода из аккаунта -->
          <div class="column is-12">
            <button @click="logout()" class="button is-danger">Log out</button>
          </div>
    
          <!-- Горизонтальная линия -->
          <hr>
    
          <!-- Колонка с заголовком и списком заказов пользователя -->
          <div class="column is-12">
            <!-- Заголовок -->
            <h2 class="subtitle"></h2>
    
            <!-- Компонент OrderSummary для каждого заказа пользователя -->
            <OrderSummary
              v-for="order in orders"
              v-bind:key="order.id"
              v-bind:order="order" />
          </div>
        </div>
      </div>
    </template>
    
    <script>
    // Импорт библиотеки для HTTP-запросов
    import axios from 'axios'
    
    // Импорт компонента OrderSummary для отображения данных заказов
    import OrderSummary from '@/components/OrderSummary.vue'
    
    // Экспорт компонента "Мой профиль"
    export default {
      // Название компонента
      name: 'MyAccount',
      // Регистрация компонента OrderSummary для использования в шаблоне
      components: {
        OrderSummary
      },
      // Данные компонента
      data() {
        return {
          // Массив для хранения данных заказов пользователя
          orders: []
        }
      },
      // Хук жизненного цикла компонента - срабатывает после монтирования на страницу
      mounted() {
        // Установка заголовка страницы
        document.title = 'Mой профиль | Книги'
    
        // Получение данных о заказах пользователя
        this.getMyOrders()
      },
      // Методы компонента
      methods: {
        // Метод для выхода из аккаунта
        logout() {
          // Очистка заголовка авторизации перед выходом
          axios.defaults.headers.common["Authorization"] = ""
    
          // Удаление токена и других данных пользователя из локального хранилища
          localStorage.removeItem("token")
          localStorage.removeItem("username")
          localStorage.removeItem("userid")
    
          // Удаление токена из хранилища состояния приложения
          this.$store.commit('removeToken')
    
          // Переход на главную страницу
          this.$router.push('/')
        },
        // Асинхронный метод для получения данных о заказах пользователя
        async getMyOrders() {
          // Установка флага загрузки данных
          this.$store.commit('setIsLoading', true)
    
          // Выполнение HTTP-запроса на сервер для получения данных о заказах
          await axios
            .get('/api/v1/orders/')
            .then(response => {
              // Запись полученных данных в массив orders
              this.orders = response.data
            })
            .catch(error => {
              // Обработка ошибок при выполнении запроса
              console.log(error)
            })
    
          // Снятие флага загрузки данных
          this.$store.commit('setIsLoading', false)
        }
      }
    }
    </script>


