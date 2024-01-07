from django.db import models
from django.contrib.auth.models import AbstractUser


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    allergens = models.CharField(max_length=255, blank=True)
    is_vegetarian = models.BooleanField(default=False)
    nutritional_value = models.ForeignKey('NutritionalValue',
                                          on_delete=models.SET_NULL, null=True,
                                          blank=True)


class NutritionalValue(models.Model):
    calories = models.IntegerField()
    proteins = models.IntegerField()
    carbohydrates = models.IntegerField()
    fats = models.IntegerField()


class Tool(models.Model):
    name = models.CharField(max_length=255)
    cleaning_time = models.IntegerField()


class Recipe(models.Model):
    difficulty_types = (
        ("E", "Easy"),
        ("M", "Medium"),
        ("H", "Hard"),
    )

    title = models.CharField(max_length=255)
    preparation_time = models.IntegerField()
    cooking_time = models.IntegerField()
    difficulty_level = models.CharField(max_length=2, choices=difficulty_types)
    region = models.CharField(max_length=255, blank=True)
    is_vegetarian = models.BooleanField(default=False)
    image_url = models.URLField(blank=True)
    ingredients = models.ManyToManyField(Ingredient,
                                         through='RecipeIngredient')
    tools = models.ManyToManyField(Tool, through='RecipeTool')


class MealPlan(models.Model):
    date = models.DateField()
    breakfast = models.ForeignKey(Recipe, related_name='meal_plan_breakfast',
                                  on_delete=models.SET_NULL, null=True,
                                  blank=True)
    lunch = models.ForeignKey(Recipe, related_name='meal_plan_lunch',
                              on_delete=models.SET_NULL, null=True, blank=True)
    dinner = models.ForeignKey(Recipe, related_name='meal_plan_dinner',
                               on_delete=models.SET_NULL, null=True,
                               blank=True)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)


class RecipeTool(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)


class UserProfile(AbstractUser):
    favorite_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
