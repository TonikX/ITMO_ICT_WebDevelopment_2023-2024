from rest_framework import serializers
from .models import *


class ChickenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chicken
        fields = "__all__"


class MutateChickenSerializer(serializers.ModelSerializer):
    breed = serializers.PrimaryKeyRelatedField(many=False, queryset=Breed.objects.all())
    cage = serializers.PrimaryKeyRelatedField(many=False, queryset=Cage.objects.all())

    class Meta:
        model = Chicken
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"


class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = "__all__"
