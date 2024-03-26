<template>
  <div class = "main-container">
    <div class = "recipe-list-container">

      <h1>Recipes</h1>
        <ul class="recipe-list">
          <li v-for="recipe in recipes" :key="recipe.id">
            <h2>{{ recipe.title }}</h2>

            <p><span class="labels">Preparation Time:</span> <span class="values">{{ recipe.preparation_time }} min</span></p>
            <p><span class="labels">Cooking Time:</span> <span class="values">{{ recipe.cooking_time }} min</span></p>
            <p><span class="labels">Difficulty:</span> <span class="values">{{ recipe.difficulty_level }}</span></p>
            <p><span class="labels">Region:</span> <span class="values">{{ recipe.region }}</span></p>
            <p><span class="labels">Vegetarian:</span> <span class="values">{{ recipe.is_vegetarian ? 'Yes' : 'No' }}</span></p>
            <br><br>
            <div v-if="recipe.ingredients.length">
              <h3>Ingredients:</h3>
              <ul>
                <li v-for="ingredient in recipe.ingredients" :key="ingredient.id">
                  <span class="value">{{ ingredient.ingredient.name }}</span> - <span class="value">{{ ingredient.quantity }}</span>
                </li>
              </ul>
            </div>

            <div v-if="recipe.tools.length">
              <h3>Tools:</h3>
              <ul>
                <li v-for="tool in recipe.tools" :key="tool.id">
                  <span class="value">{{ tool.tool.name }}</span>
                </li>
              </ul>
            </div>

            <br>
            <button @click="deleteRecipe(recipe.id)" style="margin-right: 60px;">Delete</button>
            <button @click="startEdit(recipe)" style="margin-left: 60px;">Edit</button>

          </li>
        </ul>


        <div  v-if="editRecipe">
          <h2>Recipe Edition: {{ editRecipe.title }}</h2>
          <form @submit.prevent="updateRecipe">
            <div>
              <label for="editTitle">Title:</label>
              <input id="editTitle" type="text" v-model="editRecipe.title" required>
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
              <input id="editRegion" type="text" v-model="editRecipe.region">
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
            <br>
            <button type="submit">Update Recipe</button>
            <button @click="cancelEdit" style="margin-left: 60px;">Cancel</button>
          </form>
        </div>
    </div>

    <div class="form-container">
      <h2>Create a New Recipe</h2>
      <form @submit.prevent="createRecipe">
        <div>
          <label for="newTitle">Title:</label>
          <input id="newTitle" type="text" v-model="newRecipe.title" required>
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
          <input id="newRegion" type="text" v-model="newRecipe.region">
        </div>

        <div>
          <label for="newVegetarian">Vegetarian:</label>
          <input id="newVegetarian" type="checkbox" v-model="newRecipe.is_vegetarian">
        </div>

        <br>

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
    addIngredient(event) {
      event.preventDefault();

      const ingredientToAdd = this.ingredients.find(ing => ing.id === this.newIngredientId);
      if (ingredientToAdd) {
        this.editRecipe.ingredients.push({
          ingredient: ingredientToAdd,
          quantity: this.newIngredientQuantity
        });

        this.newIngredientId = null;
        this.newIngredientQuantity = '';
      }
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
  color: #3bbcb8;
}

ul {
  list-style-type: none;
  padding: 0;
}

.recipe-list li {
  background-color: #173f32;
  margin-bottom: 1em;
  padding: 1em;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
}

.recipe-list p, .recipe-list li {
  font-size: 1em;
}

.recipe-list p {
  margin: 5px 0;
}

.recipe-list p span.label {
  font-weight: bold;
  color: #333;
  margin-right: 5px;
}

.recipe-list p span.value {
  color: #555;
}

button {
  background-color: #3bbcb8;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #1b61ce;
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

.main-container {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  height: calc(100vh - 60px);
  margin-top: 60px;
}

.recipe-list-container,
.form-container {
  flex: 1;
  padding: 50px;
  overflow: auto;
}

.recipe-list-container {
  max-width: 50%;
}

.form-container {
  max-width: 50%;
}

input[type="checkbox"] {
  transform: scale(1.5);
  margin-left: 10px;
  border-color: #4cafa0;
}

.labels{
  color: #d76817;
}

.values{
  color: #ffffff;
}
</style>