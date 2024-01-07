<template>
  <div>
    <div class="add-newspaper-form text-center">
      <h3>Добавить новую газету</h3>
      <form @submit.prevent="addNewspaper">
        <div class="form-group">
          <input v-model="newspaperForm.name" type="text" placeholder="Название газеты" class="form-control"
                 id="newspaperName" required/>
        </div>
        <div class="form-group">
          <input v-model="newspaperForm.edition_index" type="text" placeholder="Индекс выпуска" class="form-control"
                 id="editionIndex" required/>
        </div>
        <div class="form-group">
          <select v-model="newspaperForm.editor" class="form-control" id="editor" required>
            <option disabled selected value="">Редактор</option>
            <option v-for="editor in editors" :key="editor.id" :value="editor.id">
              {{ editor.first_name }} {{ editor.last_name }} {{ editor.middle_name }}
            </option>
          </select>
        </div>

        <div class="form-group">
          <input v-model="newspaperForm.price_per_copy" type="text" placeholder="Цена за копию" class="form-control"
                 id="pricePerCopy" required/>
        </div>
        <button type="submit" class="btn btn-primary">Добавить</button>
      </form>
    </div>

    <div class="search-bar text-center">
      <h3>Список газет</h3>
      <div class="input-group">
        <input v-model="searchQuery" type="text" class="form-control" placeholder="Поиск по названию газеты"/>
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button">Искать</button>
        </div>
      </div>
    </div>


    <ul class="newspaper-list">
      <li v-for="newspaper in filteredNewspapers" :key="newspaper.id" class="list-group-item">
        <h4>{{ newspaper.name }}</h4>
        <p><strong>Индекс выпуска:</strong> {{ newspaper.edition_index }}</p>
        <p><strong>Редактор:</strong> {{ newspaper.editor }}</p>
        <p><strong>Цена за копию:</strong> {{ newspaper.price_per_copy }} ₽</p>

        <div v-if="newspaper.printing_houses.length > 0">
          <p><strong>Типографии:</strong></p>
          <ul>
            <li v-for="printingHouse in newspaper.printing_houses" :key="printingHouse.id">
              {{ printingHouse.name }} - {{ printingHouse.address }}
            </li>
          </ul>
        </div>
        <div v-else>
          <p><em>Нет информации о печатных домах</em></p>
        </div>

        <div v-if="newspaper.post_offices.length > 0">
          <p><strong>Почтовые отделения:</strong></p>
          <ul>
            <li v-for="postOffice in newspaper.post_offices" :key="postOffice.id">
              {{ postOffice.number }} - {{ postOffice.address }}
            </li>
          </ul>
        </div>
        <div v-else>
          <p><em>Нет информации о почтовых отделениях</em></p>
        </div>
        <button @click="deleteNewspaper(newspaper.id)" class="delete_button btn btn-danger">Удалить</button>
      </li>
    </ul>
  </div>
  <theme-switcher></theme-switcher>

</template>

<script>
import ThemeSwitcher from "@/components/ThemeSwitcher.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  components: {NavBar, ThemeSwitcher},
  data() {
    return {
      editors: [],
      newspapers: [],
      searchQuery: '',
      newspaperForm: {
        name: '',
        edition_index: '',
        editor: '',
        price_per_copy: '',
      },
    };
  },
  computed: {
    filteredNewspapers() {
      return this.newspapers.filter(newspaper =>
          newspaper.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
  },
  mounted() {
    fetch('http://127.0.0.1:8000/editors')
        .then(response => response.json())
        .then(data => (this.editors = data))
        .catch(error => console.error('Ошибка при получении списка редакторов:', error));


    fetch('http://127.0.0.1:8000/newspapers/list')
        .then(response => response.json())
        .then(data => (this.newspapers = data))
        .catch(error => console.error('Ошибка при получении списка газет:', error));
  },

  methods: {
    deleteNewspaper(id) {
      const confirmation = confirm('Вы уверены, что хотите удалить газету?');
      if (!confirmation) {
        return;
      }

      fetch(`http://127.0.0.1:8000/newspapers/${id}/`, {
        method: 'DELETE',
      })
          .then(response => {
            if (response.ok) {
              this.newspapers = this.newspapers.filter(newspaper => newspaper.id !== id);
              console.log(`Newspaper with id ${id} deleted successfully.`);
            } else {
              console.error(`Error deleting newspaper with id ${id}: ${response.statusText}`);
            }
          })
          .catch(error => console.error(`Error deleting newspaper with id ${id}: ${error}`));
    },


    addNewspaper() {
      console.log('Post data:', JSON.stringify(this.newspaperForm));

      fetch('http://127.0.0.1:8000/newspapers/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.newspaperForm),
      })
          .then(response => response.json())
          .then(data => {
            this.newspaperForm = {
              name: '',
              edition_index: '',
              editor: '',
              price_per_copy: '',
            }
            console.log('Newspaper added successfully:', data);
          })
          .catch(error => console.error('Error adding newspaper:', error));
    }
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

.newspaper-list {
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

.add-newspaper-form {
  list-style: none;
  padding: 0;
  max-width: 600px;
  margin: auto;
}

.add-newspaper-form .form-group {
  margin-bottom: 15px;
}

.delete_button {
  margin-top: 20px;
}
</style>