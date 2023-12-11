# Практическая 3.2
## Модели данных
```Python
from django.db import models


class Warrior(models.Model):
    race_types = (
        ('s', 'student'),
        ('d', 'developer'),
        ('t', 'teamlead'),
    )
    race = models.CharField(max_length=1, choices=race_types, verbose_name='Расса')
    name = models.CharField(max_length=120, verbose_name='Имя')
    level = models.IntegerField(verbose_name='Уровень', default=0)
    skill = models.ManyToManyField('Skill', verbose_name='Умения', through='SkillOfWarrior', related_name='warrior_skils')
    profession = models.ForeignKey('Profession', on_delete=models.CASCADE, verbose_name='Профессия', blank=True, null=True)


class Profession(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')


class Skill(models.Model):
    title = models.CharField(max_length=120, verbose_name='Наименование')

    def __str__(self):
        return self.title


class SkillOfWarrior(models.Model):
    skill = models.ForeignKey('Skill', verbose_name='Умение', on_delete=models.CASCADE)
    warrior = models.ForeignKey('Warrior', verbose_name='Воин', on_delete=models.CASCADE)
    level = models.IntegerField(verbose_name='Уровень освоения умения')
```
## Файлы urls.py
```Python
from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('warriors/list/', WarriorListAPIView.as_view()),
    path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
    path('skill/generic_create/', SkillCreateAPIView.as_view()),
    ]
```
## Полученные сериализаторы
```Python
from rest_framework import serializers
from warriors_app.models import *


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ["title", "description"]


class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)

    def create(self, validated_data):
        skill = Skill(**validated_data)
        skill.save()
        return Skill(**validated_data)


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class WarriorSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer(read_only=True)
    skills = SkillSerializer(many=True, source="skill")

    class Meta:
        model = Warrior
        fields = ["id", "race", "name", "level", "profession", "skills"]


class ProfessionCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()

    def create(self, validated_data):
        profession = Profession(**validated_data)
        profession.save()
        return Profession(**validated_data)


class SkillRelatedSerializer(serializers.ModelSerializer):
    warrior_skils = WarriorSerializer(many=True)
    
    class Meta:
        model = Skill
        fields = ["title", "warrior_skils"]


class WarriorRelatedSerializer(serializers.ModelSerializer):
    skill = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"
        depth = 1
```
## Представления 
```Python
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from warriors_app.models import *
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from .serializers import *


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class ProfessionCreateView(APIView):
    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionCreateSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class WarriorListAPIView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionCreateSerializer
    queryset = Profession.objects.all()


class SkillCreateAPIView(generics.CreateAPIView):
    serializer_class = SkillCreateSerializer
    queryset = Skill.objects.all()


class WarriorList(APIView):
    def get(self, request):
        warriors = Warrior.objects.all().prefetch_related("profession", "skill")
        serializer = WarriorSerializer(warriors, many=True)
        return Response(serializer.data)


class WarriorDetail(APIView):
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


class SkillList(APIView):
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
```