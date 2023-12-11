from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from .serializers import *
from .models import *
from django.contrib.auth.models import User, Group


class TutorList(generics.ListCreateAPIView):
    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()


class TutorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()


class GroupList(generics.ListCreateAPIView):
    serializer_class = GroupSerializer
    
    def get_queryset(self):
        queryset = AcademicGroup.objects.all()
        return queryset


class GroupDetail(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all().filter(group=self.kwargs['pk'])
        return queryset


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all().filter(group=self.kwargs['pk1'], id=self.kwargs['pk'])
        return queryset


# list of tutors for a group
class GroupTutorsList(generics.ListAPIView):
    serializer_class = AssignedLectureSerializer

    def get(self, request, pk, format=None):
        user_count = AssignedLecture.objects.filter(group=self.kwargs['pk']).values_list("lecture")
        user_count = Lecture.objects.filter(pk__in=user_count).values_list("discipline").distinct()
        user_count = Discipline.objects.filter(pk__in=user_count).values("lecturer__name", "lecturer__surname", "discipline_name")
        return Response({"res": user_count})


# timetable from day of week
class GetTimetable(generics.ListAPIView):
    serializer_class = AssignedLectureSerializer

    def get(self, request, pk1, pk, format=None):
        user_count = AssignedLecture.objects.filter(group=pk1).values_list("lecture")
        user_count = Lecture.objects.filter(pk__in=user_count, day=pk).values("discipline__discipline_name", "day", "time")
        return Response({"res": user_count})


class GetTimetableDeeper(generics.ListAPIView):
    serializer_class = AssignedLectureSerializer

    def get(self, request, pk2, pk1, pk, format=None):
        user_count = AssignedLecture.objects.filter(group=pk1).values_list("lecture")
        user_count = Lecture.objects.filter(pk__in=user_count, day=pk).order_by("time").values("discipline__discipline_name", "day", "time")
        try: 
            return Response({"res": user_count[pk2]})
        except Exception:
            return Response({"res": "Что-то пошло не так"}) 


class GroupByTutor(generics.ListAPIView):
    serializer_class = AssignedLectureSerializer

    def get(self, request, pk1, pk, format=None):
        user_count = AssignedLecture.objects.filter(lecture__discipline__lecturer_id=pk1, lecture__discipline_id=pk).values("group__group_name").distinct()
        return Response({"res": user_count})

from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response


class CountStudents(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCountSerializer

    def get(self, request, pk, format=None):
        user_count = Student.objects.filter(group=self.kwargs['pk']).count()
        content = {'student_count': user_count}
        return Response(content)


class ListGroupLessons(generics.ListAPIView):
    serializer_class = AssignedLectureSerializer

    def get(self, request, pk, format=None):
        user_count = AssignedLecture.objects.filter(group=pk).values(
                "lecture__id",
                "lecture__discipline__lecturer__name",
                "lecture__discipline__lecturer__surname",
                "lecture__discipline__discipline_name")
        return Response({"res": user_count})


class GroupLessonDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LectureSerializer

    def get_queryset(self):
        queryset = Lecture.objects.filter(id=self.kwargs['pk'])
        # queryset = queryset.values()
        return queryset


class ScheduleGroupLesson(generics.ListCreateAPIView):
    serializer_class = LectureSerializer

    def get_queryset(self):
        queryset = Lecture.objects.filter(id=self.kwargs['pk'])
        # queryset = queryset.values()
        return queryset


class CreateGroupLesson(generics.ListCreateAPIView):
    serializer_class = AssignedLectureSerializer

    def get_queryset(self):
        queryset = [AssignedLecture.objects.first()]
        # queryset = queryset.values()
        return queryset


class StudentPerformance(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AcademicPerformanceSerializer

    def get_queryset(self):
        queryset = AcademicPerformance.objects.filter(student=self.kwargs['pk'])
        # queryset = queryset.values()
        return queryset