from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Ingredient, NutritionalValue, Tool, Recipe, MealPlan, \
    RecipeIngredient, RecipeTool, UserProfile


class NutritionalValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionalValue
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = '__all__'


class RecipeToolSerializer(serializers.ModelSerializer):
    tool = ToolSerializer()

    class Meta:
        model = RecipeTool
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(source='recipeingredient_set',
                                             many=True)
    tools = RecipeToolSerializer(source='recipetool_set', many=True)

    class Meta:
        model = Recipe
        fields = '__all__'


class MealPlanSerializer(serializers.ModelSerializer):
    breakfast = RecipeSerializer()
    lunch = RecipeSerializer()
    dinner = RecipeSerializer()

    class Meta:
        model = MealPlan
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    favorite_recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all(), allow_null=True)

    class Meta:
        model = UserProfile
        fields = (
            "id",
            "password",
            "username",
            "email",
            "first_name",
            "last_name",
            "favorite_recipe"
        )

    def create(self, validated_data):
        return super().create({**validated_data, "password": make_password(
            validated_data["password"])})
