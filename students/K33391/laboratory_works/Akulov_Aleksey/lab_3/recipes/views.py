from django.db.models import Sum
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response

from .models import Ingredient, NutritionalValue, Tool, Recipe, MealPlan, \
    RecipeIngredient, UserProfile, RecipeTool

from .serializers import IngredientSerializer, NutritionalValueSerializer, \
    ToolSerializer, RecipeSerializer, MealPlanSerializer, UserProfileSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        nutritional_data = request.data.get('nutritional_value')
        nutritional_value = None

        if nutritional_data:
            nutritional_serializer = NutritionalValueSerializer(
                data=nutritional_data)
            if nutritional_serializer.is_valid():
                if 'id' in nutritional_data:
                    nutritional_value = NutritionalValue.objects.get(
                        id=nutritional_data['id'])
                else:
                    nutritional_value = NutritionalValue.objects.create(
                        **nutritional_serializer.validated_data)

        ingredient_data = serializer.validated_data
        ingredient_data['nutritional_value'] = nutritional_value
        ingredient = Ingredient.objects.create(**ingredient_data)

        output_serializer = IngredientSerializer(ingredient)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class NutritionalValueViewSet(viewsets.ModelViewSet):
    queryset = NutritionalValue.objects.all()
    serializer_class = NutritionalValueSerializer


class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        recipe_data = serializer.validated_data
        recipe = Recipe.objects.create(
            title=recipe_data['title'],
            preparation_time=recipe_data['preparation_time'],
            cooking_time=recipe_data['cooking_time'],
            difficulty_level=recipe_data['difficulty_level'],
            region=recipe_data.get('region', ''),
            is_vegetarian=recipe_data['is_vegetarian'],
            image_url=recipe_data.get('image_url', '')
        )

        for ingredient_data in request.data.get('ingredients', []):
            ingredient_id = ingredient_data['id']
            quantity = ingredient_data['quantity']
            ingredient = Ingredient.objects.get(id=ingredient_id)
            RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient, quantity=quantity)

        for tool_data in request.data.get('tools', []):
            tool_id = tool_data['id']
            tool = Tool.objects.get(id=tool_id)
            RecipeTool.objects.create(recipe=recipe, tool=tool)

        output_serializer = RecipeSerializer(recipe)
        headers = self.get_success_headers(output_serializer.data)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


def find_highest_calorie_plan():
    max_calorie_plan = None
    max_calories = 0
    for plan in MealPlan.objects.all():
        total_calories = 0
        for recipe in [plan.breakfast, plan.lunch, plan.dinner]:
            if recipe:
                for recipe_ingredient in RecipeIngredient.objects.filter(
                        recipe=recipe):
                    if recipe_ingredient.ingredient.nutritional_value.calories:
                        calories_per_unit = recipe_ingredient.ingredient.\
                            nutritional_value.calories

                        #quantity = float(recipe_ingredient.quantity)
                        total_calories += calories_per_unit
        if total_calories > max_calories:
            max_calories = total_calories
            max_calorie_plan = plan
    return max_calorie_plan


class MealPlanViewSet(viewsets.ModelViewSet):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer

    @action(detail=False)
    def highest_calorie_plan(self, request):
        max_calorie_plan = find_highest_calorie_plan()
        if max_calorie_plan:
            serializer = self.get_serializer(max_calorie_plan)
            return Response(serializer.data)
        else:
            return Response({'status': 'no meal plans found'},
                            status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def find_recipes_by_ingredient(request):
    ingredient_name = request.data["name"]
    queryset = Recipe.objects.filter(ingredients__name=ingredient_name)
    serializer = RecipeSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def find_recipes_by_nutrition(request):
    min_calories = request.data.get("min_calories", 0)
    min_proteins = request.data.get("min_proteins", 0)
    min_carbs = request.data.get("min_carbs", 0)
    min_fats = request.data.get("min_fats", 0)

    queryset = Recipe.objects.annotate(
        total_calories=Sum('ingredients__nutritional_value__calories'),
        total_proteins=Sum('ingredients__nutritional_value__proteins'),
        total_carbohydrates=Sum('ingredients__nutritional_value__carbohydrates'),
        total_fats=Sum('ingredients__nutritional_value__fats')
    ).filter(
        total_calories__gte=min_calories,
        total_proteins__gte=min_proteins,
        total_carbohydrates__gte=min_carbs,
        total_fats__gte=min_fats
    )

    serializer = RecipeSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

    @action(detail=True, methods=['patch'])
    def partial_update_profile(self, request, pk=None):
        instance = self.get_object()
        partial_data = request.data
        serializer = self.get_serializer(instance, data=partial_data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)

        for key, value in serializer.validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return Response(self.get_serializer(instance).data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

