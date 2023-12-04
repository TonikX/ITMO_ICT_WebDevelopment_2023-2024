from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path('register/', views.UserRegisterView.as_view(), name='register'),
	path('login/', views.UserLoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout')
]