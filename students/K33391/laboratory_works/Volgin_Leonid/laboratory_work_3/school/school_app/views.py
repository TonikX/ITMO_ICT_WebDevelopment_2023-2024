from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import *
from .serializers import *


class TeacherListView(generics.ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

class TeacherRetrieveView(generics.RetrieveAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

class TeacherCreateView(generics.CreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

class TeacherUpdateView(generics.UpdateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

class TeacherDeleteView(generics.DestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer




class CabinetListView(generics.ListAPIView):
    queryset = Cabinets.objects.all()
    serializer_class = CabinetSerializer

class CabinetRetrieveView(generics.RetrieveAPIView):
    queryset = Cabinets.objects.all()
    serializer_class = CabinetSerializer

class CabinetCreateView(generics.CreateAPIView):
    queryset = Cabinets.objects.all()
    serializer_class = CabinetSerializer

class CabinetUpdateView(generics.UpdateAPIView):
    queryset = Cabinets.objects.all()
    serializer_class = CabinetSerializer

class CabinetDeleteView(generics.DestroyAPIView):
    queryset = Cabinets.objects.all()
    serializer_class = CabinetSerializer




class ClassListView(generics.ListAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer

class ClassRetrieveView(generics.RetrieveAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer

class ClassCreateView(generics.CreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer

class ClassUpdateView(generics.UpdateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer

class ClassDeleteView(generics.DestroyAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer



class StudentListView(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveView(generics.RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class StudentCreateView(generics.CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateView(generics.UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class StudentDeleteView(generics.DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer




class ScheduleListView(generics.ListAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer

class ScheduleRetrieveView(generics.RetrieveAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer

class ScheduleCreateView(generics.CreateAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer

class ScheduleUpdateView(generics.UpdateAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer

class ScheduleDeleteView(generics.DestroyAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer




class TeachingListView(generics.ListAPIView):
    queryset = Teachings.objects.all()
    serializer_class = TeachingSerializer

class TeachingRetrieveView(generics.RetrieveAPIView):
    queryset = Teachings.objects.all()
    serializer_class = TeachingSerializer

class TeachingCreateView(generics.CreateAPIView):
    queryset = Teachings.objects.all()
    serializer_class = TeachingSerializer

class TeachingUpdateView(generics.UpdateAPIView):
    queryset = Teachings.objects.all()
    serializer_class = TeachingSerializer

class TeachingDeleteView(generics.DestroyAPIView):
    queryset = Teachings.objects.all()
    serializer_class = TeachingSerializer



class SubjectListView(generics.ListAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer

class SubjectRetrieveView(generics.RetrieveAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer

class SubjectCreateView(generics.CreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer

class SubjectUpdateView(generics.UpdateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer

class SubjectDeleteView(generics.DestroyAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer




class GradeListView(generics.ListAPIView):
    queryset = Grades.objects.all()
    serializer_class = SubjectSerializer

class GradeRetrieveView(generics.RetrieveAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer

class GradeCreateView(generics.CreateAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer

class GradeUpdateView(generics.UpdateAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer

class GradeDeleteView(generics.DestroyAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer