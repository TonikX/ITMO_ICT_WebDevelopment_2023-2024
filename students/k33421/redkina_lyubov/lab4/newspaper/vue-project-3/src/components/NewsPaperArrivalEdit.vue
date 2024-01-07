<template>
    <div class="edit-newspaperarrival">
      <h2>Редактировать поступление газеты</h2>
      <form @submit.prevent="saveChanges">
        <div class="form-group">
          <label for="newspaper">Газета:</label>
          <input v-model="editedNewspaperarrival.number" type="number" id="newspaper" required>
        </div>
  
        <div class="form-group">
          <label for="post_office">Почтовое отделение:</label>
          <input v-model="editedNewspaperarrival.post_office" type="number" id="post_office" required>
        </div>

        <div class="form-group">
          <label for="quantity">Количество:</label>
          <input v-model="editedNewspaperarrival.quantity" type="number" id="quantity" required>
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
        editedNewspaperarrival: {
          newspaper: '',
          post_office: '',
          quantity: '',
        },
      };
    },
    methods: {
      async fetchNewspaperarrivalDetails() {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/newspaperarrivals/${this.$route.params.id}/`);
          this.editedNewspaperarrival = response.data;
        } catch (error) {
          console.error(error);
        }
      },
      async saveChanges() {
        try {
          await axios.put(`http://127.0.0.1:8000/api/newspaperarrivals/${this.$route.params.id}/`, this.editedNewspaperarrival);
          // В случае успешного сохранения, вы можете выполнить дополнительные действия, например, перенаправление на страницу с деталями
          this.$router.push({ name: 'NewsPaperArrivalDetails', params: { id: this.$route.params.id }});
        } catch (error) {
          console.error(error);
        }
      },
    },
    created() {
      this.fetchNewspaperarrivalDetails();
    },
    computed: {
      isValidForm() {
        return (
          this.editedNewspaperarrival.newspaper &&
          this.editedNewspaperarrival.post_office &&
          this.editedNewspaperarrival.quantity
        );
      },
    },
  };
  </script>
  
  <style scoped>
  .edit-newspaperarrival {
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
  