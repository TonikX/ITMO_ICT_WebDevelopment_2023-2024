from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from .serializers import *
from .models import *
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import *
import logging


def signup(request):
    if request.method == 'POST':
        form = FormForUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('http://127.0.0.1:8000/group/')
    else:
        form = FormForUser()
    return render(request, 'register.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('http://127.0.0.1:8000/group/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.contrib.auth.models import User


@csrf_exempt
@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def sign_in_js(request):
    request_json = json.loads(request.body)
    print(request.body)
    username = request_json['username']
    password = request_json['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user=user)
        # token, created = Token.objects.get_or_create(user=user)
        return Response(status=200)
    else:
        return Response(status=404)


@csrf_exempt
@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def sign_up_js(request):
    request_json = json.loads(request.body)
    username = request_json['username']
    password = request_json['password']
    user = User.objects.create_user(username=username, password=password)
    if user is not None:
        return Response(status=200)
    else:
        return Response(status=404)


@csrf_exempt
def get_group_list(request):
    groups = AcademicGroup.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_group_js(request, pk):
    students = Student.objects.all().filter(group=pk)
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_tutor_list(request):
    tutors = Tutor.objects.all().filter()
    serializer = TutorSerializer(tutors, many=True)
    return JsonResponse(serializer.data, safe=False)


class TutorList(LoginRequiredMixin, generics.ListCreateAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()


class TutorDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()


class GroupList(LoginRequiredMixin, generics.ListCreateAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = GroupSerializer
    
    def get_queryset(self):
        queryset = AcademicGroup.objects.all()
        return queryset


class GroupDetail(LoginRequiredMixin, generics.ListCreateAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all().filter(group=self.kwargs['pk'])
        return queryset


class StudentDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all().filter(group=self.kwargs['pk1'], id=self.kwargs['pk'])
        return queryset


# list of tutors for a group
class GroupTutorsList(LoginRequiredMixin, generics.ListAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = AssignedLectureSerializer

    def get(self, request, pk, format=None):
        user_count = AssignedLecture.objects.filter(group=self.kwargs['pk']).values_list("lecture")
        user_count = Lecture.objects.filter(pk__in=user_count).values_list("discipline").distinct()
        user_count = Discipline.objects.filter(pk__in=user_count).values("lecturer__name", "lecturer__surname", "discipline_name")
        return Response({"res": user_count})


# timetable from day of week
class GetTimetable(LoginRequiredMixin, generics.ListAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = AssignedLectureSerializer

    def get(self, request, pk1, pk, format=None):
        user_count = AssignedLecture.objects.filter(group=pk1).values_list("lecture")
        user_count = Lecture.objects.filter(pk__in=user_count, day=pk).values("discipline__discipline_name", "day", "time")
        return Response({"res": user_count})


class GetTimetableDeeper(LoginRequiredMixin, generics.ListAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = AssignedLectureSerializer

    def get(self, request, pk2, pk1, pk, format=None):
        user_count = AssignedLecture.objects.filter(group=pk1).values_list("lecture")
        user_count = Lecture.objects.filter(pk__in=user_count, day=pk).order_by("time").values("discipline__discipline_name", "day", "time")
        try: 
            return Response({"res": user_count[pk2]})
        except Exception:
            return Response({"res": "Что-то пошло не так"}) 


class GroupByTutor(LoginRequiredMixin, generics.ListAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = AssignedLectureSerializer

    def get(self, request, pk1, pk, format=None):
        user_count = AssignedLecture.objects.filter(lecture__discipline__lecturer_id=pk1, lecture__discipline_id=pk).values("group__group_name").distinct()
        return Response({"res": user_count})

from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response


class CountStudents(LoginRequiredMixin, generics.ListAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    queryset = Student.objects.all()
    serializer_class = StudentCountSerializer

    def get(self, request, pk, format=None):
        user_count = Student.objects.filter(group=self.kwargs['pk']).count()
        content = {'student_count': user_count}
        return Response(content)


class ListGroupLessons(LoginRequiredMixin, generics.ListAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = AssignedLectureSerializer

    def get(self, request, pk, format=None):
        user_count = AssignedLecture.objects.filter(group=pk).values(
                "lecture__id",
                "lecture__discipline__lecturer__name",
                "lecture__discipline__lecturer__surname",
                "lecture__discipline__discipline_name")
        return Response({"res": user_count})


class GroupLessonDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = LectureSerializer

    def get_queryset(self):
        queryset = Lecture.objects.filter(id=self.kwargs['pk'])
        # queryset = queryset.values()
        return queryset


class ScheduleGroupLesson(LoginRequiredMixin, generics.ListCreateAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = LectureSerializer

    def get_queryset(self):
        queryset = Lecture.objects.filter(id=self.kwargs['pk'])
        # queryset = queryset.values()
        return queryset


class CreateGroupLesson(LoginRequiredMixin, generics.ListCreateAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = AssignedLectureSerializer

    def get_queryset(self):
        queryset = [AssignedLecture.objects.first()]
        # queryset = queryset.values()
        return queryset


class StudentPerformance(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    raise_exception = True
    permission_denied_message = "You are not allowed here."
    serializer_class = AcademicPerformanceSerializer

    def get_queryset(self):
        queryset = AcademicPerformance.objects.filter(student=self.kwargs['pk'])
        # queryset = queryset.values()
        return queryset