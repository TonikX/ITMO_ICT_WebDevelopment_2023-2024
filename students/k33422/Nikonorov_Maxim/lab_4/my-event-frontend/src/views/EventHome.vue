<template>
    <div>
      <EventList />
    </div>
  </template>
  
  <script>
  import EventList from '@/components/EventList.vue';
  
  export default {
    components: {
      EventList,
    },
  };
  </script>
  
  <style scoped>
  .event-list {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .event-cards {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: space-between;
  }
  
  .event-card {
    background-color: #d8e9ff;
    border: 1px solid #4682b4;
    border-radius: 10px;
    padding: 15px;
    width: calc(25% - 20px);
    box-sizing: border-box;
    margin-bottom: 20px;
  }
  
  h1 {
    font-family: 'Poppins';
    color: #0066cc;
    text-align: center;
  }
  
  h2 {
    font-family: 'Poppins';
    color: #003366;
    margin-bottom: 10px;
  }
  
  p {
    font-family: 'Poppins';
    color: #333;
    margin-bottom: 5px;
  }
  </style>
  
  