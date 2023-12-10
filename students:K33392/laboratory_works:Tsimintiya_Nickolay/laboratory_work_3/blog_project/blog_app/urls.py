from django.contrib import admin
from django.urls import path, include
from .views import PostListAPIView

# Отображение всех постов

urlpatterns = [
    path('posts/', PostListAPIView.as_view())
]
