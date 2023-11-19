from rest_framework import serializers

from warriors_app.models import Warrior, Profession, Skill, SkillOfWarrior


class ProfessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ('title', 'description')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class SkillOfWarriorSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = SkillOfWarrior
        fields = '__all__'


class WarriorSerializer(serializers.ModelSerializer):
    skills = SkillOfWarriorSerializer(many=True, read_only=True)
    profession = ProfessionSerializer()

    class Meta:
        model = Warrior
        fields = '__all__'
