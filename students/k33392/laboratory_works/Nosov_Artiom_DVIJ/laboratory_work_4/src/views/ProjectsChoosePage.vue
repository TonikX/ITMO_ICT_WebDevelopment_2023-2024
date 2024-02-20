<template>
               <!-- {{ voteList }} -->
     <div>
     <div v-for="project in projects" :key="project.id" class="card" v-if="this.selectionStatus==='' || this.selectionStatus==='AlreadyFill'">
          <h3>{{ project.name }}</h3>
          <p>{{ project.description }}</p>
          <p><strong>Руководитель:</strong> {{ project.creator }}</p>
          <!-- <p><strong>Оценка сложности:</strong> {{ project.complexity }}</p> -->
          <p><strong>Технологии:</strong> {{ project.topics }}</p> 
          <div class="buttons">
               <!--  -->
               <button @click="rateProject(project.id, 'очень не хочу')" :class="{ 'active': this.choose[project.id] === 'очень не хочу' }">Очень не хочу</button>
               <button @click="rateProject(project.id, 'не хочу')" :class="{ 'active': this.choose[project.id] === 'не хочу' }">Не хочу</button>
               <button @click="rateProject(project.id, 'нейтрально')" :class="{ 'active': this.choose[project.id] === 'нейтрально' }">Нейтрально</button>
               <button @click="rateProject(project.id, 'хочу')" :class="{ 'active': this.choose[project.id] === 'хочу' }">Хочу</button>
               <button @click="rateProject(project.id, 'очень хочу')" :class="{ 'active': this.choose[project.id] === 'очень хочу' }">Очень хочу</button>
          </div>
     </div>
     <div v-if="this.selectionStatus==='NotAllSelect'">
          Вы не выбрали степень вашего желания на всех требуемых проектах!
     </div>
     <div v-else-if="this.selectionStatus==='AllSelected'">
          Ваш выбор сохранён!
     </div>
     <div v-else-if="this.selectionStatus==='AllSelectedEdit'">
          Ваши изменения сохранены!
     </div>
     <button @click="saveSelection()" v-else v-if="this.selectionStatus !== 'AlreadyFill'">Сохранить выбор</button>
     <button @click="editSelection()" v-else>Изменить выбор</button>
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
               selectionStatus: '',
               voteList: [],
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
               console.log(Object.keys(this.choose).length);
               if (Object.keys(this.choose).length < this.projects.length) {
                    this.selectionStatus = 'NotAllSelect';
                    return;
               }
               console.log('Выборы студента:');
               for(var key in this.choose) {
                    console.log(key + " : " + this.choose[key]);
                    try {
                         const response = axios.post('http://127.0.0.1:8000/project/vote/', 
                              {
                                   project_id: key,
                                   vote: this.choose[key],
                              },
                              {
                                   headers: {
                                        'Authorization': `Token ${localStorage.getItem('access_token')}`,
                                   },
                              },
                         );
                         
                    } catch (error) {
                         console.error('Ошибка при выборе проекта: ', error);
                    }
               }    
               this.selectionStatus = 'AllSelected';
          },
          editSelection() {
               // Сохранение выборов студента в БД (пример)
               // Может потребоваться использование axios.post или других методов для отправки данных на сервер
               console.log(Object.keys(this.choose).length);
               if (Object.keys(this.choose).length < this.projects.length) {
                    this.selectionStatus = 'NotAllSelect';
                    return;
               }
               console.log('Выборы студента:');
               for(var key in this.choose) {
                    console.log(key + " : " + this.choose[key]);
                    try {
                         const response = axios.post('http://127.0.0.1:8000/project/vote/', 
                              {
                                   project_id: key,
                                   vote: this.choose[key],
                              },
                              {
                                   headers: {
                                        'Authorization': `Token ${localStorage.getItem('access_token')}`,
                                   },
                              },
                         );
                         
                    } catch (error) {
                         console.error('Ошибка при выборе проекта: ', error);
                    }
               }    
               this.selectionStatus = 'AllSelectedEdit';
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
          async fetchVoteData() {
               try {
                    const response = await axios.get('http://127.0.0.1:8000/project/vote/', {
                    headers: {
                    Authorization: `Token ${localStorage.getItem('access_token')}`,
                    },
                    });
                    this.voteList = response.data.result.votes;
               } catch (error) {
                    console.error('Error fetching project data:', error);
               }
          },
          async initChoose() {
               for(let elem of this.voteList) {
                    this.choose[elem.project_field.id] = elem.name;
               }
               if(this.voteList.length >= this.projects.length) {
                    this.selectionStatus = 'AlreadyFill';
               }
          },
     },
     async created() {
          await this.fetchProjectData();
          await this.fetchVoteData();
          await this.initChoose();
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