
<template>
    <div class="container">
        <div class = "animals-text">
      <h2> Животные </h2>
        <p> Здесь вы можете посмотреть наших животных. Воспользуйтесь поиском, чтобы найти нужное животное. </p>
    </div>
      <div v-if="isLoggedIn && animals.length">
        <div class="search-container">

        
        </div>
  
        <table class="animal-table">
          <thead>
            <tr>
              <th>Имя</th>
              <th>Возраст (лет)</th>
              <th>Пол</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="animal in filteredAnimals" :key="animal.id">
              <td>{{ animal.name }}</td>
              <td>{{ animal.age }}</td>
              <td>{{ animal.sex }}</td>
            </tr>
          </tbody>
        </table>     
         <br/>
        <div> Поиск по животным: </div>
        <br/>

<input type="text" v-model="searchTerm" id="search" />
      </div>
  
      <div v-else-if="isLoggedIn">
        <p> На данный момент нет животных. </p>
      </div>
    </div>
  </template>
  
  <script>
  
  import axios from 'axios';
  
  export default {
    data() {
      return {
        animals: [],
        searchTerm: '',
      };
    },
    methods: {
      async fetchAnimalData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/system/animals/', {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          this.animals = response.data;
        } catch (error) {
          console.error('Error fetching animal data:', error);
        }
      },
    },
    computed: {
      isLoggedIn() {
        return localStorage.getItem('access_token') !== null;
      },
      filteredAnimals() {
        return this.animals.filter(animal =>
          animal.name.toLowerCase().includes(this.searchTerm.toLowerCase())
        );
      },
    },
    created() {
      this.fetchAnimalData();
    },
  };
  </script>
  
  <style scoped>

template { 
    font-family: Arial, Helvetica, sans-serif;
    text-align: center;
    color:  #ffffff;

}
.container {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.animals-text {
  background-color: #f7f7f7;
  border-radius: 10px;
  padding: 20px;
  margin: 20px 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.animals-text h2 {
    color: #333;
    margin: 0 0 20px;
}

  
  .search-container {
    margin-bottom: 15px;
  }
  
  #search {
    padding: 8px;
    margin-left: 5px;
  }
  
  .animal-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
  }
  
  .animal-table th, .animal-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
    background-color: #f2f2f2;

  }

  .animal-table td:hover 
  {
    background-color: #ffff99;
    cursor: pointer;
  }

  
  </style>
  