from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from warriors_app.models import *
from warriors_app.serializers import *


# Create your views here.
class WarriorListAPIView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


# class ProfessionCreateView(APIView):
#
#     def post(self, request):
#         profession = request.data.get("profession")
#         serializer = ProfessionSerializer(data=profession)
#
#         if serializer.is_valid(raise_exception=True):
#             profession_saved = serializer.save()
#
#         return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})

class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"skills": serializer.data})


class SkillCreateView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response(
            {"Success": "Skill '{}' created succesfully.".format(skill_saved.title)}
        )


class WarriorDetail(generics.RetrieveAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorWithProfessionsView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorWithProfessionsSerializer


class WarriorWithSkillsView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorWithSkillsSerializer


class WarriorUpdate(generics.UpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorDelete(generics.DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
