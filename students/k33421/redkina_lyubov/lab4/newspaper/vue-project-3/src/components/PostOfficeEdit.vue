<template>
    <div class="edit-postoffice">
      <h2>Редактировать почтовое отделение</h2>
      <form @submit.prevent="saveChanges">
        <div class="form-group">
          <label for="number">Номер отделения:</label>
          <input v-model="editedPostoffice.number" type="number" id="number" required>
        </div>
  
        <div class="form-group">
          <label for="address">Адрес:</label>
          <input v-model="editedPostoffice.address" type="text" id="address" required>
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
        editedPostoffice: {
          number: '',
          address: '',
        },
      };
    },
    methods: {
      async fetchPostofficeDetails() {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/postoffices/${this.$route.params.id}/`);
          this.editedPostoffice = response.data;
        } catch (error) {
          console.error(error);
        }
      },
      async saveChanges() {
        try {
          await axios.put(`http://127.0.0.1:8000/api/postoffices/${this.$route.params.id}/`, this.editedPostoffice);
          // В случае успешного сохранения, вы можете выполнить дополнительные действия, например, перенаправление на страницу с деталями
          this.$router.push({ name: 'PostOfficeDetails', params: { id: this.$route.params.id }});
        } catch (error) {
          console.error(error);
        }
      },
    },
    created() {
      this.fetchPostofficeDetails();
    },
    computed: {
      isValidForm() {
        return (
          this.editedPostoffice.number &&
          this.editedPostoffice.address
        );
      },
    },
  };
  </script>
  
  <style scoped>
  .edit-postoffice {
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
  