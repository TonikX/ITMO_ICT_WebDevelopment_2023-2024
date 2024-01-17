<template>
     <div>
          
     <div v-for="project in projects" :key="project.id" class="card">
          <h3>{{ project.name }}</h3>
          <p>{{ project.description }}</p>
          <p><strong>Руководитель:</strong> {{ project.creator }}</p>
          <!-- <p><strong>Оценка сложности:</strong> {{ project.complexity }}</p> -->
          <!-- <p><strong>Web-технологии:</strong> {{ project.technologies }}</p> -->
          <div class="buttons">
               <!--  -->
               <button @click="rateProject(project.id, 'очень не хочу')" :class="{ 'active': this.choose[project.id] === 'очень не хочу' }">Очень не хочу</button>
               <button @click="rateProject(project.id, 'не хочу')" :class="{ 'active': this.choose[project.id] === 'не хочу' }">Не хочу</button>
               <button @click="rateProject(project.id, 'нейтрально')" :class="{ 'active': this.choose[project.id] === 'нейтрально' }">Нейтрально</button>
               <button @click="rateProject(project.id, 'хочу')" :class="{ 'active': this.choose[project.id] === 'хочу' }">Хочу</button>
               <button @click="rateProject(project.id, 'очень хочу')" :class="{ 'active': this.choose[project.id] === 'очень хочу' }">Очень хочу</button>
          </div>
     </div>
     <button @click="saveSelection()">Сохранить выбор</button>
     </div>
    </template>
    
    <script>
    import axios from 'axios';

    export default {
     data() {
          return {
               projects: [
                    // {
                    // id: 1,
                    // name: "Проект 1",
                    // description: "Описание проекта 1",
                    // manager: "Иван Иванов",
                    // complexity: 5,
                    // technologies: "Vue.js, HTML, CSS"
                    // },
                    // {
                    // id: 2,
                    // name: "Проект 2",
                    // description: "Описание проекта 2",
                    // manager: "Анна Смирнова",
                    // complexity: 3,
                    // technologies: "React.js, Node.js, MongoDB"
                    // },
                    // Другие проекты...
               ],
               choose: {},
          };
     },
     methods: {
          rateProject(id, rating) {
               // Здесь можно добавить логику обработки выбора пользователя
               this.choose[id] = rating;     
               console.log(`Вы выбрали оценку "${rating}" для проекта с ID ${id}`);
               for(var key in this.choose) {
                    console.log(key + " : " + this.choose[key]);
               }
          },
          saveSelection() {
               // Сохранение выборов студента в БД (пример)
               // Может потребоваться использование axios.post или других методов для отправки данных на сервер
               console.log('Выборы студента:');
               for(var key in this.choose) {
                    console.log(key + " : " + this.choose[key]);
               }    
          },
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
     created() {
          this.fetchProjectData();
     },
     };
    </script>
    
    <style>
    .card {
     margin-bottom: 20px;
     padding: 10px;
     border: 1px solid #ccc;
    }
    
    .buttons {
     margin-top: 10px;
    }
    
    .buttons button {
     margin-right: 5px;
    }

    .active {
          text-decoration: underline;
          /* color: #f8fa87; */
     }
    </style>