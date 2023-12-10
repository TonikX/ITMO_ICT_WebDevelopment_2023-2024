from rest_framework import serializers
from .models import *


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class WarriorProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = ['name', 'profession']

    profession = ProfessionSerializer(read_only=True)


class SkillOfWarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillOfWarrior
        fields = ['skill', 'level']

    skill = serializers.SlugRelatedField(slug_field='title', read_only=True)


class WarriorSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = ['name', 'skill']

    skill = serializers.SerializerMethodField('get_skill_of_warrior')

    @staticmethod
    def get_skill_of_warrior(obj):
        skill = SkillOfWarrior.objects.filter(warrior=obj)
        return SkillOfWarriorSerializer(skill, many=True).data


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = '__all__'

    skill = serializers.SerializerMethodField("get_skill_of_warrior")
    race = serializers.CharField(source="get_race_display", read_only=True)
    profession = ProfessionSerializer(read_only=True)

    @staticmethod
    def get_skill_of_warrior(obj):
        skill = SkillOfWarrior.objects.filter(warrior=obj)
        return SkillOfWarriorSerializer(skill, many=True).data
