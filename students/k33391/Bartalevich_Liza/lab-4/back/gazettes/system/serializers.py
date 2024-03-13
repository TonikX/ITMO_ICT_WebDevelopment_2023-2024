from rest_framework import  serializers
from .models import *
from django.contrib.auth.models import User


class ZooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zoo
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class CountAnimalInArea(serializers.ModelSerializer):

    count_animals_in = serializers.SerializerMethodField()
    animals_in = serializers.SerializerMethodField()

    class Meta:
        model = Area
        fields = ['id', 'name', 'count_animals_in', 'animals_in']

    def get_count_animals_in(self, obj):
        aias = AnimalInAviary.objects.filter(aviary__area=obj.id)
        return Animal.objects.filter(where__in=aias).distinct().count()

    def get_animals_in(self, obj):
        aias = AnimalInAviary.objects.filter(aviary__area=obj.id)
        qs = Animal.objects.filter(where__in=aias).distinct()
        ser = AnimalSerializer(qs, many=True)
        return ser.data


class AviarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviary
        fields = '__all__'


class ShowAviarySerializer(serializers.ModelSerializer):
    area = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Aviary
        fields = ['id', 'name', 'area', 'communal', 'winter_place', 'additional']


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


class ShowAnimalInAviarySerializer(serializers.ModelSerializer):
    animal = serializers.SlugRelatedField(read_only=True, slug_field='name')
    aviary = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = AnimalInAviary
        fields = ['animal', 'aviary']


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


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class ShowWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'num', 'name', 'birthday', 'type',]


class ShowOwningSerializer(serializers.ModelSerializer):
    animal = serializers.SlugRelatedField(read_only=True, slug_field="name")
    owner = serializers.SlugRelatedField(read_only=True, slug_field="name")
    here_now = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = Owning
        fields = [ 'animal', 'in_lease', 'owner', 'here_now', 'since',]


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password Does not match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password',]


class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []


class PasswordChangeSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    class Meta:
        model = User
        fields = ['current_password', 'new_password']

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value