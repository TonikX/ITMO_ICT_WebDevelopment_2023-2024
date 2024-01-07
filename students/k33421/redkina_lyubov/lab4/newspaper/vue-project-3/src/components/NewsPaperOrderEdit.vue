<template>
    <div class="edit-newspaperorder">
      <h2>Редактировать заказ газеты</h2>
      <form @submit.prevent="saveChanges">
        <div class="form-group">
          <label for="user_profile">Получатель:</label>
          <input v-model="editedNewspaperorder.user_profile" type="number" id="user_profile" required>
        </div>
  
        <div class="form-group">
          <label for="newspaper">Идентификатор газеты:</label>
          <input v-model="editedNewspaperorder.newspaper" type="number" id="newspaper" required>
        </div>

        <div class="form-group">
          <label for="quantity">Количество:</label>
          <input v-model="editedNewspaperorder.quantity" type="number" id="quantity" required>
        </div>

        <div class="form-group">
          <label for="order_date">Дата получения:</label>
          <input v-model="editedNewspaperorder.order_date" type="date" id="order_date" required>
        </div>

        <button :class="{ 'inactive-button': !isValidForm }" type="submit">Сохранить изменения</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        editedNewspaperorder: {
          user_profile: '',
          newspaper: '',
          quantity: '',
          order_date: '',
        },
      };
    },
    methods: {
      async fetchNewspaperorderDetails() {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/newspaperorders/${this.$route.params.id}/`);
          this.editedNewspaperorder = response.data;
        } catch (error) {
          console.error(error);
        }
      },
      async saveChanges() {
        try {
          await axios.put(`http://127.0.0.1:8000/api/newspaperorders/${this.$route.params.id}/`, this.editedNewspaperorder);
          // В случае успешного сохранения, вы можете выполнить дополнительные действия, например, перенаправление на страницу с деталями
          this.$router.push({ name: 'NewsPaperOrderDetails', params: { id: this.$route.params.id }});
        } catch (error) {
          console.error(error);
        }
      },
    },
    created() {
      this.fetchNewspaperorderDetails();
    },
    computed: {
      isValidForm() {
        return (
          this.editedNewspaperorder.user_profile &&
          this.editedNewspaperorder.newspaper &&
          this.editedNewspaperorder.quantity &&
          this.editedNewspaperorder.order_date
        );
      },
    },
  };
  </script>
  
  <style scoped>
  .edit-newspaperorder {
    text-align: center;
    padding: 20px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    font-size: 16px;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 10px;
    font-size: 14px;
  }
  
  button {
    padding: 15px 20px;
    font-size: 16px;
    border-radius: 30px;
    background-color: transparent;
    color: #3498db;
    border: 1px solid #3498db;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
  }
  
  button:hover {
    background-color: #3498db;
    color: #fff;
  }
  
  /* Новые стили для неактивной кнопки */
  .inactive-button {
    background-color: transparent;
    color: #3498db;
    border: 1px solid #3498db;
  }
  
  .inactive-button:hover {
    background-color: #3498db;
    color: #fff;
  }
  </style>
  