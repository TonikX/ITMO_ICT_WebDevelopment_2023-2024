<template>
 <div class="salon" v-for="salon in salons"> <!-- v-for - директива для отображения списка элементов на основе массива. -->
   <div class="salon"><strong>Название:</strong> {{ salon.name }}</div>
   <div class="salon"><strong>Город:</strong> {{ salon.city }}</div>
 </div>
</template>

<script>
export default {
 props: { // «Props» -- это специальное ключевое слово, обозначающее свойства . Его можно зарегистрировать в дочернем компоненте для передачи данных от родительского компонента к одному из его дочерних компонентов.
   salons: {
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