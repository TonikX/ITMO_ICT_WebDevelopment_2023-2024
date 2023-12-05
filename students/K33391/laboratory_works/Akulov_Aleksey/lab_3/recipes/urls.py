from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngredientViewSet, NutritionalValueViewSet, \
    ToolViewSet, RecipeViewSet, MealPlanViewSet, find_recipes_by_nutrition, \
    find_recipes_by_ingredient

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet)
router.register(r'nutritionalvalues', NutritionalValueViewSet)
router.register(r'tools', ToolViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'mealplans', MealPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('mealplans/highest_calorie_plan/',
         MealPlanViewSet.as_view({'get': 'highest_calorie_plan'})),
    path('find_recipe/', find_recipes_by_nutrition),
    path('find_recipe_ing/', find_recipes_by_ingredient)
]
