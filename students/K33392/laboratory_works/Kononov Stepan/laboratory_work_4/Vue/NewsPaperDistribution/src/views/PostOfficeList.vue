<template>
  <div>

    <div class="add-post-office-form text-center">
      <h3>Добавить новое почтовое отделение</h3>
      <form @submit.prevent="addPostOffice">
        <div class="form-group">
          <input v-model="postOfficeForm.number" type="text" placeholder="Номер отделения" class="form-control"
                 id="postOfficeNumber" required/>
        </div>
        <div class="form-group">
          <input v-model="postOfficeForm.address" type="text" placeholder="Адрес отделения" class="form-control"
                 id="postOfficeAddress" required/>
        </div>
        <button type="submit" class="btn btn-primary">Добавить</button>
      </form>
    </div>


    <div class="search-bar text-center">
      <h3>Список почтовых отделений</h3>
      <div class="input-group">
        <input v-model="searchQuery" type="text" class="form-control" placeholder="Поиск по номеру отделения"/>
        <div class="input-group-append">
          <button @click="" class="btn btn-outline-secondary" type="button">Искать</button>
        </div>
      </div>
    </div>

    <ul class="post-office-list">
      <li v-for="postOffice in filteredPostOffices" :key="postOffice.id" class="list-group-item">
        <h4>{{ postOffice.number }}</h4>
        <p><strong>Адрес отделения:</strong> {{ postOffice.address }}</p>
        <button @click="deletePostOffice(postOffice.id)" class="delete_button btn btn-danger">Удалить</button>
      </li>
    </ul>
  </div>
  <theme-switcher></theme-switcher>
</template>


<script>
import ThemeSwitcher from "@/components/ThemeSwitcher.vue";

export default {
  components: {ThemeSwitcher},
  data() {
    return {
      searchQuery: '',
      postOffices: [],
      postOfficeForm: {
        number: '',
        address: '',
      },
    };
  },
  computed: {
    filteredPostOffices() {
      return this.postOffices.filter(postOffice =>
          postOffice.number.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
  },
  mounted() {
    fetch('http://127.0.0.1:8000/postoffices/')
        .then(response => response.json())
        .then(data => (this.postOffices = data))
        .catch(error => console.error('Ошибка при получении списка почтовых отделений:', error));
  },
  methods: {
    deletePostOffice(id) {
      const confirmation = confirm('Вы уверены, что хотите удалить почтовое отделение?');
      if (!confirmation) {
        return;
      }

      fetch(`http://127.0.0.1:8000/postoffices/${id}/`, {
        method: 'DELETE',
      })
          .then(response => {
            if (response.ok) {
              this.postOffices = this.postOffices.filter(postOffice => postOffice.id !== id);
              console.log(`PostOffices with id ${id} deleted successfully.`);
            } else {
              console.error(`Error deleting postOffices with id ${id}: ${response.statusText}`);
            }
          })
          .catch(error => console.error(`Error deleting postOffices with id ${id}: ${error}`));
    },
    addPostOffice() {

      console.log('Post data:', JSON.stringify(this.postOfficeForm));

      fetch('http://127.0.0.1:8000/postoffices/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.postOfficeForm),
      })
          .then(response => response.json())
          .then(data => {
            this.postOfficeForm = {
              number: '',
              address: '',
            };
            console.log('Post Office added successfully:', data);
          })
          .catch(error => console.error('Error adding Post Office:', error));
    },
  },
};
</script>


<style scoped>
.search-bar {
  text-align: center;
  max-width: 600px;
  padding-top: 20px;
  padding-bottom: 20px;
  margin: auto;
}


.input-group-append {
  padding-left: 10px;
}

.post-office-list {
  list-style: none;
  padding: 0;
  max-width: 600px;
  margin: auto;
}


.list-group-item {
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}


.list-group-item:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.add-post-office-form {
  list-style: none;
  padding: 0;
  max-width: 600px;
  margin: auto;
}

.add-post-office-form .form-group {
  margin-bottom: 15px;
}

.delete_button {
  margin-top: 20px;
}
</style>