<template>
  <div>

    <div class="add-print-run-form text-center">
      <h3>Добавить новый тираж</h3>
      <form @submit.prevent="addPrintRun">
        <div class="form-group">
          <label for="copiesCount">Количество копий</label>
          <input v-model="printRunForm.copies_count" type="number" placeholder="Количество копий" class="form-control"
                 id="copiesCount" required/>
        </div>
        <div class="form-group">
          <label for="newspaper">Газета</label>
          <select v-model="printRunForm.newspaper" class="form-control" id="newspaper" required>
            <option v-for="newspaper in newspapers" :key="newspaper.id" :value="newspaper.id">{{
                newspaper.name
              }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label for="printingHouse">Печатное предприятие</label>
          <select v-model="printRunForm.printing_house" class="form-control" id="printingHouse" required>
            <option v-for="printingHouse in printingHouses" :key="printingHouse.id" :value="printingHouse.id">
              {{ printingHouse.name }}
            </option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Добавить</button>
      </form>
    </div>

    <ul class="print-run-list">
      <li v-for="printRun in printRuns" :key="printRun.id" class="list-group-item">
        <h4>{{ printRun.copiesCount }}</h4>
        <p><strong>Газета:</strong> {{ getNewspaperName(printRun.newspaper) }}</p>
        <p><strong>Типография:</strong> {{ getPrintingHouseName(printRun.printing_house) }}</p>
        <p><strong>Размер тиража:</strong> {{ printRun.copies_count }}</p>
        <button @click="deletePrintRun(printRun.id)" class="delete_button btn btn-danger">Удалить</button>
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
      newspapers: [],
      printingHouses: [],
      printRuns: [],
      printRunForm: {
        copies_count: '',
        newspaper: '',
        printing_house: '',
      },
    };
  },

  mounted() {
    this.fetchNewspapers();
    this.fetchPrintingHouses();

    this.fetchPrintRuns();
  },
  methods: {
    getNewspaperName(newspaperId) {
      const newspaper = this.newspapers.find(n => n.id === newspaperId);
      return newspaper ? newspaper.name : 'Неизвестно';
    },
    getPrintingHouseName(printingHouseId) {
      const printingHouse = this.printingHouses.find(ph => ph.id === printingHouseId);
      return printingHouse ? printingHouse.name : 'Неизвестно';
    },
    fetchNewspapers() {
      fetch('http://127.0.0.1:8000/newspapers/')
          .then(response => response.json())
          .then(data => (this.newspapers = data))
          .catch(error => console.error('Ошибка при получении списка газет:', error));
    },
    fetchPrintingHouses() {
      fetch('http://127.0.0.1:8000/printinghouses/')
          .then(response => response.json())
          .then(data => (this.printingHouses = data))
          .catch(error => console.error('Ошибка при получении списка печатных предприятий:', error));
    },
    fetchPrintRuns() {
      fetch('http://127.0.0.1:8000/printruns/')
          .then(response => response.json())
          .then(data => (this.printRuns = data))
          .catch(error => console.error('Ошибка при получении списка тиражей:', error));
    },
    deletePrintRun(id) {
      const confirmation = confirm('Вы уверены, что хотите удалить тираж?');
      if (!confirmation) {
        return;
      }

      fetch(`http://127.0.0.1:8000/printruns/${id}/`, {
        method: 'DELETE',
      })
          .then(response => {
            if (response.ok) {
              this.printRuns = this.printRuns.filter(print => print.id !== id);
              console.log(`Print runs with id ${id} deleted successfully.`);
            } else {
              console.error(`Error deleting printRuns with id ${id}: ${response.statusText}`);
            }
          })
          .catch(error => console.error(`Error deleting printRuns with id ${id}: ${error}`));
    },
    addPrintRun() {
      console.log('Print Run data:', JSON.stringify(this.printRunForm));

      fetch('http://127.0.0.1:8000/printruns/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.printRunForm),
      })
          .then(response => response.json())
          .then(data => {
            this.printRunForm = {
              copies_count: '',
              newspaper: '',
              printing_house: '',
            };
            console.log('Print Run added successfully:', data);
            this.fetchPrintRuns();
          })
          .catch(error => console.error('Error adding Print Run:', error));
    },
  },
};
</script>

<style scoped>
.add-print-run-form {
  text-align: center;
  max-width: 600px;
  padding-top: 20px;
  padding-bottom: 20px;
  margin: auto;
}

.add-print-run-form .form-group {
  margin-bottom: 15px;
}

.add-print-run-form label {
  display: block;
  margin-bottom: 5px;
}

.add-print-run-form select {
  width: 100%;
  padding: 8px;
  font-size: 16px;
}

.search-bar {
  text-align: center;
  max-width: 600px;
  padding-top: 20px;
  padding-bottom: 20px;
  margin: auto;
}

.print-run-list {
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

.delete_button {
  margin-top: 20px;
}
</style>
