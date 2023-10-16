from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login/", views.login_request, name="login"),
    path('register/', views.register_request, name='register'),
    path("logout", views.logout_request, name="logout"),

    path('homepage/', views.homepage, name='homepage'),

    path('class_info/<int:class_id>/', views.class_info, name='class_info'),

    path('user_profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('update_user_profile/<int:user_id>/', views.update_user_profile, name='update_user_profile'),

    path('student_homeworks/', views.student_homeworks, name='student_homeworks'),
    path('homework/<int:pk>/', views.homework_detail, name='homework_detail'),

    path('add_homework/', views.add_homework, name='add_homework'),
    path('update_homework/<int:pk>/', views.update_homework, name='update_homework'),
    path('delete_homework/<int:pk>/', views.delete_homework, name='delete_homework'),
    path('all_homeworks/', views.all_homeworks, name='all_homeworks'),
    path('teacher_homework/<int:pk>/', views.teacher_homework_detail, name='teacher_homework_detail'),

    path('submitted_homeworks/<int:pk>/', views.submitted_homeworks, name='submitted_homeworks'),
    path('submitted_homework_detail/<int:pk>/', views.submitted_homework_detail, name='submitted_homework_detail'),

]
