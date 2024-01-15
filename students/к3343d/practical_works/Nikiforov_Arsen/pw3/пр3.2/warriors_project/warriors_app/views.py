from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Warrior
from .serializers import *  



class WarriorWithProfessionAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorWithProfessionSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})

class ProfessionCreateView(APIView):
    def post(self, request):
        profession_data = request.data.get("profession")
        serializer = ProfessionCreateSerializer(data=profession_data)
        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()
        return Response({"Success": "Profession '{}' created successfully.".format(profession_saved.title)})

class WarriorWithSkillsAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorWithSkillsSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})
    
class WarriorDetailsAPIView(APIView):
    def get(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        serializer = WarriorWithProfessionSerializer(warrior)
        return Response(serializer.data)
    
class WarriorDeleteAPIView(APIView):
    def delete(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        warrior.delete()
        return Response({"Success": f"Warrior with id {pk} deleted successfully."})

class WarriorUpdateAPIView(APIView):
    def put(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        serializer = WarriorWithProfessionSerializer(warrior, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": f"Warrior with id {pk} updated successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
