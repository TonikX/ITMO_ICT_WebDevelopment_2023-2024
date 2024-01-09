from rest_framework import serializers
from .models import Skill, SkillOfWarrior, Warrior, Profession


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'title']


class WarriorSkillSerializer(serializers.ModelSerializer):
    skill_set = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Warrior
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ('title', 'description')


class WarriorProfessionSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer(many=False)

    class Meta:
        model = Warrior
        fields = ('id', 'race', 'name', 'level', 'profession')


class SingleWarriorInfoSerializer(serializers.ModelSerializer):
    professions = ProfessionSerializer(many=True, read_only=True)
    skill_set = SkillSerializer(source='warrior_skills', many=True, read_only=True)

    class Meta:
        model = Warrior
        fields = '__all__'

class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = '__all__'
