<template>
  <div class = "main-container">
    <div class = "recipe-list-container">

      <h1>Recipes</h1>
        <ul>
          <li v-for="recipe in recipes" :key="recipe.id">
            <h2>{{ recipe.title }}</h2>
            <p>Preparation Time: {{ recipe.preparation_time }} min</p>
            <p>Cooking time: {{ recipe.cooking_time }} min</p>
            <p>Difficulty: {{ recipe.difficulty_level }}</p>
            <p>Region: {{ recipe.region }}</p>
            <p>Vegetarian: {{ recipe.is_vegetarian ? 'Yes' : 'No' }}</p>
            <div v-if="recipe.ingredients.length">
              <h3>Ingredients:</h3>
              <ul>
                <li v-for="ingredient in recipe.ingredients" :key="ingredient.id">
                  {{ ingredient.ingredient.name }} - {{ ingredient.quantity }}
                </li>
              </ul>
            </div>
            <div v-if="recipe.tools.length">
              <h3>Tools:</h3>
              <ul>
                <li v-for="tool in recipe.tools" :key="tool.id">
                   {{ tool.tool.name }}
                </li>
              </ul>
            </div>
            <button @click="deleteRecipe(recipe.id)">Delete</button>
            <button @click="startEdit(recipe)">Edit</button>
          </li>
        </ul>

        <div  v-if="editRecipe">
          <h2>Recipe Edition: {{ editRecipe.title }}</h2>
          <form @submit.prevent="updateRecipe">
            <div>
              <label for="editTitle">Title:</label>
              <input id="editTitle" v-model="editRecipe.title" required>
            </div>

            <div>
              <label for="editPreparationTime">Preparation Time (in minutes):</label>
              <input id="editPreparationTime" type="number" v-model="editRecipe.preparation_time" required>
            </div>

            <div>
              <label for="editCookingTime">Cooking Time (in minutes):</label>
              <input id="editCookingTime" type="number" v-model="editRecipe.cooking_time" required>
            </div>

            <div>
              <label for="editDifficulty">Difficulty:</label>
              <select id="editDifficulty" v-model="editRecipe.difficulty_level" required>
                <option value="E">Easy</option>
                <option value="M">Medium</option>
                <option value="H">Hard</option>
              </select>
            </div>

            <div>
              <label for="editRegion">Region:</label>
              <input id="editRegion" v-model="editRecipe.region">
            </div>

            <div>
              <label for="editVegetarian">Vegetarian:</label>
              <input id="editVegetarian" type="checkbox" v-model="editRecipe.is_vegetarian">
            </div>



            <h3>Ingredients:</h3>
            <ul>
              <li v-for="(ingredient, index) in editRecipe.ingredients" :key="ingredient.id">
                {{ ingredient.ingredient.name }} -
                <input type="text" v-model="ingredient.quantity">
                <button @click="removeIngredient(index)">Remove</button>
              </li>
            </ul>
            <div>
              <select v-model="newIngredientId">
                <option v-for="ingredient in ingredients" :value="ingredient.id">{{ ingredient.name }}</option>
              </select>
              <input type="text" v-model="newIngredientQuantity" placeholder="Quantity">
              <button @click="addIngredient">Add Ingredient</button>
            </div>


            <button type="submit">Update Recipe</button>
            <button @click="cancelEdit">Cancel</button>
          </form>
        </div>
    </div>

    <div class="form-container">
      <h2>Create a New Recipe</h2>
      <form @submit.prevent="createRecipe">
        <div>
          <label for="newTitle">Title:</label>
          <input id="newTitle" v-model="newRecipe.title" required>
        </div>

        <div>
          <label for="newPreparationTime">Preparation Time (in minutes):</label>
          <input id="newPreparationTime" type="number" v-model="newRecipe.preparation_time" required>
        </div>

        <div>
          <label for="newCookingTime">Cooking Time (in minutes):</label>
          <input id="newCookingTime" type="number" v-model="newRecipe.cooking_time" required>
        </div>

        <div>
          <label for="newDifficulty">Difficulty:</label>
          <select id="newDifficulty" v-model="newRecipe.difficulty_level" required>
            <option value="E">Easy</option>
            <option value="M">Medium</option>
            <option value="H">Hard</option>
          </select>
        </div>

        <div>
          <label for="newRegion">Region:</label>
          <input id="newRegion" v-model="newRecipe.region">
        </div>

        <div>
          <label for="newVegetarian">Vegetarian:</label>
          <input id="newVegetarian" type="checkbox" v-model="newRecipe.is_vegetarian">
        </div>

        <button type="submit">Create Recipe</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "RecipeList",
  data() {
    return {
      recipes: [],
      editRecipe: null,
      newRecipe: {
        title: '',
        preparation_time: 0,
        cooking_time: 0,
        difficulty_level: 'E',
        region: '',
        is_vegetarian: false,
        ingredients: []
      },
      newIngredientId: null,
      newIngredientQuantity: '',
      ingredients: []
    }
  },
  created() {
    this.fetchRecipes();
    this.fetchIngredients();
  },
  methods: {
    addIngredient() {
      this.editRecipe.ingredients.push({
        ingredient: this.ingredients.find(ing => ing.id === this.newIngredientId),
        quantity: this.newIngredientQuantity
      });
      this.newIngredientId = null;
      this.newIngredientQuantity = '';
    },
    removeIngredient(index) {
      this.editRecipe.ingredients.splice(index, 1);
    },


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



    fetchRecipes() {
      const token = localStorage.getItem('access_token');

      axios.get('http://127.0.0.1:8000/api/recipes/', {
        headers: {
          'Authorization': `Token ${token}`
        }
      })
        .then(response => {
          this.recipes = response.data;
        })
        .catch(error => {
          console.error('Ошибка при получении рецептов:', error);
        })
    },


    startEdit(recipe) {
      this.editRecipe = {...recipe};
    },
    cancelEdit() {
      this.editRecipe = null;
    },
    updateRecipe() {
      const token = localStorage.getItem('access_token');
      axios.patch(`http://127.0.0.1:8000/api/recipes/${this.editRecipe.id}/`, this.editRecipe, {
        headers: {
          'Authorization': `Token ${token}`
        }
      })
      .then(() => {
        this.fetchRecipes();
        this.editRecipe = null;
      })
      .catch(error => {
        console.error('Ошибка при обновлении рецепта:', error);
      });
    },


    deleteRecipe(id) {
      const token = localStorage.getItem('access_token');
      axios.delete(`http://127.0.0.1:8000/api/recipes/${id}`, {
        headers: {
          'Authorization': `Token ${token}`
        }
      })
      .then(() => {
        this.fetchRecipes();
      })
      .catch(error => {
        console.error('Ошибка при удалении рецепта:', error);
      });
    },


    createRecipe() {
      const token = localStorage.getItem('access_token');
      axios.post(`http://127.0.0.1:8000/api/recipes/`, this.newRecipe, {
        headers: {
          'Authorization': `Token ${token}`
        }
      })
      .then(() => {
        this.fetchRecipes();
        this.newRecipe = { title: '', preparation_time: 0, cooking_time: 0, difficulty_level: 'E', region: '', is_vegetarian: false };
      })
      .catch(error => {
        console.error('Ошибка при создании рецепта:', error);
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
  color: #4CAF50;
}

ul {
  list-style-type: none;
  padding: 0;
}

.recipe-list li {
  background-color: #fff;
  margin-bottom: 1em;
  padding: 1em;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
}

.recipe-list h2 {
  margin-top: 0;
}

button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #45a049;
}

input[type="text"], input[type="number"], select {
  width: 100%;
  padding: 10px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.main-container {
  display: flex;
  margin-top: 60px; /* Adjust based on the height of your navigation menu */
}

.recipe-list-container {
  flex: 1; /* Takes up 1 part of the available space */
  padding: 10px;
}

.form-container {
  flex: 1; /* Takes up 1 part of the available space */
  padding: 10px;
}

</style>