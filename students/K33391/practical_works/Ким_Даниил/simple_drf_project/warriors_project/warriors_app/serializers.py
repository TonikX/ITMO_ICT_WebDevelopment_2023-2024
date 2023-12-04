from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"


class ProfessionCreateSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=120)
    description = serializers.CharField()

    # Переопределяем только его, потому что save более высокого уровня
    def create(self, validated_data):
        # validated_data - словарь, поэтому **
        prof_model_inst = Profession(**validated_data)
        prof_model_inst.save()
        return prof_model_inst

    def update(self, instance, validated_data):
        pass


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'title']


class ProfessionSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Profession
        fields = ['id', 'title', 'skills']


class WarriorWithProfessionsSerializer(serializers.ModelSerializer):
    professions = ProfessionSerializer(many=True, read_only=True)

    class Meta:
        model = Warrior
        fields = ['id', 'name', 'professions']


class WarriorWithSkillsSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Warrior
        fields = ['id', 'name', 'skills']


class WarriorFullInfoSerializer(serializers.ModelSerializer):
    professions = ProfessionSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Warrior
        fields = ['id', 'name', 'professions', 'skills']