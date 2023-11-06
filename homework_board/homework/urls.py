from django.urls import path
from . import views

urlpatterns = [
    path('homework_list/', views.view_homework),
    path('signup/', views.signup),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('journal/', views.view_journal),
]
