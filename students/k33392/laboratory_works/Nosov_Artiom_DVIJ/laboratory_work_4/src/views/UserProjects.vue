
<template>
    <!-- {{ getProjectOfUserRel(project)      }} -->
            <!-- {{ info }}
            {{ project_show }} -->
            <!-- {{ projectOfUserList }} -->
    <div class="container" v-if="project_show === null">
        <div class = "projects-text">
      <h2> Проекты </h2>
        <p> Здесь представлены проекты, в которых вы участвуете. Воспользуйтесь поиском, чтобы найти нужный проект. 
            Чтобы посмотреть информацию о проекте, нажмите на него</p>
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
              <th>Ваша роль</th>
            </tr>
          </thead>
          <tbody>
            <tr @click="project_show=project" v-for="project in filteredProjects" :key="project.id">
              <td>{{ project.name }}</td>
              <td>{{ project.description }}</td>
              <td>{{ project.creator.name }}</td>
              <td>{{ rolesDict[project.id] }}</td>
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

    <div v-else class="container">
        <!-- {{ project_show }} -->
        <div>
            <h1>Основная информация</h1>
            <div>Номер проекта: {{ project_show.id }}</div>
            <div>Навание проекта: {{ project_show.name }}</div>
            <div>Описание: {{ project_show.description }}</div>
            <div>Технологии: <div v-for="topic in project_show.topics" :key="topic.id">{{ topic.name }}</div></div>
            <div>Создатель проекта: {{ project_show.creator.name }}</div>
            <div>Дата создания проекта: {{ project_show.created }}</div>
            <div>Дата изменения проекта: {{ project_show.updated }}</div>
            <div>Дата начала проекта: {{ project_show.start_date }}</div>
            <div>Дата окончания проекта: {{ project_show.end_date }}</div>
        </div>
        <div calss="participants">
            <h1>Участники проекта</h1>
            <!-- <div>{{ projectOfUserListParticipants }}</div> -->
            <table class="project-table">
            <thead>
            <tr>
              <th>ФИО</th>
              <th>Роль</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="projectOfUserListParticipant in projectOfUserListParticipants" :key="projectOfUserListParticipant.id">
              <td>{{ projectOfUserListParticipant.user_field.name }}</td>
              <td>{{ projectOfUserListParticipant.name }}</td>
            </tr>
          </tbody>
        </table>
        </div>
        <button @click="project_show=null">
            Назад к выбору проектов
        </button>
    </div>
  </template>
  
  <script>
  
  import axios from 'axios';
  
  export default {
    data() {
      return {
        info: [],
        projects: [],
        projectOfUserList: [],
        getProjectOfUserRelList: [],
        projectOfUserListParticipants: [],
        rolesDict: {},
        project_show: null, 
        searchTerm: '',
      };
    },
    methods: {
      async fetchData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/project/my', 
          {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          this.info = response.data.result;
          this.projects = this.info['projects']
          this.projectOfUserList = this.info['projectOfUserList']
        //   console.error(`TEEEEEEEST: ${response.data}`);
        } catch (error) {
          console.error(`Error fetching data: `);
        }
        
        try {
          const response = await axios.get('http://127.0.0.1:8000/project/participants', 
          {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          this.projectOfUserListParticipants = response.data.result['projectOfUserListParticipants'];

        } catch (error) {
          console.error(`Error fetching data: `);
        }
      },
      getRoles() {
        for (let project of this.projects) {
            let res = this.projectOfUserList.filter(projectOfUser =>
                projectOfUser.project_field === project.id
            );
            let str_buf = '';
            for (let ttt of res) {
                str_buf += ttt.name + ' ';
            }
            this.rolesDict[project.id] = str_buf;
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
    async created() {
      await this.fetchData();
      this.getRoles();
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
  