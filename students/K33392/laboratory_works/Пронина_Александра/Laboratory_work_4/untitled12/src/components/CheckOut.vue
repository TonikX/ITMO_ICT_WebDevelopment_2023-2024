<template>
  <div>
    <h2>Checkout</h2>
    <form @submit.prevent="placeOrder">
      <!-- Поля для ввода информации о доставке и платеже -->
      <input type="text" v-model="address" placeholder="Введите адрес" required>
      <input type="text" v-model="paymentInfo" placeholder="Введите информацию о платеже" required>
      <button type="submit">Отправить заказ</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CheckOut',
  data() {
    return {
      address: '',
      paymentInfo: ''
    };
  },
  methods: {
    placeOrder() {
      const orderData = {
        address: this.address,
        paymentInfo: this.paymentInfo
      };

      axios.post('http://127.0.0.1:8000/orders/', orderData) // Используем ваш эндпоинт для создания заказа
          .then(response => {
            console.log('Заказ успешно оформлен:', response.data);
            // Логика при успешном оформлении заказа
          })
          .catch(error => {
            console.error('Ошибка при оформлении заказа:', error);
            // Логика при ошибке оформления заказа
          });
    }
  }
};
</script>
