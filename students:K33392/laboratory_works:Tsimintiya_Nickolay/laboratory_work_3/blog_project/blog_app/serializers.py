from rest_framework import serializers
from .models import Post, Comment, User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        depth = 1


class CommentariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["post"]
        depth = 1


class AuthorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ["is_superuser"]
