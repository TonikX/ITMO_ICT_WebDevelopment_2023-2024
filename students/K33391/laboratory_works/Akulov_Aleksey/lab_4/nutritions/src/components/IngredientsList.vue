<template>
  <div>
    <h1>Ingredients List</h1>
    <ul>
      <li v-for="ingredient in ingredients" :key="ingredient.id">
        {{ ingredient.name }} -
        <span class="allergens">Allergens: {{ ingredient.allergens || 'None' }}</span>,
        <span class="vegetarian-status">Vegetarian: {{ ingredient.is_vegetarian ? 'Yes' : 'No' }}</span>,
        <span class="nutritional-value">Nutritional Value: Calories: {{ ingredient.nutritional_value.calories }},
        Proteins: {{ ingredient.nutritional_value.proteins }},
        Carbohydrates: {{ ingredient.nutritional_value.carbohydrates }},
        Fats: {{ ingredient.nutritional_value.fats }}</span>
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
h1 {
  color: #4CAF50;
  text-align: center;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0 auto;
  max-width: 800px; /* Adjust as needed */
}

li {
  background-color: #fff;
  margin-bottom: 1em;
  padding: 1em;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
  line-height: 1.5;
}

.ingredient-details {
  color: #333;
  font-size: 0.9em;
}

.allergens, .vegetarian-status, .nutritional-value {
  display: inline-block;
  margin-right: 15px;
  font-weight: bold;
}

.vegetarian-status {
  color: #4CAF50;
}

.allergens {
  color: #E53935;
}
</style>
