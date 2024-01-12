# Компоненты

Итак, у меня всего 3 компоненты:

1. CartItem
<template>
    <!-- Верстка для отображения отдельного элемента корзины -->
    <tr>
        <!-- Ссылка на страницу продукта с использованием Vue Router -->
        <td><router-link :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></td>
        
        <!-- Отображение цены продукта -->
        <td>${{ item.product.price }}</td>
        
        <!-- Отображение количества продукта и кнопок для изменения количества -->
        <td>
            {{ item.quantity }}
            <!-- Уменьшение количества на 1 -->
            <a @click="decrementQuantity(item)">-</a>
            <!-- Увеличение количества на 1 -->
            <a @click="incrementQuantity(item)">+</a>
        </td>
        
        <!-- Отображение общей стоимости продукта в корзине -->
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
        
        <!-- Кнопка для удаления продукта из корзины -->
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',  // Название компонента
    props: {
        initialItem: Object  // Переданный через свойство объект initialItem
    },
    data() {
        return {
            item: this.initialItem  // Инициализация данных компонента из initialItem
        }
    },
    methods: {
        // Метод для вычисления общей стоимости продукта в корзине
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        // Метод для уменьшения количества продукта на 1
        decrementQuantity(item) {
            item.quantity -= 1

            if (item.quantity === 

2. OrderSummary
<template>
    <!-- Обертка для блока заказа -->
    <div class="box mb-4">
        <!-- Заголовок с номером заказа -->
        <h3 class="is-size-4 mb-6">Заказ #{{ order.id }}</h3>

        <!-- Заголовок раздела с товарами в заказе -->
        <h4 class="is-size-5">Товары</h4>

        <!-- Таблица для отображения товаров в заказе -->
        <table class="table is-fullwidth">
            <thead>
                <tr>
                    <!-- Заголовки столбцов таблицы -->
                    <th>Товар</th>
                    <th>Цена</th>
                    <th>Количество</th>
                    <th>Итого</th>
                </tr>
            </thead>

            <tbody>
                <!-- Цикл для отображения каждого товара в заказе -->
                <tr
                    v-for="item in order.items"
                    v-bind:key="item.product.id"
                >
                    <!-- Отображение данных о товаре -->
                    <td>{{ item.product.name }}</td>
                    <td>${{ item.product.price }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>${{ getItemTotal(item).toFixed(2) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'OrderSummary',  // Название компонента
    props: {
        order: Object  // Свойство, представляющее объект заказа
    },
    methods: {
        // Метод для вычисления общей стоимости товара в заказе
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        // Метод для вычисления общего количества товаров в заказе
        orderTotalLength(order) {
            return order.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
    }
}
</script>

Этот компонент Vue предназначен для отображения информации о заказе, включая номер заказа, список товаров, их цены, количество и общую стоимость. Методы компонента используются для вычисления общей стоимости товара и общего количества товаров в заказе.

3. ProdictBox
<template>
    <!-- Компонент-контейнер для товара, представленного в виде блока -->
    <div class="column is-3">
        <!-- Обертка для блока товара -->
        <div class="box">
            <!-- Изображение товара -->
            <figure class="image mb-4">
                <!-- Динамическое связывание атрибута src с методом get_thumbnail объекта product -->
                <img v-bind:src="product.get_thumbnail">
            </figure>

            <!-- Название товара -->
            <h3 class="is-size-4">{{ product.name }}</h3>
            
            <!-- Цена товара -->
            <p class="is-size-6 has-text-grey">{{ product.price }}руб.</p>

            <!-- Ссылка для перехода к подробной информации о товаре -->
            <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">Подробнее</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProductBox',  // Название компонента
    props: {
        product: Object  // Свойство, представляющее объект товара
    }
}
</script>

<style scoped>
  /* Стили применяются только к этому компоненту */
  .image {
    /* Изменение отступов для изображения товара */
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>

Этот компонент представляет товар в виде блока, который может использоваться для отображения списка товаров. В компоненте есть изображение товара, его название, цена и кнопка для перехода к подробной информации о товаре. Стили применяются только к данному компоненту, что обеспечивает изоляцию стилей от других компонентов.
