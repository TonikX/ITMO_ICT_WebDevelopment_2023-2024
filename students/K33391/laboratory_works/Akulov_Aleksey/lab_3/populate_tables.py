import django


from recipes.models import Ingredient, NutritionalValue, Tool, Recipe, MealPlan, RecipeIngredient, RecipeTool


nv1 = NutritionalValue(calories=100, proteins=5, carbohydrates=20, fats=0)
nv1.save()
nv2 = NutritionalValue(calories=200, proteins=10, carbohydrates=30, fats=5)
nv2.save()
nv3 = NutritionalValue(calories=50, proteins=2, carbohydrates=10, fats=0)
nv3.save()
nv4 = NutritionalValue(calories=250, proteins=30, carbohydrates=0, fats=15)
nv4.save()

ingredient1 = Ingredient(name='Tomato', allergens='', is_vegetarian=True, nutritional_value=nv1)
ingredient1.save()
ingredient2 = Ingredient(name='Cheese', allergens='Milk', is_vegetarian=True, nutritional_value=nv2)
ingredient2.save()
ingredient3 = Ingredient(name='Cucumber', allergens='', is_vegetarian=True, nutritional_value=nv3)
ingredient3.save()
ingredient4 = Ingredient(name='Chicken', allergens='', is_vegetarian=False, nutritional_value=nv4)
ingredient4.save()


tool1 = Tool(name='Knife', cleaning_time=5)
tool1.save()
tool2 = Tool(name='Oven', cleaning_time=20)
tool2.save()
tool3 = Tool(name='Grill', cleaning_time=15)
tool3.save()

recipe1 = Recipe(title='Tomato Salad', preparation_time=10, cooking_time=0, difficulty_level='Easy', is_vegetarian=True)
recipe1.save()
recipe2 = Recipe(title='Cheese Pizza', preparation_time=20, cooking_time=15, difficulty_level='Medium', is_vegetarian=True)
recipe2.save()
recipe3 = Recipe(title='Grilled Chicken', preparation_time=15, cooking_time=30, difficulty_level='Medium', is_vegetarian=False)
recipe3.save()


ri1 = RecipeIngredient(recipe=recipe1, ingredient=ingredient1, quantity='2 Tomatoes')
ri1.save()
ri2 = RecipeIngredient(recipe=recipe1, ingredient=ingredient3, quantity='1 Cucumber')
ri2.save()
ri3 = RecipeIngredient(recipe=recipe2, ingredient=ingredient2, quantity='100g Cheese')
ri3.save()
ri4 = RecipeIngredient(recipe=recipe3, ingredient=ingredient4, quantity='200g Chicken')
ri4.save()

rt1 = RecipeTool(recipe=recipe1, tool=tool1)
rt1.save()
rt2 = RecipeTool(recipe=recipe2, tool=tool2)
rt2.save()
rt3 = RecipeTool(recipe=recipe3, tool=tool3)
rt3.save()
rt4 = RecipeTool(recipe=recipe3, tool=tool1)
rt4.save()


mp1 = MealPlan(date='2023-12-01', breakfast=recipe1, lunch=recipe2, dinner=recipe3)
mp1.save()
mp2 = MealPlan(date='2023-12-02', breakfast=recipe3, lunch=recipe1, dinner=recipe2)
mp2.save()

print("Database has been populated with sample data!")
