from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    imageURL = models.URLField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Subscriptions(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Followings")
