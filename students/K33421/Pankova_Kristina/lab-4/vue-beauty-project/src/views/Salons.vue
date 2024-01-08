<template>
  <div class="app">

    <button v-on:click="CreateSalon" class="button">Register a new salon</button>

    <div v-if="showComponent === 'CreateSalon'">
        <salon-form class="form" />
    </div>

    <h1 class="title">Registered salons: </h1>
    <button v-on:click="fetchSalons" class="button">Get a list of all salons</button>
    <salon-list v-bind:salons="salons" />
  </div>
</template>

<style>
.app {
  font-family: Arial, sans-serif;
  padding: 20px;
}

.title {
  color: #333;
  font-size: 24px;
  margin-bottom: 20px;
}

.button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.form {
  margin-bottom: 20px;
}

.list {
  border: 1px solid #ccc;
  padding: 10px;
}
</style>

<script>
import SalonForm from "@/components/SalonForm.vue";
import SalonList from "@/components/SalonList.vue";
import axios from "axios";

export default {
 components: {
   SalonForm, SalonList
 },

 data() { // data - это функция, которая возвращает объект с данными
   return {
     salons: [], // Массив данных (передается в компонент SalonList, получает данные средствами функции fetchSalons
     showComponent: null
   }
 },


 methods: { // methods. Это объект, который содержит список Javascript функций, которые должны выполняться в зависимости от того, какие действия производит пользователь.
   async fetchSalons () { // асинхронная функция для получения данных
     try {
       const response = await axios.get('http://127.0.0.1:8000/salon/salons/') // Выполнение GET-запроса Backend-серверу. Запрос вернет JSON.
       console.log(response.data.results)
       console.log(response)
       this.salons = response.data // Массив данных salons из блока(функции) data() получает значением результат только-что выполненного запроса
     } catch (e) {
       alert('Ошибка')
     }
   },
    CreateSalon() {
      this.showComponent = 'CreateSalon';
    },

 },
 mounted() {
 //  this.fetchSalons() // Vue вызывает хук mount(), когда компонент добавляется в DOM.  В данном примере это позволяет вызвать fetchSalons для получения списка воинов до отрисовки страницы в браузере, благодаря этому страница загружается с уже полученными ранее данными.
 }
}
</script>
