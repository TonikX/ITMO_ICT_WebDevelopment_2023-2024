<template>
    <div>
      <h1 class="title">Set goals.<br>Have a ten-year plan.<br>Invest.<br>Wake up early.<br>CEO mindset</h1>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Home',
  };
  </script>
  
  <style scoped>
  .title {
    color: #f8ff39;
    text-align: center;
    margin-top: 50vh;
    transform: translateY(-100%);
    animation: flicker 0.5s steps(1) infinite;
  }

  @keyframes flicker {
  0% { opacity: 1; }
  50% { opacity: 0; }
  100% { opacity: 1; }
}

@keyframes colorShift {
  0% { background-color: #f500ff; }
  50% { background-color: #f500ff; }
  100% { background-color: #f500ff; }
}

  </style>
  