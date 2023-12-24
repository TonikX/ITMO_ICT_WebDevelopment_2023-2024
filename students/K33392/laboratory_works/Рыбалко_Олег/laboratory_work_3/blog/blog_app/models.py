from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  bio = models.TextField(blank=True)
  profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
  title = models.TextField(blank=True)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  likes = models.IntegerField(default=0)

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
  follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
  followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
  created_at = models.DateTimeField(auto_now_add=True)
