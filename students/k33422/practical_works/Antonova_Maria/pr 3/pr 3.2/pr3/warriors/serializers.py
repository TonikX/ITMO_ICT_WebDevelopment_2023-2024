from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"


class ProfessionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profession
        fields = ('title', 'description')



class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SkillCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('title',)



class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class WarriorAndProfessionSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer()

    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorAndSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)

    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorGetSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer(read_only=True)
    skill = SkillSerializer(many=True, read_only=True)

    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        fields = "__all__"