<template>
    <header>
      <h1 class="logo">Stock&Lock</h1>
      <nav>
        <router-link to="/" class="nav-link" :class="{ 'active': $route.path === '/' }">Home</router-link>
        <router-link v-if="!isAuthPage()" to="/brokers" class="nav-link" :class="{ 'active': $route.path === '/brokers' }">Brokers</router-link>
        <router-link v-if="!isAuthPage()" to="/producers" class="nav-link" :class="{ 'active': $route.path === '/producers' }">Producers</router-link>
        <router-link v-if="!isAuthPage()" to="/products" class="nav-link" :class="{ 'active': $route.path === '/products' }">Products</router-link>
        <router-link v-if="!isAuthPage()" to="/cosignments" class="nav-link" :class="{ 'active': $route.path === '/cosignments' }">Cosignments</router-link>
        <router-link v-if="!isAuthenticated" to="/login" class="nav-link" :class="{ 'active': $route.path === '/login' }">Login</router-link>
        <router-link v-if="!isAuthenticated" to="/register" class="nav-link" :class="{ 'active': $route.path === '/register' }">Register</router-link>
        <router-link v-if="isAuthenticated" to="/profile" class="nav-link" :class="{ 'active': $route.path === '/profile' }">Profile</router-link>
        <button v-if="isAuthenticated" @click="logout" class="nav-link logout-button">Logout</button>
      </nav>
    </header>
  </template>
  
  <script>
  export default {
    name: 'Navbar',
    data() {
      return {
        isAuthenticated: false,
      };
    },
    methods: {
      isAuthPage() {
        const authPages = ['/login', '/register'];
        return authPages.includes(this.$route.path);
      },
      logout() {
        // Clear authentication token from local storage
        localStorage.removeItem('access_token');
  
        // Update the isAuthenticated status
        this.isAuthenticated = false;
  
        // Redirect to the login page
        this.$router.push('/login');
      },
    },
    created() {
      // Check if the user is already authenticated
      this.isAuthenticated = localStorage.getItem('access_token') !== null;
    },
  };
  </script>
  
  <style scoped>
  header {
    background-color: #282828;
    color: #dbd8d8;
    padding: 10px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .logo {
    margin: 0;
    color: #dbd8d8;
  }
  
  nav {
    display: flex;
  }
  
  .nav-link {
    text-decoration: none;
    color: #6c6c6c;
    font-size: 1.2em;
    padding: 10px;
    border: none;
    cursor: pointer;
    font-size: 1.2em;
    border-radius: 4px;
    margin-left: 10px;
    transition: color 0.3s;
  }
  
  .nav-link:hover,
  .active {
    text-decoration: underline;
    color: #9c9c9c;
  }
  
  .logout-button {
    background-color: #4d4d4d;
    color: #767676;
    padding: 10px;
    border: none;
    cursor: pointer;
    font-size: 1.2em;
    border-radius: 4px;
    margin-left: 10px;
    transition: color 0.3s;
  }
  
  .logout-button:hover {
    color: #f8fa87;
    text-decoration: underline;
  }
  </style>
  