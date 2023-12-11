from rest_framework import viewsets
from .models import User, Post, Comment, Follow
from .serializers import (
  UserSerializer,
  PostSerializer,
  CommentSerializer,
  FollowSerializer,
)

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class FollowViewSet(viewsets.ModelViewSet):
  queryset = Follow.objects.all()
  serializer_class = FollowSerializer
