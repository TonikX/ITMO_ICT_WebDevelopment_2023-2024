# warriors_app/serializers.py
from rest_framework import serializers
from .models import Profession
from .models import Warrior, Skill, SkillOfWarrior, Profession


class ProfessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"

class WarriorWithProfessionSerializer(serializers.ModelSerializer):
    profession = ProfessionCreateSerializer()

    class Meta:
        model = Warrior
        fields = "__all__"

class WarriorWithSkillsSerializer(serializers.ModelSerializer):
    skills = serializers.StringRelatedField(many=True)

    class Meta:
        model = Warrior
        fields = "__all__"

