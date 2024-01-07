<template>
    <div>
      <h2>Создать новое поступление</h2>
      <form @submit.prevent="createNewspaperarrival">
        <div class="form-group">
          <label for="newspaper">Газета:</label>
          <input v-model="newspaperarrival.number" type="number" id="newspaper" required>
        </div>
  
        <div class="form-group">
          <label for="post_office">Отделение почты:</label>
          <input v-model="newspaperarrival.address" type="number" id="post_office" required>
        </div>

        <div class="form-group">
          <label for="quantity">Количество:</label>
          <input v-model="newspaperarrival.quantity" type="number" id="quantity" required>
        </div>
  
        <button type="submit" :class="{ 'active-button': isValidForm }">Сохранить</button>
      </form>
      <button @click="goToMainPage" class="back-button">На главную</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        newspaperarrival: {
          newspaper: '',
          post_office: '',
          quantity: '',
        },
      };
    },
    computed: {
      isValidForm() {
        return (
          this.newspaperarrival.newspaper &&
          this.newspaperarrival.post_office &&
          this.newspaperarrival.quantity
        );
      },
    },
    methods: {
      async createNewspaperarrival() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/newspaperarrivals/', this.newspaperarrival);
          console.log('Server response:', response.data);
          this.$root.eventBus.$emit('updateNewspaperarrival');
          this.$router.push({ name: 'NewsPaperArrivalList' });
        } catch (error) {
          console.error(error);
        }
      },
      goToMainPage(){
        this.$router.push({ name: 'MainPage' });
      },
    },
  };
  </script>
  
  <style scoped>
  /* ... ваш общий стиль для кнопок ... */
  
  /* Дополнительные стили для кнопки возврата на главную */
  .back-button {
    margin-top: 20px; /* Добавлен верхний отступ */
  }
  
  /* Стили для групп полей формы */
  .form-group {
    margin-bottom: 15px;
  }
  
  /* Стили для меток полей формы */
  label {
    display: block;
    margin-bottom: 5px;
    color: #333; /* Цвет текста метки */
    font-weight: bold; /* Жирный шрифт для метки */
  }
  
  /* Стили для полей ввода формы */
  input {
    width: 100%; /* Занимать всю доступную ширину */
    padding: 10px;
    border: 1px solid #3498db;
    border-radius: 8px;
    box-sizing: border-box;
    margin-bottom: 10px;
  }
  
  /* Стили для кнопок формы */
  button {
    background-color: transparent;
    color: #333;
    border: 2px solid #3498db;
    padding: 15px 20px;
    border-radius: 30px;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
    display: block;
    margin-bottom: 10px;
  }
  
  button:hover {
    background-color: #3498db;
    color: #ffff;
  }
  </style>
  
  