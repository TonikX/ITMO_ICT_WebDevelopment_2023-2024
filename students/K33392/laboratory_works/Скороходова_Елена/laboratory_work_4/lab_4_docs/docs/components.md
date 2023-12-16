##Компоненты

Были созданы Vue компоненты для страниц профиля, добавления самолетов, полетов, экипажа и сотрудников.

На примере Aircrafts.vue объясню работу компонентов:

Страница состоит из таблицы с уже записанными самолетам, и формы с добавлением нового самолета.

В секции скрипта, я определяю данные компонента, включая массив 
aircrafts для хранения списка воздушных судов и объект newAircraft 
для хранения данных нового воздушного судна.

mounted(): Хук жизненного цикла Vue.js. Когда компонент был добавлен в DOM, 
вызывается метод mounted. В этом методе происходит 
вызов другого метода fetchAircrafts(). 

Методы:
fetchAircrafts(): Выполняет GET-запрос к серверу для получения списка воздушных судов и обновляет данные в массиве aircrafts.

addAircraft(): Выполняет POST-запрос для добавления нового воздушного судна на сервер. После успешного добавления обновляет данные и сбрасывает значения полей формы.

deleteAircraft(aircraftId): Выполняет DELETE-запрос для удаления воздушного судна с указанным идентификатором на сервере. После успешного удаления обновляет данные.

    <template>
      <div>
        <h2>Aircraft List</h2>
        <table class="aircraft-table">
          <thead>
            <tr>
              <th>Number</th>
              <th>Type</th>
              <th>Seats</th>
              <th>Speed</th>
              <th>Carrier</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="aircraft in aircrafts" :key="aircraft.id">
              <td>{{ aircraft.number }}</td>
              <td>{{ aircraft.type }}</td>
              <td>{{ aircraft.seats }}</td>
              <td>{{ aircraft.speed }}</td>
              <td>{{ aircraft.carrier }}</td>
              <button @click="deleteAircraft(aircraft.id)">Delete</button>
            </tr>
          </tbody>
        </table>
    
        <h3>Add New Aircraft</h3>
        <form @submit.prevent="addAircraft" class="add-aircraft-form">
          <label>
            Number:
            <input v-model="newAircraft.number" type="text" required class="input-field" />
          </label>
          <label>
            Type:
            <input v-model="newAircraft.type" type="text" required class="input-field" />
          </label>
          <label>
            Seats:
            <input v-model="newAircraft.seats" type="number" required class="input-field" />
          </label>
          <label>
            Speed:
            <input v-model="newAircraft.speed" type="number" required class="input-field" />
          </label>
          <label>
            Carrier:
            <input v-model="newAircraft.carrier" type="text" required class="input-field" />
          </label>
          <button type="submit" class="add-button">Add Aircraft</button>
        </form>
        <div>
          <router-link to="/crewmembers">
            <button>Crew Members</button>
          </router-link>
          <router-link to="/flights">
            <button>Flights</button>
          </router-link>
          <router-link to="/employees">
            <button>Employees</button>
          </router-link>
          <router-link to="/profile">
            <button>Back to Profile</button>
          </router-link>
        </div>
      </div>
    </template>
    
    <script>
    import axios from 'axios';
    
    export default {
      data() {
        return {
          aircrafts: [],
          newAircraft: {
            number: '',
            type: '',
            seats: 0,
            speed: 0,
            carrier: '',
          },
        };
      },
      mounted() {
        this.fetchAircrafts();
      },
      methods: {
        fetchAircrafts() {
          axios.get('http://localhost:8000/my_avia_app/api/aircrafts/')
            .then(response => {
              this.aircrafts = response.data;
            })
            .catch(error => {
              console.error(error);
            });
        },
        addAircraft() {
          axios.post('http://localhost:8000/my_avia_app/api/aircrafts/', this.newAircraft)
            .then(() => {
              this.newAircraft = {
                number: '',
                type: '',
                seats: 0,
                speed: 0,
                carrier: '',
              };
              this.fetchAircrafts();
            })
            .catch(error => {
              console.error(error);
            });
        },
         deleteAircraft(aircraftId) {
          axios.delete(`http://localhost:8000/my_avia_app/api/aircrafts/${aircraftId}/`)
            .then(() => {
              this.fetchAircrafts();
            })
            .catch(error => {
              console.error(error);
            });
        },
      },
    };
    </script>
    
    <style scoped>
    
    .aircraft-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }
    
    .aircraft-table th,
    .aircraft-table td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }
    
    .aircraft-table th {
      background-color: #f4f4f4;
    }
    
    .add-aircraft-form {
      margin-top: 20px;
    }
    
    .input-field {
      width: 200px;
      padding: 8px;
      margin-bottom: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    
    
    button {
      background-color: #007BFF;
      color: #fff;
      padding: 10px 15px;
      border: none;
      border-radius: 3px;
      cursor: pointer;
    }
    
    button:hover {
      background-color: #0056b3;
    }
    </style>

