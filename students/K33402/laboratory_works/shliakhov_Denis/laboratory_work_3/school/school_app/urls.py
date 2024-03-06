from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [

    path('teacher/all/', TeacherListView.as_view()),
    path('teacher/<int:pk>/', TeacherRetrieveView.as_view()),
    path('teacher/create/', TeacherCreateView.as_view()),
    path('teacher/update/<int:pk>/', TeacherUpdateView.as_view()),
    path('teacher/delete/<int:pk>/', TeacherDeleteView.as_view()),

    path('group/all/', GroupListView.as_view()),
    path('group/<int:pk>/', GroupRetrieveView.as_view()),
    path('group/create/', GroupCreateView.as_view()),
    path('group/update/<int:pk>/', GroupUpdateView.as_view()),
    path('group/delete/<int:pk>/', GroupDeleteView.as_view()),

    path('student/all/', StudentListView.as_view()),
    path('student/<int:pk>/', StudentRetrieveView.as_view()),
    path('student/create/', StudentCreateView.as_view()),
    path('student/update/<int:pk>/', StudentUpdateView.as_view()),
    path('student/delete/<int:pk>/', StudentDeleteView.as_view()),

    path('lesson/all/', LessonListView.as_view()),
    path('lesson/<int:pk>/', LessonRetrieveView.as_view()),
    path('lesson/create/', LessonCreateView.as_view()),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view()),
    path('lesson/delete/<int:pk>/', LessonDeleteView.as_view()),

    path('teach/all/', TeachProcessListView.as_view()),
    path('teach/<int:pk>/', TeachProcessRetrieveView.as_view()),
    path('teach/create/', TeachProcessCreateView.as_view()),
    path('teach/update/<int:pk>/', TeachProcessUpdateView.as_view()),
    path('teach/delete/<int:pk>/', TeachProcessDeleteView.as_view()),

    path('subject/all/', SubjectListView.as_view()),
    path('subject/<int:pk>/', SubjectRetrieveView.as_view()),
    path('subject/create/', SubjectCreateView.as_view()),
    path('subject/update/<int:pk>/', SubjectUpdateView.as_view()),
    path('subject/delete/<int:pk>/', SubjectDeleteView.as_view()),

    path('grade/all/', GradeListView.as_view()),
    path('grade/<int:pk>/', GradeRetrieveView.as_view()),
    path('grade/create/', GradeCreateView.as_view()),
    path('grade/update/<int:pk>/', GradeUpdateView.as_view()),
    path('grade/delete/<int:pk>/', GradeDeleteView.as_view()),

    path('auth/', include('djoser.urls')),
    path('auth/token/', obtain_auth_token),
    path('logout/', Logout.as_view()),

]