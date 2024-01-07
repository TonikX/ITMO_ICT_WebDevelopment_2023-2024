<template>
  <div>

    <div class="add-printing-house-form text-center">
      <h3>Добавить новую типографию</h3>
      <form @submit.prevent="addPrintingHouse">
        <div class="form-group">
          <input v-model="printingHouseForm.name" type="text" placeholder="Название типографии" class="form-control"
                 id="printingHouseName" required/>
        </div>
        <div class="form-group">
          <input v-model="printingHouseForm.address" type="text" placeholder="Адрес" class="form-control"
                 id="printingHouseAddress" required/>
        </div>
        <div class="form-group">
          <input v-model="printingHouseForm.status" type="text" placeholder="Статус" class="form-control" id="status"
                 required/>
        </div>
        <button type="submit" class="btn btn-primary">Добавить</button>
      </form>
    </div>

    <div class="search-bar text-center">
      <h3>Список типографий</h3>
      <div class="input-group">
        <input v-model="searchQuery" type="text" class="form-control" placeholder="Поиск по названию типографии"/>
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" @click="searchPrintingHouses">Искать</button>
        </div>
      </div>

      <div class="sorting-dropdown">
        <label for="sortSelect">Сортировать тираж по:</label>
        <select v-model="sortOrder" id="sortSelect" class="form-control">
          <option value="asc">По возрастанию</option>
          <option value="desc">По убыванию</option>
        </select>
      </div>
    </div>


    <ul class="printing-house-list">
      <li v-for="printingHouse in filteredPrintingHouses" :key="printingHouse.id" class="list-group-item">
        <h4>{{ printingHouse.name }}</h4>
        <p><strong>Адрес:</strong> {{ printingHouse.address }}</p>
        <p><strong>Статус:</strong> {{ printingHouse.status }}</p>


        <div v-if="printingHouse.newspapers.length > 0">
          <p><strong>Газеты:</strong></p>
          <ul>
            <li v-for="newspaper in printingHouse.newspapers" :key="newspaper.newspaper_name">
              {{ newspaper.newspaper_name }} - {{ newspaper.copies_count }}
            </li>
          </ul>
        </div>
        <p v-else>Данная типография еще не печатает газеты</p>
        <button @click="deletePrintingHouse(printingHouse.id)" class="delete_button btn btn-danger">Удалить</button>

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
      printingHouses: [],
      searchQuery: '',
      sortOrder: 'asc',
      printingHouseForm: {
        name: '',
        address: '',
        status: '',
      },
    };
  },
  computed: {
    filteredPrintingHouses() {
      let filteredHouses = this.printingHouses.filter(printingHouse =>
          printingHouse.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
      const orderMultiplier = this.sortOrder === 'asc' ? 1 : -1;
      filteredHouses.sort((a, b) =>
          orderMultiplier * (a.newspapers.reduce((acc, curr) => acc + curr.copies_count, 0) -
              b.newspapers.reduce((acc, curr) => acc + curr.copies_count, 0))
      );

      return filteredHouses;
    },
  },
  mounted() {
    this.fetchPrintingHouses();
  },
  methods: {
    deletePrintingHouse(id) {
      const confirmation = confirm('Вы уверены, что хотите удалить типографию?');
      if (!confirmation) {
        return;
      }

      fetch(`http://127.0.0.1:8000/printinghouses/${id}/`, {
        method: 'DELETE',
      })
          .then(response => {
            if (response.ok) {
              this.printingHouses = this.printingHouses.filter(printingHouse => printingHouse.id !== id);
              console.log(`Printing house with id ${id} deleted successfully.`);
            } else {
              console.error(`Error deleting printing house with id ${id}: ${response.statusText}`);
            }
          }).catch(error => console.error(`Error deleting printing house with id ${id}: ${error}`));
    },


    fetchPrintingHouses() {
      fetch('http://127.0.0.1:8000/printinghouses/list')
          .then(response => response.json())
          .then(data => (this.printingHouses = data))
          .catch(error => console.error('Ошибка при получении списка типографий:', error));
    },
    addPrintingHouse() {

      fetch('http://127.0.0.1:8000/printinghouses/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.printingHouseForm),
      })
          .then(response => response.json())
          .then(data => {
            console.log('Printing house added successfully:', data);
            this.printingHouseForm = {
              name: '',
              address: '',
              status: '',
            };
            this.fetchPrintingHouses();
          })
          .catch(error => console.error('Error adding printing house:', error));
    },
    searchPrintingHouses() {
      this.fetchPrintingHouses();
    },
  },
};
</script>

<style scoped>
.printing-house-list {
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

.add-printing-house-form {
  list-style: none;
  padding: 0;
  max-width: 600px;
  margin: auto;
}

.add-printing-house-form .form-group {
  margin-bottom: 15px;
}


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


.delete_button {
  margin-top: 20px;
}
</style>