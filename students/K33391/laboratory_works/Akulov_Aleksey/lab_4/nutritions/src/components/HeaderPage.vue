<template>
  <header>
    <nav>
      <ul>
        <li><router-link to="/">Главная</router-link></li>
      </ul>
      </nav>

  </header>
</template>
<script>
export default {
  name: 'HeaderPage'
}
</script>
<style scoped>
header {
background: #f5f5f5;
padding: 10px 0;
}

nav ul {
list-style: none;
display: flex;
justify-content: center;
}

nav ul li {
margin: 0 15px;
}

nav ul li a {
text-decoration: none;
color: #333;
font-weight: bold;
}
</style>