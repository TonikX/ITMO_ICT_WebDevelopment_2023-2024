from django.urls import path, include
from .views import UserRegister, UserEditing
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegister.as_view(), name = 'register'),
    path('edit_profile/', UserEditing.as_view(), name = 'edit'),
    path('password/', auth_views.PasswordChangeView.as_view()),
    
]
