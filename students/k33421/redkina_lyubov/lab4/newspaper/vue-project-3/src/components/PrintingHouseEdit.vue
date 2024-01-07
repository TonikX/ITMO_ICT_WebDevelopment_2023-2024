<template>
    <div class="edit-printinghouse">
      <h2>Редактировать издательство</h2>
      <form @submit.prevent="saveChanges">
        <div class="form-group">
          <label for="name">Название:</label>
          <input v-model="editedPrintinghouse.name" type="text" id="name" required>
        </div>
  
        <div class="form-group">
          <label for="address">Адрес:</label>
          <input v-model="editedPrintinghouse.address" type="text" id="address" required>
        </div>
  
        <div class="form-group">
          <label for="is_closed">Статус:</label>
          <input v-model="editedPrintinghouse.is_closed" type="checkbox" id="is_closed" required>
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
        editedPrintinghouse: {
          name: '',
          address: '',
          status: true,
        },
      };
    },
    methods: {
      async fetchPrintinghouseDetails() {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/printinghouses/${this.$route.params.id}/`);
          this.editedPrintinghouse = response.data;
        } catch (error) {
          console.error(error);
        }
      },
      async saveChanges() {
        try {
          await axios.put(`http://127.0.0.1:8000/api/printinghouses/${this.$route.params.id}/`, this.editedPrintinghouse);
          // В случае успешного сохранения, вы можете выполнить дополнительные действия, например, перенаправление на страницу с деталями
          this.$router.push({ name: 'PrintingHousesDetails', params: { id: this.$route.params.id }});
        } catch (error) {
          console.error(error);
        }
      },
    },
    created() {
      this.fetchPrintinghouseDetails();
    },
    computed: {
      isValidForm() {
        return (
          this.editedPrintinghouse.name &&
          this.editedPrintinghouse.address &&
          this.editedPrintinghouse.status
        );
      },
    },
  };
  </script>
  
  <style scoped>
  .edit-printinghouse {
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
  