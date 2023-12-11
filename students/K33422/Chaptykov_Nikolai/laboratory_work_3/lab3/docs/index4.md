# Лабораторная работа 3
## Модель базы данных
Хорошей идеей в начале показалось разграничить лекции на несколько сущностей, однако в дальнейшем это принесло много бед
```Python
from django.db import models


DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)


class Tutor(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.surname}"


class AcademicGroup(models.Model):
    group_name = models.CharField(max_length=30)
    faculty = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.group_name}, {self.faculty}"


class Student(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname} {self.group}"


"""
    Discipline хранит название дисциплины, преподавателя и закрепленный
    за ним кабинет. Учитывать проведение лекций и практик в разных 
    аудиториях можно с помощью введения поля для маркера, также можно 
    добавлять уточняющий префикс к названию дисциплины: 'Вышмат лекция'
    и 'Вышмат практика'
"""
class Discipline(models.Model):
    lecturer = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    discipline_name = models.CharField(max_length=30)
    room = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"каб. {self.room}, {self.discipline_name}, ведет {self.lecturer}"


"""
    По одному предмету может быть несколько занятий в разное время,
    введем сущность Lecture чтобы не дублировать данные дисциплин
"""
class Lecture(models.Model):
    discipline = models.ForeignKey(Discipline, related_name='lecture', on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAYS_OF_WEEK, default=0)
    time = models.TimeField(null=True)

    def __str__(self):
        return f"{DAYS_OF_WEEK[self.day][1]} {self.discipline}"


"""
    На одном занятии может находится несколько групп, введем
    ассоциативную сущность между лекцией и группой чтобы это учитывать
"""
class AssignedLecture(models.Model):
    group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE, primary_key=True)
    lecture = models.ManyToManyField(Lecture)

    def __str__(self):
        return f"{self.group}" + f"{self.lecture}"


class AcademicPerformance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)



```
## Сериалайзеры
```Python
from lab_app.models import *
from rest_framework import serializers


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('time', 'discipline')


class AssignedLectureSerializer(serializers.ModelSerializer):
    lecture = LectureSerializer(many=True, read_only=True)
    group_str = serializers.StringRelatedField(source='group')

    class Meta:
        model = AssignedLecture
        fields = ('group', 'group_str', 'lecture')


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ('__all__')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'group']


class StudentCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'group']


class AcademicPerformanceSerializer(serializers.ModelSerializer):
    student_str = serializers.StringRelatedField(source='student')
    subject_str = serializers.StringRelatedField(source='subject')

    class Meta:
        model = AcademicPerformance
        fields = ['student', 'student_str', 'subject', 'subject_str', 'grade']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicGroup
        fields = ('__all__')

```
## Файл urls.py
```Python
"""laboratory_work_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lab_app.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='Conversion, software version 7.0',
      description="Looking at life through the eyes of a tire hub ",
      terms_of_service="Пользуйтесь на здоровье",
      contact=openapi.Contact(email="Не пишите, но если уже начали - не прекращайте, nick.chaptykov@gmail.com"),
      license=openapi.License(name="Лицензия на продажу рыболовных снастей"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('group/', GroupList.as_view()),
    path('group/<int:pk>', GroupDetail.as_view()),
    path('group/<int:pk1>/<int:pk>', StudentDetail.as_view()),
    path('tutor/', TutorList.as_view()),
    path('tutor/<int:pk>', TutorDetail.as_view()),
    path('group/<int:pk>/tutors', GroupTutorsList.as_view()),
    path('group/<int:pk>/cnt', CountStudents.as_view()),
    path('group/timetable/<int:pk1>/<int:pk>', GetTimetable.as_view()),
    path('group/timetable/<int:pk2>/<int:pk1>/<int:pk>', GetTimetableDeeper.as_view()),
    path('tutor/groups/<int:pk1>/<int:pk>', GroupByTutor.as_view()),
    path('group/list_lessons/<int:pk>', ListGroupLessons.as_view()),
    path('group/list_lessons/<int:pk1>/<int:pk>', GroupLessonDetail.as_view()),
    path('group/list_lessons/schedule/<int:pk>', ScheduleGroupLesson.as_view()),
    path('group/list_lessons/create', CreateGroupLesson.as_view()),
    path('student/performance/<int:pk>', StudentPerformance.as_view()),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
```
## Файл View.py
```Python
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
```