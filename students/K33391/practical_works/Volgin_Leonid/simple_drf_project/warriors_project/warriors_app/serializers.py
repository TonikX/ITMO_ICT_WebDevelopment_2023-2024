from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):

  class Meta:
     model = Warrior
     fields = "__all__"


class ProfessionCreateSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=120)
    description = serializers.CharField()

    def create(self, validated_data):
        prof_model_inst = Profession(**validated_data)
        prof_model_inst.save()
        return prof_model_inst

    def update(self, instance, validated_data):
        pass


class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)

    def create(self, validated_data):
        skill_model_inst = Skill(**validated_data)
        skill_model_inst.save()
        return skill_model_inst

    def update(self, instance, validated_data):
        pass


class SkillSerializer(serializers.ModelSerializer):

  class Meta:
     model = Skill
     fields = "__all__"
