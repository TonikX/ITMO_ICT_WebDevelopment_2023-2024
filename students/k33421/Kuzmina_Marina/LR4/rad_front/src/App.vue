<template>
  <div class="books-list">
    <nav class="navigation-links">
      <button class="styled-button">
        <router-link to="/register">Register</router-link>
      </button>
      <button class="styled-button">
        <router-link to="/login">Login</router-link>
      </button>
      <button class="styled-button">
        <router-link to="/profile">Profile</router-link>
      </button>
    </nav>
    <br>
    <header class="header">
      <h1 class="title">Books</h1>
      <nav class="navigation-links">
        <router-link to="/"> ↩︎ Back to main</router-link>
      </nav>
    </header>

    <router-view></router-view>

    <ul class="books">
      <p>
        <li v-for="book in books" :key="book.id" class="book-item">
          <router-link :to="{ name: 'book-detail', params: { id: book.id } }"style="text-decoration: none;">
            <div class="book-details">
              <h2>{{ book.title }}</h2>
              <p>by {{ book.author }}</p>
              <p>{{ book.description }}</p>
            </div>
          </router-link>
        </li>
      </p>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      books: [],
    };
  },
  mounted() {
    axios.get('http://localhost:8000/api/books/')
      .then(response => {
        this.books = response.data;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  },
  methods: {
    getCoverUrl(cover) {
      return `/book_covers/${cover}`;
    },
  },
};
</script>

<style scoped>

.styled-button {
  background-color: #FFFFFF;
  color: #000000;
  padding: 10px 20px;
  border: 1px solid #ddd;
  cursor: pointer;
  border-radius: 7px;
  transition: transform 0.3s;
}
.styled-button:hover {
  transform: scale(1.1);
}

body {
  font-family: Montserrat, sans-serif;
  background-color: #f5f5f5;
  color: #333;
}
а {
  text-decoration: none;
  font-color: #333;
}
.books-list {
  max-width: 800px;
  margin: 0 auto;
}

.header {
  background-color: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  border-radius: 8px;
}

.title {
  font-size: 24px;
  font-weight: bold;
}

.navigation-links {
  margin-top: 10px;
}

.navigation-links a {
  margin-right: 0px;
  color: #333;
  text-decoration: none;
  font-size: 14px;
}

.books {
  list-style: none;
  padding: 0;
}

.book-item {
  display: flex;
  border: 1px solid #ddd;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 8px;
  background-color: #fff;
  transition: transform 0.3s;
}

.book-item:hover {
  transform: scale(1.02);
}

.book-cover {
  max-width: 100px;
  margin-right: 10px;
  border-radius: 5px;
}

.book-details {
  flex-grow: 1;
}

.book-details h2 {
  margin: 0 0 5px;
  font-size: 20px;
  color: #000000;
}

.book-details p {
  margin: 0;
  text-decoration: none;
}

.book-details p a {
  color: inherit; /* Используем цвет текста по умолчанию (унаследованный) */
  text-decoration: none; /* Убираем подчеркивание текста */
}

.book-details p a:hover {
  text-decoration: none; /* Убираем подчеркивание текста при наведении */
  color: inherit; /* Можно явно указать цвет при наведении, если нужно изменить */
}

p {
  color: #000;
}
</style>







