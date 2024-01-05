from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

# handler404 = 'homeworks.views.handler404'todo

urlpatterns = [
    #  Student
    path('', views.home, name='home'),
    path('homeworks/<int:subject_id>', views.index_homeworks, name='homeworks.index'),
    path('homeworks/show/<int:hw_id>', views.show_homeworks, name='homeworks.show'),
    path('submissions/', views.store_submission, name='submissions.store'),

    #  Teacher
    path('journal', views.journal, name='journal'),
    path('submissions/<int:s_id>', views.show_submission, name='submissions.show'),
    path('grades', views.store_grade, name='grades.store'),

    #  Auth
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    #  System
    # path('not_found/', views.not_found, name='404'),
]
