<template>
    <div class="favorite-products">
      <h1 class="title">Избранные книги</h1>
      <div v-if="favoriteProducts.length === 0">
        <p>У вас пока нет избранных книг.</p>
      </div>
      <div v-else>
        <div v-for="product in favoriteProducts" :key="product.id" class="column is-3">
          <div class="box">
            <figure class="image mb-4">
              <img :src="product.get_thumbnail" alt="Product Thumbnail">
            </figure>
            <h3 class="is-size-4">{{ product.name }}</h3>
            <p class="is-size-6 has-text-grey">{{ product.price }}руб.</p>
            <button @click="toggleFavorite(product)" class="button is-danger mt-4">
              {{ product.is_favorite ? 'Убрать из избранных' : 'Добавить в избранное' }}
            </button>
            <router-link :to="product.get_absolute_url" class="button is-dark mt-2">Подробнее</router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'FavouriteBooks',
    data() {
      return {
        favoriteProducts: [],
      };
    },
    created() {
      this.getFavoriteProducts();
    },
    methods: {
      async getFavoriteProducts() {
        try {
          const response = await axios.get('/api/v1/favorite-products');
          this.favoriteProducts = response.data;
        } catch (error) {
          console.error('Ошибка при получении избранных книг', error);
        }
      },
      async toggleFavorite(product) {
        try {
          const response = await axios.patch(`/api/v1/products/${product.id}/toggle-favorite/`);
          product.is_favorite = response.data.is_favorite;
        } catch (error) {
          console.error('Ошибка при изменении статуса избранного', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
  </style>