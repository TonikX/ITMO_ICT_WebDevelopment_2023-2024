from rest_framework import serializers
from .models import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class WarriorProfessionSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer(many=True)

    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        exclude = ('skill', )


class WarriorSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)

    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        exclude = ('profession', )


class FullWarriorSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)
    profession = ProfessionSerializer(many=True)

    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        fields = "__all__"

