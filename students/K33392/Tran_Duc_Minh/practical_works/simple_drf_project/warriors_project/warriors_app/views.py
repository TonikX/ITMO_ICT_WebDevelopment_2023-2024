from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework import serializers
from .models import *



class WarriorSerializer(serializers.ModelSerializer):
  class Meta:
     model = Warrior
     fields = "__all__"

class ProfessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"

class WarriorAPIView(APIView):
   def get(self, request):
       warriors = Warrior.objects.all()
       serializer = WarriorSerializer(warriors, many=True)
       return Response({"Warriors": serializer.data})

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

class SkillOfWarriorSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()  # Include SkillSerializer for nested serialization

    class Meta:
        model = SkillOfWarrior
        fields = "__all__"

############################################################

class ProfessionCreateView(APIView):

   def post(self, request):
       profession = request.data.get("profession")
       serializer = ProfessionCreateSerializer(data=profession)

       if serializer.is_valid(raise_exception=True):
           profession_saved = serializer.save()

       return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})

class ProfessionAPIView(APIView):
   def get(self, request):
       profession = Profession.objects.all()
       serializer = ProfessionCreateSerializer(profession, many=True)
       return Response({"Profession": serializer.data})


class WarriorDetailAPIView(APIView):
    def get(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        serializer = WarriorSerializer(warrior)
        return Response(serializer.data)

    def put(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        serializer = WarriorSerializer(warrior, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        warrior.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WarriorsWithProfessionsAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})

class WarriorsWithSkillsAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})

class WarriorFullInfoAPIView(APIView):
    def get(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        warrior_serializer = WarriorSerializer(warrior)

        # Use the correct related name
        skills_serializer = SkillOfWarriorSerializer(warrior.skill.all(), many=True)

        professions_serializer = ProfessionCreateSerializer(warrior.profession)

        return Response({
            "Warrior": warrior_serializer.data,
            "Skills": skills_serializer.data,
            "Profession": professions_serializer.data
        })

