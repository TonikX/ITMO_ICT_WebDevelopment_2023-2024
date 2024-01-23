from django.urls import path
from . import views


urlpatterns = [
    path('teacher/new', views.teacher_form_view),
    path('teacher/success', views.teacher_add_success_view),
    path('student/new', views.student_form_view),
    path('student/success', views.student_add_success_view),
    path('homeworks', views.homeworks_view),
    path('homeworks/new/<hw_id>', views.solution_form_view),
    path('solution/success', views.solution_add_success_view),
    path('register', views.register_view),
]
