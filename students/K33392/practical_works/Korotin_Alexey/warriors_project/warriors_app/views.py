from rest_framework.response import *
from rest_framework.views import APIView
from rest_framework.generics import *

from .serializers import *


class WarriorSkillsAPIView(APIView):

    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"skills": serializer.data})

    def post(self, request):
        skill = request.data
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)


class WarriorProfessionListAPIView(ListAPIView):
    serializer_class = WarriorProfessionSerializer
    queryset = Warrior.objects.all()


class WarriorSkillListApiView(ListAPIView):
    serializer_class = WarriorSkillSerializer
    queryset = Warrior.objects.all()


class GetWarriorAPIView(RetrieveAPIView):
    serializer_class = FullWarriorSerializer
    queryset = Warrior.objects.all()


class UpdateWarriorAPIView(UpdateAPIView):
    serializer_class = FullWarriorSerializer
    queryset = Warrior.objects.all()


class DeleteWarriorAPIView(DestroyAPIView):
    serializer_class = FullWarriorSerializer
    queryset = Warrior.objects.all()
