<template>
  <div class="edit-newspaper">
    <h2>Редактировать газету</h2>
    <form @submit.prevent="saveChanges">
      <div class="form-group">
        <label for="title">Название:</label>
        <input v-model="editedNewspaper.title" type="text" id="title" required>
      </div>

      <div class="form-group">
        <label for="edition_index">Индекс выпуска:</label>
        <input v-model="editedNewspaper.edition_index" type="text" id="edition_index" required>
      </div>

      <div class="form-group">
        <label for="editor_last_name">Фамилия редактора:</label>
        <input v-model="editedNewspaper.editor_last_name" type="text" id="editor_last_name" required>
      </div>

      <div class="form-group">
        <label for="editor_first_name">Имя редактора:</label>
        <input v-model="editedNewspaper.editor_first_name" type="text" id="editor_first_name" required>
      </div>

      <div class="form-group">
        <label for="editor_middle_name">Отчество редактора:</label>
        <input v-model="editedNewspaper.editor_middle_name" type="text" id="editor_middle_name">
      </div>

      <div class="form-group">
        <label for="price">Цена:</label>
        <input v-model="editedNewspaper.price" type="number" id="price" required>
      </div>

      <!-- Добавьте другие поля газеты, которые вы хотите редактировать -->

      <button :class="{ 'inactive-button': !isValidForm }" type="submit">Сохранить изменения</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      editedNewspaper: {
        title: '',
        edition_index: '',
        editor_last_name: '',
        editor_first_name: '',
        editor_middle_name: '',
        price: 0,
        // Добавьте другие поля газеты, которые вы хотите редактировать
      },
    };
  },
  methods: {
    async fetchNewspaperDetails() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/newspapers/${this.$route.params.id}/`);
        this.editedNewspaper = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async saveChanges() {
      try {
        await axios.put(`http://127.0.0.1:8000/api/newspapers/${this.$route.params.id}/`, this.editedNewspaper);
        // В случае успешного сохранения, вы можете выполнить дополнительные действия, например, перенаправление на страницу с деталями
        this.$router.push({ name: 'NewsPaperDetails', params: { id: this.$route.params.id }});
      } catch (error) {
        console.error(error);
      }
    },
  },
  created() {
    this.fetchNewspaperDetails();
  },
  computed: {
    isValidForm() {
      return (
        this.editedNewspaper.title &&
        this.editedNewspaper.edition_index &&
        this.editedNewspaper.editor_last_name &&
        this.editedNewspaper.editor_first_name &&
        this.editedNewspaper.price
      );
    },
  },
};
</script>

<style scoped>
.edit-newspaper {
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
