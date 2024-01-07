<template>
    <div class="edit-newspaperprint">
      <h2>Редактировать выпуск газеты</h2>
      <form @submit.prevent="saveChanges">
        <div class="form-group">
          <label for="newspaper">Газета:</label>
          <input v-model="editedNewspaperprint.newspaper" type="text" id="newspaper" required>
        </div>
  
        <div class="form-group">
          <label for="printing_house">Издательство:</label>
          <input v-model="editedNewspaperprint.printing_house" type="text" id="printing_house" required>
        </div>

        <div class="form-group">
          <label for="circulation">Тираж:</label>
          <input v-model="editedNewspaperprint.circulation" type="number" id="circulation" required>
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
        editedNewspaperprint: {
          newspaper: '',
          printing_house: '',
          circulation: '',
        },
      };
    },
    methods: {
      async fetchNewspaperprintDetails() {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/newspaperprints/${this.$route.params.id}/`);
          this.editedNewspaperprint = response.data;
        } catch (error) {
          console.error(error);
        }
      },
      async saveChanges() {
        try {
          await axios.put(`http://127.0.0.1:8000/api/newspaperprints/${this.$route.params.id}/`, this.editedNewspaperprint);
          // В случае успешного сохранения, вы можете выполнить дополнительные действия, например, перенаправление на страницу с деталями
          this.$router.push({ name: 'NewsPaperPrintDetails', params: { id: this.$route.params.id }});
        } catch (error) {
          console.error(error);
        }
      },
    },
    created() {
      this.fetchNewspaperprintDetails();
    },
    computed: {
      isValidForm() {
        return (
          this.editedNewspaperprint.newspaper &&
          this.editedNewspaperprint.printing_house &&
          this.editedNewspaperprint.circulation
        );
      },
    },
  };
  </script>
  
  <style scoped>
  .edit-newspaperprint {
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
  