from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from warriors_app.models import Warrior, Skill, SkillOfWarrior
from .serializers import ProfessionCreateSerializer, SkillSerializer, WarriorSerializer, SkillOfWarriorSerializer, \
    ProfessionSerializer


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class ProfessionCreateView(APIView):
    def post(self, request):
        profession_data = request.data.get("profession")
        serializer = ProfessionCreateSerializer(data=profession_data)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()
            return Response({"Success": f"Profession '{profession_saved.title}' created successfully."})


class SkillListView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request):
        skill_data = request.data.get("skill")
        serializer = SkillSerializer(data=skill_data)

        if serializer.is_valid():
            skill_saved = serializer.save()
            return Response({"Success": f"Skill '{skill_saved.title}' created successfully."},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WarriorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorProfessionsAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer

    def list(self, request, *args, **kwargs):
        warriors = self.get_queryset()
        data = self.serializer_class(warriors, many=True).data
        return Response(data)


class WarriorSkillsAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        data = []
        for warrior in warriors:
            skills = SkillOfWarrior.objects.filter(warrior=warrior)
            skill_data = SkillOfWarriorSerializer(skills, many=True).data
            data.append({
                'skills': skill_data
            })
        return Response(data)


class WarriorDetailInfoAPIView(APIView):
    def get(self, request, pk):
        warrior = Warrior.objects.get(pk=pk)
        serializer = WarriorSerializer(warrior)
        professions = ProfessionSerializer(warrior.profession).data if warrior.profession else None
        skills = SkillOfWarrior.objects.filter(warrior=warrior)
        skill_data = SkillOfWarriorSerializer(skills, many=True).data
        data = {
            'warrior': serializer.data,
            'professions': professions,
            'skills': skill_data
        }
        return Response(data)


class WarriorCreateAPIView(generics.CreateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorListAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
