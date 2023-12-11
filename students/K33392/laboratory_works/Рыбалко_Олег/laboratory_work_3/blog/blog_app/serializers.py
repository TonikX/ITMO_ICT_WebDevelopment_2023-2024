from rest_framework import serializers
from blog_app.models import User, Post, Comment, Follow

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = (
      "id",
      "username",
      "email",
      "first_name",
      "last_name",
      "bio",
      "profile_picture",
    )

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ("id", "author", "content", "created_at", "likes")

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ("id", "post", "author", "content", "created_at")

class FollowSerializer(serializers.ModelSerializer):
  class Meta:
    model = Follow
    fields = ("id", "follower", "followed", "created_at")