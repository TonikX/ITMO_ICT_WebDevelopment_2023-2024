<template>
<div>
 <div class="service" v-for="service in salonServices"> <!-- v-for - директива для отображения списка элементов на основе массива. -->
   <div class="service"><strong>Name:</strong> {{ service.name }}</div>
   <div class="service"><strong>Description:</strong> {{ service.description }}</div>
 </div>
</div>
</template>

<script>
export default {
 props: {
   salonServices: {
     type: Array,
     required: true
   }
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