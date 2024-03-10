<template>
    <div>
      <h1>Products Page</h1>
      
      <!-- Sorting options -->
      <label>Sort By:</label>
      <select v-model="sortBy" @change="sortProducts">
        <option value="code">Code</option>
        <option value="name">Name</option>
        <option value="unit">Unit</option>
        <option value="shelf_life">Shelf Life</option>
      </select>
  
      <!-- Search input -->
      <label>Search by Code:</label>
      <input v-model="searchTerm" @input="filterProducts" />
  
      <!-- List of products -->
      <ul>
        <li v-for="product in filteredProducts" :key="product.id">
          {{ product.code }} - {{ product.name }} - {{ product.unit }} - {{ product.shelf_life }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Products',
    data() {
      return {
        products: [],
        sortBy: 'code',
        searchTerm: '',
      };
    },
    computed: {
      sortedProducts() {
        return this.products.slice().sort((a, b) => {
          if (this.sortBy === 'code') {
            return a.code.localeCompare(b.code);
          } else if (this.sortBy === 'name') {
            return a.name.localeCompare(b.name);
          } else if (this.sortBy === 'unit') {
            return a.unit.localeCompare(b.unit);
          } else if (this.sortBy === 'shelf_life') {
            return a.shelf_life - b.shelf_life;
          }
          return 0;
        });
      },
      filteredProducts() {
        const search = this.searchTerm.toLowerCase();
        return this.sortedProducts.filter(
          product => product.code.toLowerCase().includes(search)
        );
      },
    },
    methods: {
      async fetchProducts() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/main/products/', {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          this.products = response.data;
        } catch (error) {
          console.error('Error fetching product data:', error);
        }
      },
      sortProducts() {
        // Triggered when sorting option changes
      },
      filterProducts() {
        // Triggered when search term changes
      },
    },
    created() {
      this.fetchProducts();
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  