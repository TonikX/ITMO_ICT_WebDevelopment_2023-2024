<template>

  <div class="add-postal-arrival-form text-center">
    <h3>Добавить новое поступление</h3>
    <form @submit.prevent="addPostalArrival">
      <div class="form-group">
        <label for="copiesReceived">Количество поступивших копий</label>
        <input v-model="postalArrivalForm.copies_received" type="number" placeholder="Количество поступивших копий"
               class="form-control" id="copiesReceived" required/>
      </div>
      <div class="form-group">
        <label for="postOffice">Почтовое отделение</label>
        <select v-model="postalArrivalForm.post_office" class="form-control" id="postOffice" required>
          <option v-for="postOffice in postOffices" :key="postOffice.id" :value="postOffice.id">
            {{ postOffice.number }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="newspaperArrival">Газета</label>
        <select v-model="postalArrivalForm.newspaper" class="form-control" id="newspaperArrival" required>
          <option v-for="newspaper in newspapers" :key="newspaper.id" :value="newspaper.id">{{
              newspaper.name
            }}
          </option>
        </select>
      </div>
      <button type="submit" class="btn btn-primary">Добавить</button>
    </form>
  </div>

  <ul class="postal-arrival-list">
    <li v-for="postalArrival in postalArrivals" :key="postalArrival.id" class="list-group-item">
      <h4>{{ postalArrival.copies_received }} копий</h4>
      <p><strong>Почтовое отделение:</strong> {{ getPostOfficeNumber(postalArrival.post_office) }}</p>
      <p><strong>Газета:</strong> {{ getNewspaperName(postalArrival.newspaper) }}</p>
      <button @click="deletePostalArrival(postalArrival.id)" class="delete_button btn btn-danger">Удалить</button>
    </li>
  </ul>
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
      postalArrivals: [],
      postalArrivalForm: {
        copies_received: '',
        post_office: '',
        newspaper: '',
      },
      postOffices: [],
    };
  },

  mounted() {
    this.fetchNewspapers();
    this.fetchPrintingHouses();
    this.fetchPrintRuns();

    this.fetchPostOffices();
    this.fetchPostalArrivals();
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

    getPostOfficeNumber(postOfficeId) {
      const postOffice = this.postOffices.find(po => po.id === postOfficeId);
      return postOffice ? postOffice.number : 'Неизвестно';
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

    fetchPostOffices() {
      fetch('http://127.0.0.1:8000/postoffices/')
          .then(response => response.json())
          .then(data => (this.postOffices = data))
          .catch(error => console.error('Ошибка при получении списка почтовых отделений:', error));
    },

    fetchPostalArrivals() {
      fetch('http://127.0.0.1:8000/postalarrivals/')
          .then(response => response.json())
          .then(data => (this.postalArrivals = data))
          .catch(error => console.error('Ошибка при получении списка почтовых поступлений:', error));
    },

    deletePostalArrival(id) {
      const confirmation = confirm('Вы уверены, что хотите удалить поступление?');
      if (!confirmation) {
        return;
      }

      fetch(`http://127.0.0.1:8000/postalarrivals/${id}/`, {
        method: 'DELETE',
      })
          .then(response => {
            if (response.ok) {
              this.postalArrivals = this.postalArrivals.filter(pa => pa.id !== id);
              console.log(`Postal arrivals with id ${id} deleted successfully.`);
            } else {
              console.error(`Error deleting postalArrivals with id ${id}: ${response.statusText}`);
            }
          })
          .catch(error => console.error(`Error deleting postalArrivals with id ${id}: ${error}`));
    },

    addPostalArrival() {
      console.log('Postal Arrival data:', JSON.stringify(this.postalArrivalForm));

      fetch('http://127.0.0.1:8000/postalarrivals/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.postalArrivalForm),
      })
          .then(response => response.json())
          .then(data => {
            this.postalArrivalForm = {
              copies_received: '',
              post_office: '',
              newspaper: '',
            };
            console.log('Postal Arrival added successfully:', data);
            this.fetchPostalArrivals();
          })
          .catch(error => console.error('Error adding Postal Arrival:', error));
    },
  },
};
</script>


<style scoped>

.add-postal-arrival-form {
  text-align: center;
  max-width: 600px;
  padding-top: 20px;
  padding-bottom: 20px;
  margin: auto;
}

.add-postal-arrival-form .form-group {
  margin-bottom: 15px;
}

.add-postal-arrival-form label {
  display: block;
  margin-bottom: 5px;
}

.add-postal-arrival-form select {
  width: 100%;
  padding: 8px;
  font-size: 16px;
}

.postal-arrival-list {
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
