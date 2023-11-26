# book_exchange/models.py
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='book_covers/')
    description = models.TextField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_genres = models.CharField(max_length=255)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    text = models.TextField()

class BookList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    list_type = models.CharField(max_length=255)  # Прочитано, Хочу прочитать, Читаю сейчас и т.д.

class BookClub(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class ClubMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(BookClub, on_delete=models.CASCADE)

class ClubPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(BookClub, on_delete=models.CASCADE)
    text = models.TextField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(ClubPost, on_delete=models.CASCADE)
    text = models.TextField()

