<template>
  <div>
    <h2>Shopping Cart</h2>
    <div v-if="cartItems.length === 0">
      <p>Ваша корзина пуста.</p>
    </div>
    <div v-else>
      <ul>
        <li v-for="item in cartItems" :key="item.id">
          {{ item.title }} - {{ item.price }} - {{ item.quantity }}
        </li>
      </ul>
      <p>Общая стоимость: {{ totalCost }}</p>
      <!-- Дополнительная логика оформления заказа, удаления товаров из корзины и т.д. -->
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CarT',
  data() {
    return {
      cartItems: [],
      totalCost: 0
    };
  },
  mounted() {
    this.fetchCartItems();
  },
  methods: {
    fetchCartItems() {
      axios.get('http://127.0.0.1:8000/cart/') // Используем адрес вашего бэкенда
          .then(response => {
            this.cartItems = response.data.items;
            this.totalCost = response.data.totalCost;
          })
          .catch(error => {
            console.error('Ошибка при получении содержимого корзины:', error);
          });
    }
  }
};
</script>
