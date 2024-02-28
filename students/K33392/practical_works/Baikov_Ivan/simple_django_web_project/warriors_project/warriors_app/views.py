from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from .models import *
from .serializers import *


class WarriorList(generics.ListCreateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer

class WarriorDetail(generics.RetrieveAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorUpdate(generics.UpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorDelete(generics.DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorViewSet(viewsets.ModelViewSet):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


#####


class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


#####


class ProfessionList(generics.ListCreateAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class ProfessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


#####


class SkillOfWarriorViewSet(viewsets.ModelViewSet):
    queryset = SkillOfWarrior.objects.all()
    serializer_class = SkillOfWarriorSerializer


class WarriorWithProfessionsView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorWithProfessionsSerializer


class WarriorWithSkillsView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorWithSkillsSerializer

#
# class SkillAPIView(APIView):
#     def get(self, request):
#         skills = Skill.objects.all()
#         serializer = SkillSerializer(skills, many=True)
#         return Response({"Skills": serializer.data})
#
#
# class SkillCreateView(APIView):
#     def post(self, request):
#         skill = request.data.get("skill")
#         serializer = SkillCreateSerializer(data=skill)
#         if serializer.is_valid(raise_exception=True):
#             skill_saved = serializer.save()
#         return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})
#
