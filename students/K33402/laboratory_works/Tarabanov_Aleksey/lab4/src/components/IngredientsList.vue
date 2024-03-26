<template>
  <div>
    <div class="ingredient-list-container">
      <h1>Ingredients list</h1>
      <ul>
        <li v-for="ingredient in ingredients" :key="ingredient.id" class="ingredient-item">
          <div class="ingredient-details">
            <span class="ingredient-name">{{ ingredient.name }}</span>
            <br>
            <span class="allergens">Allergens: {{ ingredient.allergens || 'None' }}</span>
            <span class="vegetarian-status">Vegetarian: {{ ingredient.is_vegetarian ? 'Yes' : 'No' }}</span>
            <br>
            <div class="nutritional-value">
              Nutritional Value:
              <br>
              Calories: {{ ingredient.nutritional_value.calories }},
              Proteins: {{ ingredient.nutritional_value.proteins }},
              Carbohydrates: {{ ingredient.nutritional_value.carbohydrates }},
              Fats: {{ ingredient.nutritional_value.fats }}
            </div>
          </div>
          <div class="ingredient-actions">
            <button @click="deleteIngredient(ingredient.id)">Delete</button>
          </div>
        </li>
      </ul>
    </div>


    <div class="form-container">
      <h2>Add a new ingredient</h2>
      <form @submit.prevent="createIngredient">
        <div>
          <label for="newName">Designation:</label>
          <input id="newName" type="text" v-model="newIngredient.name" required>
        </div>

        <div>
          <label for="newAllergens">Allergens:</label>
          <input id="newAllergens" type="text" v-model="newIngredient.allergens" required>
        </div>

        <div>
          <label for="newIsVegetarian">Vegetarian:</label>
          <input id="newIsVegetarian" type="checkbox" v-model="newIngredient.is_vegetarian">
          <br>
        </div>

        <div>
          <label for="newCalories">Calories:</label>
          <input id="newCalories" type="number" v-model.number="newIngredient.nutritional_value.calories" required>
        </div>

        <div>
          <label for="newProteins">Proteins:</label>
          <input id="newProteins" type="number" v-model.number="newIngredient.nutritional_value.proteins" required>
        </div>

        <div>
          <label for="newCarbohydrates">Carbohydrates:</label>
          <input id="newCarbohydrates" type="number" v-model.number="newIngredient.nutritional_value.carbohydrates" required>
        </div>

        <div>
          <label for="newFats">Fats:</label>
          <input id="newFats" type="number" v-model.number="newIngredient.nutritional_value.fats" required>
        </div>

        <div>
          <button type="submit">Add Ingredient</button>
        </div>
      </form>

    </div>

  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'IngredientsList',
  data() {
      return {
        ingredients: [],
        newIngredient: { name: '', allergens: '', is_vegetarian: false, nutritional_value:
              {calories: 0, proteins: 0, carbohydrates: 0, fats: 0} }
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
  },
  createIngredient() {
    const token = localStorage.getItem('access_token');
    axios.post('http://127.0.0.1:8000/api/ingredients/', this.newIngredient, {
      headers: {
        'Authorization': `Token ${token}`
      }
    })
    .then(() => {
      this.fetchIngredients();
      this.newIngredient = { name: '', allergens: '', is_vegetarian: false, nutritional_value:
                           {calories: 0, proteins: 0, carbohydrates: 0, fats: 0} };
    })
    .catch(error => {
      console.error('Ошибка при создании ингредиента:', error);
    });
  },
  deleteIngredient(ingredientId) {
    const token = localStorage.getItem('access_token');
    axios.delete(`http://127.0.0.1:8000/api/ingredients/${ingredientId}`, {
      headers: {
        'Authorization': `Token ${token}`
      }
    })
    .then(() => {
      this.fetchIngredients(); // Refresh the list after deletion
    })
    .catch(error => {
      console.error('Ошибка при удалении ингредиента:', error);
    });
  }
}

}
</script>

<style scoped>

body {
  font-family: 'Arial', sans-serif;
  color: #333;
  background-color: #f8f8f8;
  line-height: 1.6;
}


h1, h2, h3 {
  color: #3bbcb8;
  text-align: center;
}

.ingredient-list-container ul {
  list-style: none;
  padding: 0;
  margin: 0 auto;
  max-width: 800px;
}

.ingredient-item {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 10px;
}

li {
  background-color: #173f32;
  margin-bottom: 1em;
  padding: 1em;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
  line-height: 1.5;
}

.allergens, .vegetarian-status, .nutritional-value {
  display: inline-block;
  margin-right: 15px;
}

.vegetarian-status {
  color: #00ff0b;
}

.allergens {
  color: #ff0700;
}

.ingredient-name {
    color: white;
    font-size: 20px; /* Изменение размера текста для ingredient.name */
}

.nutritional-value {
    color: #d59405; /* Изменение цвета текста для Nutritional Value */
}

button {
  background-color: #3bbcb8;
  color: white;
  border: none;
  padding: 20px 30px;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s;
  margin: 0 auto; /* Центрирование по горизонтали */
  display: block; /* Чтобы кнопка занимала всю доступную ширину */
}

button:hover {
  background-color: #0578ff;
}

input[type="text"], input[type="number"], select {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  display: inline-block;
  border: 2px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

label[for="newIsVegetarian"] {
  margin-right: 10px;
}

input[type="checkbox"] {
  transform: scale(1.5);
  margin-right: 5px;
  border-color: #4CAF50;
}

</style>
