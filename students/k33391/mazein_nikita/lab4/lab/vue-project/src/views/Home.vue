<template>
    <div>
      <h1 class="title">Stock, Click, and Two Smoking Barcodes</h1>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Home',
  };
  </script>
  
  <style scoped>
  .title {
    text-align: center;
    margin-top: 50vh;
    transform: translateY(-50%);
    animation: fadeIn 1.5s ease-in-out;
  }
  
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
  </style>
  