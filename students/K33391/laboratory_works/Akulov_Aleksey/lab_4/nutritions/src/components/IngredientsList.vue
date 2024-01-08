<template>
  <div>
    <h1>Список Ингредиентов</h1>
    <ul>
      <li v-for="ingredient in ingredients" :key="ingredient.id">
        {{ ingredient.name }} -
        Аллергены: {{ ingredient.allergens || 'Нет' }},
        Вегетарианский: {{ ingredient.is_vegetarian ? 'Да' : 'Нет' }},
        Пищевая ценность: Калории: {{ ingredient.nutritional_value.calories }},
        Белки: {{ ingredient.nutritional_value.proteins }},
        Углеводы: {{ ingredient.nutritional_value.carbohydrates }},
        Жиры: {{ ingredient.nutritional_value.fats }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'IngredientsList',
  data() {
      return {
        ingredients: []
      }
  },
  created() {
      this.fetchIngredients();
  },
  methods: {
  fetchIngredients() {
      const token = localStorage.getItem('access_token');

      axios.get('http://127.0.0.1:8000/api/ingredients/', {
        headers: {
          'Authorization': `Token ${token}`
        }
      })
      .then(response => {
        this.ingredients = response.data;
      })
      .catch(error => {
        console.error('Ошибка при получении списка ингредиентов:', error);
      });
  }
}

}
</script>

<style scoped>
/* Стили для компонента */
</style>
