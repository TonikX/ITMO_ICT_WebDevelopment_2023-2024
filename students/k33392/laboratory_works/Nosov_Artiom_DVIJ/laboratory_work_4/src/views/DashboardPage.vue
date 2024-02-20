
<template>
    <div class="container">
        <div>
            <!-- <div>{{ projects }}</div> -->
            <div>Количество проектов: {{ projects.length }}</div>
            <div>Количество активных проектов: {{ activeProjects.length }}</div>
            <div>Количество завершённых проектов: {{ projects.length-activeProjects.length }}</div>
        </div>
        <div>
            <!-- <div>{{ students }}</div> -->
            <div>Количество студентов: {{ students.length }}</div>
        </div>
        <div>
            <div>
                <!-- <div>{{ topics }}</div> -->
                <div>Количество тем: {{ topics.length }}</div>
            </div>
        </div>
    </div>
</template>
  
  <script>
  
  import axios from 'axios';
  
  export default {
    data() {
      return {
        projects: [],
        students: [],
        topics: [],
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
      async fetchStudentData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/student/list/', {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          this.students = response.data.results;
        } catch (error) {
          console.error('Error fetching student data:', error);
        }
      },
      async fetchTopicData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/topic/list/', {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          this.topics = response.data.results;
        } catch (error) {
          console.error('Error fetching topic data:', error);
        }
      },
    },
    computed: {
      isLoggedIn() {
        return localStorage.getItem('access_token') !== null;
      },
      activeProjects() {
        var date = new Date();
        return this.projects.filter(project =>
        Date.parse(project.start_date) <= date &&
          Date.parse(project.end_date) >= date
        );
      },
    },
    created() {
      this.fetchProjectData();
      this.fetchStudentData();
      this.fetchTopicData();
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
  