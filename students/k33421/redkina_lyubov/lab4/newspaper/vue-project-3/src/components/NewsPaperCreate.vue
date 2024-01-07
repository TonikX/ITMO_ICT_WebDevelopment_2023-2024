<template>
    <div>
      <h2>Создать новую газету</h2>
      <form @submit.prevent="createNewspaper">
        <div class="form-group">
          <label for="title">Название газеты:</label>
          <input v-model="newspaper.title" type="text" id="title" required>
        </div>
  
        <div class="form-group">
          <label for="edition_index">Индекс выпуска:</label>
          <input v-model="newspaper.edition_index" type="text" id="edition_index" required>
        </div>
  
        <div class="form-group">
          <label for="editor_first_name">Имя редактора:</label>
          <input v-model="newspaper.editor_first_name" type="text" id="editor_first_name" required>
        </div>
  
        <div class="form-group">
          <label for="editor_last_name">Фамилия редактора:</label>
          <input v-model="newspaper.editor_last_name" type="text" id="editor_last_name" required>
        </div>
  
        <div class="form-group">
          <label for="editor_middle_name">Отчество редактора:</label>
          <input v-model="newspaper.editor_middle_name" type="text" id="editor_middle_name">
        </div>
  
        <div class="form-group">
          <label for="price">Цена:</label>
          <input v-model="newspaper.price" type="text" id="price" required>
        </div>
  
        <!-- Добавьте другие поля газеты, если необходимо -->
  
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
        newspaper: {
          title: '',
          edition_index: '',
          editor_first_name: '',
          editor_last_name: '',
          editor_middle_name: '',
          price: '',
          // Добавьте другие поля газеты, которые вы хотите создать
        },
      };
    },
    computed: {
      isValidForm() {
        return (
          this.newspaper.title &&
          this.newspaper.edition_index &&
          this.newspaper.editor_first_name &&
          this.newspaper.editor_last_name &&
          this.newspaper.price
        );
      },
    },
    methods: {
      async createNewspaper() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/newspapers/', this.newspaper);
          console.log('Server response:', response.data);
          this.$root.eventBus.$emit('updateNewspapers');
          this.$router.push({ name: 'NewsPaperList' });
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
  
  