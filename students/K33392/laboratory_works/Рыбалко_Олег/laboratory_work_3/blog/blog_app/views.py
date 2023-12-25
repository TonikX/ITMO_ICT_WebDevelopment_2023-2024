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

  def create(self, request: Request):
    request.data["author_id"] = request.user.pk
    post = Post()
    post.__dict__.update(request.data)
    post.save()
    serializer = PostSerializer(post)
    return Response(serializer.data)
  
class PostCommentsViewSet(viewsets.ViewSet):
  def retrieve(self, req:Request, pk=None):
    queryset = Comment.objects.all().filter(post=pk)
    if (page := req.query_params.get("page")) is not None:
      page, per_page = int(page), int(req.query_params.get("perPage", 2))
      queryset = queryset[page*per_page:page*per_page+per_page]
    serializer = CommentSerializer(queryset, many=True)
    return Response(serializer.data)
  def create(self, request: Request):
    comment = Comment()
    comment.author = request.user
    comment.content = request.data["content"]
    comment.post = get_object_or_404(Post.objects.all(), pk=request.data["post"])
    comment.save()
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
  
class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class FollowViewSet(viewsets.ModelViewSet):
  queryset = Follow.objects.all()
  serializer_class = FollowSerializer
