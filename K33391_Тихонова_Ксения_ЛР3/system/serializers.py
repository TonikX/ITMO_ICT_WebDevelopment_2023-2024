from rest_framework import  serializers
from .models import *


class ZooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zoo
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class AviarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviary
        fields = '__all__'


class HabitatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitat
        fields = '__all__'


class TypeOfDietSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfDiet
        fields = '__all__'


class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = '__all__'


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'


class WinterPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WinterPlace
        fields ='__all__'


class AnimalInAviarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalInAviary
        fields = '__all__'


class OwningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owning
        fields = '__all__'


class CountAnimalInArea(serializers.ModelSerializer):

    count_animals_in = serializers.SerializerMethodField()
    animals_in = serializers.SerializerMethodField()

    def get_count_animals_in(self, obj):
        aias = AnimalInAviary.objects.filter(aviary__building__area=obj.id)
        return Animal.objects.filter(where__in=aias).distinct().count()

    def get_animals_in(self, obj):
        aias = AnimalInAviary.objects.filter(aviary__building__area=obj.id)
        qs = Animal.objects.filter(where__in=aias).distinct()
        ser = AnimalSerializer(qs, many=True)
        return ser.data

    class Meta:
        model = Area
        fields = ['id', 'name', 'count_animals_in', 'animals_in']

class ShowAIASerializers(serializers.ModelSerializer):
    animal = AnimalSerializer()

    class Meta:
        model = AnimalInAviary
        fields = ['animal']


class ShowAviarySerializer(serializers.ModelSerializer):
    
    building = BuildingSerializer()
    who = ShowAIASerializers(many=True)

    class Meta:
        model = Aviary
        fields = ['id','name', 'communal', 'additional', 'who', 'building']