from django.contrib import admin
from django.urls import path, include
from .views import PostListAPIView, CommentariesAPIView, AuthorsAPIView, SubscriptionsAPIView

# Список всех постов
# Список всех постов определенного автора
# Создание поста определенным автором

# Комментарии к посту
# Создание комментария определенным автором

# Список всех авторов

urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/commentaries', CommentariesAPIView.as_view()),
    path('authors/', AuthorsAPIView.as_view()),
    path('subscriptions/', SubscriptionsAPIView.as_view())
]
