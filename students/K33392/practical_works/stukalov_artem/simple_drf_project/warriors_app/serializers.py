from rest_framework import serializers
from .models import Warrior, Profession, Skill


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class WarriorSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer(read_only=True)
    skill = SkillSerializer(many=True)

    class Meta:
        model = Warrior
        fields = ["id", "race", "name", "level", "profession", "skill"]
