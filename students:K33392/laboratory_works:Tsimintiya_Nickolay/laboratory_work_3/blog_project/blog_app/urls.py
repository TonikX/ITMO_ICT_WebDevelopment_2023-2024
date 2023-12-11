from django.contrib import admin
from django.urls import path, include
from .views import PostListAPIView

# Список всех постов
# Список всех постов определенного автора

urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
]
