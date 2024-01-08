from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import *
from .models import *


''' 
User Views
'''

class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserCreate(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserDelete(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


'''
Courses Views
'''

class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourseCreate(generics.CreateAPIView):
    serializer_class = CourseCreateSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class CourseDetail(generics.RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class CoursesStudents(generics.ListAPIView):
    serializer_class = CourseStudentSerializer
    queryset = CourseStudent.objects.all()
    permission_classes = [IsAuthenticated]


class CoursesTeachers(generics.ListAPIView):
    serializer_class = CourseTeacherSerializer
    queryset = CourseTeacher.objects.all()
    permission_classes = [IsAuthenticated]


class CourseStudentCreate(generics.CreateAPIView):
    serializer_class = CourseStudentSerializer
    queryset = CourseStudent.objects.all()
    permission_classes = [IsAuthenticated]


class CourseTeacherCreate(generics.CreateAPIView):
    serializer_class = CourseStudentSerializer
    queryset = CourseTeacher.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class CourseStudentDelete(generics.DestroyAPIView):
    serializer_class = CourseStudentSerializer
    queryset = CourseStudent.objects.all()
    permission_classes = [IsAuthenticated]


class CourseTeacherDelete(generics.DestroyAPIView):
    serializer_class = CourseStudentSerializer
    queryset = CourseTeacher.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class CourseUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]


class CourseDelete(generics.DestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


''' 
Subjects Views
'''

class SubjectList(generics.ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]


class SubjectCreate(generics.CreateAPIView):
    serializer_class = SubjectCreateSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]


class SubjectDetail(generics.RetrieveAPIView):
    serializer_class = SubjectDetailSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]


class SubjectUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]


class SubjectDelete(generics.DestroyAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]


''' 
Lessons Views
'''

class LessonList(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonCreate(generics.CreateAPIView):
    serializer_class = LessonCreateSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonDetail(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonDelete(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


''' 
Applications Views
'''

class ApplicationList(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    permission_classes = [IsAuthenticated]


class ApplicationCreate(generics.CreateAPIView):
    serializer_class = ApplicationCreateSerializer
    queryset = Application.objects.all()
    permission_classes = [IsAuthenticated]


class ApplicationReview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicationReviewSerializer
    queryset = Application.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.status == Application.APPROVED:
            # Create CourseStudent if application is approved
            CourseStudent.objects.create(course=instance.course, user=instance.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ApplicationDetail(generics.RetrieveAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    permission_classes = [IsAuthenticated]


class ApplicationUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    permission_classes = [IsAuthenticated]


class ApplicationDelete(generics.DestroyAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    permission_classes = [IsAuthenticated]