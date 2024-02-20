
<template>
    <div class="container">
        <div class = "projects-text">
      <h2> Проекты </h2>
        <p> Здесь вы можете посмотреть наши проекты. Воспользуйтесь поиском, чтобы найти нужный проект. </p>
    </div>
      <div v-if="isLoggedIn && projects.length">
        <div class="search-container">

        
        </div>
  
        <table class="project-table">
          <thead>
            <tr>
              <th>Название</th>
              <th>Описание</th>
              <th>Создатель</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="project in filteredProjects" :key="project.id">
              <td>{{ project.name }}</td>
              <td>{{ project.description }}</td>
              <td>{{ project.creator }}</td>
            </tr>
          </tbody>
        </table>     
         <br/>
        <div> Поиск по проектам: </div>
        <br/>

<input type="text" v-model="searchTerm" id="search" />
      </div>
  
      <div v-else-if="isLoggedIn">
        <p> На данный момент нет проектов. </p>
      </div>
    </div>
  </template>
  
  <script>
  
  import axios from 'axios';
  
  export default {
    data() {
      return {
        projects: [],
        searchTerm: '',
      };
    },
    methods: {
      async fetchProjectData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/project/list/', {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          this.projects = response.data.results;
        } catch (error) {
          console.error('Error fetching project data:', error);
        }
      },
    },
    computed: {
      isLoggedIn() {
        return localStorage.getItem('access_token') !== null;
      },
      filteredProjects() {
        return this.projects.filter(project =>
          project.name.toLowerCase().includes(this.searchTerm.toLowerCase())
        );
      },
    },
    created() {
      this.fetchProjectData();
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

.projects-text {
  background-color: #f7f7f7;
  border-radius: 10px;
  padding: 20px;
  margin: 20px 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.projects-text h2 {
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
  
  .project-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
  }
  
  .project-table th, .project-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
    background-color: #f2f2f2;

  }

  .project-table td:hover 
  {
    background-color: #ffff99;
    cursor: pointer;
  }

  
  </style>
  