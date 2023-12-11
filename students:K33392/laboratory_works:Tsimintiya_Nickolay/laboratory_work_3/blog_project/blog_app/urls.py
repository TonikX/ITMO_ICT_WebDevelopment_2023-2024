from django.contrib import admin
from django.urls import path, include
from .views import PostListAPIView, CommentariesAPIView

# Список всех постов
# Список всех постов определенного автора
# Комментарии к посту

urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/commentaries', CommentariesAPIView.as_view())
]
