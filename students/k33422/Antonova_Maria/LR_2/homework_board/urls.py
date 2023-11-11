from django.urls import path
from . import views



urlpatterns = [
    path('student_homework/', views.student_homework, name='student_homework'),
    path('teacher_answers/', views.teacher_answers, name='teacher_answers'),
]
