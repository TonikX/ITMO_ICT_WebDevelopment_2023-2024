from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from blog_app.models import User, Post, Comment, Follow
from django.shortcuts import get_object_or_404
from blog_app.serializers import (
  MyUserSerializer,
  PostSerializer,
  CommentSerializer,
  FollowSerializer,
)

class UserViewSet(viewsets.ModelViewSet):
  permission_classes = [AllowAny]
  queryset = User.objects.all()
  serializer_class = MyUserSerializer

class UsernameViewSet(viewsets.ViewSet):
  def partial_update(self, req:Request, pk=None):
    queryset = User.objects.all()
    user = get_object_or_404(queryset, username=pk)
    user.__dict__.update(req.data)
    user.save()
    return Response()
  def retrieve(self, _, pk=None):
    queryset = User.objects.all()
    serializer = MyUserSerializer(get_object_or_404(queryset, username=pk))
    return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all().order_by('-created_at')
  serializer_class = PostSerializer

  def create(self, request):
    request.data["author_id"] = request.user.pk
    post = Post()
    post.__dict__.update(request.data)
    post.save()
    serializer = PostSerializer(post)
    return Response(serializer.data)
  
class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class FollowViewSet(viewsets.ModelViewSet):
  queryset = Follow.objects.all()
  serializer_class = FollowSerializer
