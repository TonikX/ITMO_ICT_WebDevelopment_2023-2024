from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import serializers
from warriors.models import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SkillList(APIView):
    """
    Представление для просмотра списка скиллов или создания нового скилла.
    """

    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class WarriorSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer(read_only=True)
    skills = SkillSerializer(many=True, source="skill_set")

    class Meta:
        model = Warrior
        fields = ["id", "race", "name", "level", "profession", "skills"]


class WarriorList(APIView):
    """
    Представление для вывода информации о всех войнах и их профессиях/скилах.
    """

    def get(self, request):
        warriors = Warrior.objects.all().prefetch_related("profession", "skill_set")
        serializer = WarriorSerializer(warriors, many=True)
        return Response(serializer.data)


class WarriorDetail(APIView):
    """
    Представление для вывода полной информации о войне по id, его профессиях и скилах,
    удаления война и редактирования информации о войне.
    """

    def get(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        serializer = WarriorSerializer(warrior)
        return Response(serializer.data)

    def delete(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        warrior.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        serializer = WarriorSerializer(warrior, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
