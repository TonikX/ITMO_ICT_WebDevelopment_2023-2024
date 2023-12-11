from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, User, Comment
from .serializers import PostSerializer, CommentariesSerializer
# Create your views here.


class PostListAPIView(APIView):
    # Parametres
    author_name_parameter = "author"

    def get_posts_by_author(self, author_name):
        author = User.objects.get(username=author_name)
        posts = Post.objects.filter(author = author)
        serialized_posts = PostSerializer(posts, many=True)
        return serialized_posts

    def get_all_posts(self):
        posts = Post.objects.all()
        serialized_posts = PostSerializer(posts, many=True)
        return serialized_posts

    def get(self, request):
        author_name = request.GET.get(self.author_name_parameter)
        if author_name:
            response = self.get_posts_by_author(author_name)
        else:
            response = self.get_all_posts()

        return Response({"Posts": response.data})


class CommentariesAPIView(APIView):

    def get(self, request):
        post_id = int(request.GET.get("id"))

        if post_id:
            post = Post.objects.get(id=post_id)
            commentaries = Comment.objects.filter(post=post)
            serialized_comment = CommentariesSerializer(commentaries, many=True)
            return Response({"Commentaries": serialized_comment.data})