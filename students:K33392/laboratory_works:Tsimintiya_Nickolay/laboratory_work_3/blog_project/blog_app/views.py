from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, User
from .serializers import PostSerializer
# Create your views here.


class PostListAPIView(APIView):
    # Parametres
    author_name_parameter = "author"

    def get_posts_by_author(self, author_name):
        author = User.objects.get(username=author_name)
        posts = Post.objects.filter(author = author)
        serialized_posts = PostSerializer(posts, many=True)
        return Response({"Posts": serialized_posts.data})

    def get(self, request):
        author_name = request.GET.get(self.author_name_parameter)
        if author_name:
            return self.get_posts_by_author(author_name)

        posts = Post.objects.all()
        single_post = posts[0]
        author = single_post.author
        print(author.username)
        serializer = PostSerializer(posts, many=True)

        return Response({"Posts": serializer.data})