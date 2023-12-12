from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, User, Comment, Subscriptions
from .serializers import PostSerializer, CommentariesSerializer, AuthorsSerializer, SubscriptionSerializer
# Create your views here.

author_name_parameter = "author"

class PostListAPIView(APIView):
    # Parameters
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

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CommentariesAPIView(APIView):

    def get(self, request):
        post_id = int(request.GET.get("id"))

        if post_id:
            post = Post.objects.get(id=post_id)
            commentaries = Comment.objects.filter(post=post)
            comm_count = commentaries.count()
            serialized_comment = CommentariesSerializer(commentaries, many=True)
            return Response({"Commentaries": serialized_comment.data, "Count": str(comm_count)})

    def post(self, request):
        serializer = CommentariesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class AuthorsAPIView(APIView):
    def get(self, request):
        authors = User.objects.all()
        serialized_authors = AuthorsSerializer(authors, many=True)
        return Response({"Authors": serialized_authors.data})


class SubscriptionsAPIView(APIView):
    def get(self, request):
        subscriber_name = request.GET.get(author_name_parameter)
        subscriber = User.objects.get(username=subscriber_name)
        subscriptions = Subscriptions.objects.filter(follower=subscriber)
        serialized_followings = SubscriptionSerializer(subscriptions, many=True)
        return Response({"user": subscriber_name, "Subs": serialized_followings.data})

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)