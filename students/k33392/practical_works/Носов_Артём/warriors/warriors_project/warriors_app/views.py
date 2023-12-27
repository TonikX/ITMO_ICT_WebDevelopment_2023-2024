from django.shortcuts import render

from rest_framework.views import APIView, Response
from rest_framework import generics

from warriors_app.models import Warrior
from warriors_app.serializers import *


# class WarriorAPIView(APIView):
#    def get(self, request):
#        warriors = Warrior.objects.all()
#        serializer = WarriorSerializer(warriors, many=True)
#        print(serializer.data)
#        return Response({"Warriors": serializer.data})

class WarriorListAPIView(generics.ListAPIView):
   serializer_class = WarriorSerializer
   queryset = Warrior.objects.all()

class WarriorGETAPIView(generics.ListAPIView):
    serializer_class = WarriorSerializer
   
#    def get_record(self):
#       print(self.lookup_url_kwarg)
#       print(self.lookup_url_kwarg)
#       print(self.lookup_url_kwarg)
#       return Warrior.objects.all()
    def get_queryset(self):
        # print(self.request.pk)
        # print(self.lookup_url_kwarg)
        # print(self.format_kwarg)
        # print(self.headers)
        # print(self.lookup_field)
        # print(self.__dict__)
        # print(self)
        # print(111111)
        return Warrior.objects.filter(id=self.kwargs['pk'])
   # queryset = Warrior.objects.filter()
    
    
class WarriorDestroyAPIView(generics.DestroyAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()

class WarriorUpdateAPIView(generics.UpdateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


# class ProfessionCreateView(APIView):

#    def post(self, request):
#        profession = request.data.get("profession")
#        serializer = ProfessionCreateSerializer(data=profession)

#        if serializer.is_valid(raise_exception=True):
#            profession_saved = serializer.save()

#        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})
   
# class ProfessionCreateView(APIView):
#     def post(self, request):
#         profession = request.data.get("profession")

#         serializer = ProfessionCreateSerializer(data=profession)

#         if serializer.is_valid(raise_exception=True):
#             profession_saved = serializer.save()

#         return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})

# class ProfessionCreateView(APIView):

#    def post(self, request):
#        print("REQUEST DATA", request.data)
#        profession = request.data.get("profession")
#        print("PROF DATA", profession)

#        serializer = ProfessionCreateSerializer(data=profession)

#        if serializer.is_valid(raise_exception=True):
#            profession_saved = serializer.save()

#        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})

class ProfessionCreateAPIView(generics.CreateAPIView):
   serializer_class = ProfessionSerializer
   queryset = Profession.objects.all()
   
class SkillOfWarriorAPIView(APIView):
   def get(self, request):
       skills_of_warrior = SkillOfWarrior.objects.all()
       serializer = SkillOfWarriorSerializer(skills_of_warrior, many=True)
       print(serializer.data)
       return Response({"Skills of warrior": serializer.data})

class SkillOfWarriorCreateView(APIView):

   def post(self, request):
       skill_of_warrior = request.data.get("skill_of_warrior")
       serializer = SkillOfWarriorCreateSerializer(data=skill_of_warrior)

       if serializer.is_valid(raise_exception=True):
           skill_of_warrior_saved = serializer.save()

       return Response({"Success": "Skill of warrior '{}' created succesfully.".format(skill_of_warrior_saved.level)})