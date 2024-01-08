<template>
 <div class="salon" v-for="salon in salons"> <!-- v-for - директива для отображения списка элементов на основе массива. -->
   <div class="salon"><strong>Название:</strong> {{ salon.name }}</div>
   <div class="salon"><strong>Город:</strong> {{ salon.city }}</div>

 </div>
</template>

<script>
import SalonServiceList from "@/components/SalonServiceList.vue";
import axios from 'axios';

export default {
 components: {
   SalonServiceList
 },
 props: {
   salons: {
     type: Array,
     required: true
   }
 },
   methods: {
    async fetchSalonServices(salonId) {
      const url = `http://127.0.0.1:8000/salon/${salonId}/services/`;
      axios
        .get(url)
        .then((response) => {
          this.salonServices = response.data;
          console.log(this.salonServices);
        })
        .catch((error) => {
          console.error(error);
          alert("Error fetching salon services");
        });
  },
},
 mounted() {
   this.fetchSalonServices(0) // Vue вызывает хук mount(), когда компонент добавляется в DOM.  В данном примере это позволяет вызвать fetchSalons для получения списка воинов до отрисовки страницы в браузере, благодаря этому страница загружается с уже полученными ранее данными.
 }

}
</script>

<style>
.salon {
  padding: 20px;
  margin: 10px;
    margin-top: 20px;

  border: 1px solid gray;
  padding: 8px;
    text-align: center;
  text-transform: uppercase;
  color: #4CAF50;
  text-indent: 50px;
  text-align: justify;
  letter-spacing: 3px;
text-decoration: none;
  color: #008CBA;
}


</style>