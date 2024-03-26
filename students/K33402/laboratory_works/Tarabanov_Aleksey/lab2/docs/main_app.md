# MainApp

## admin.py
регистрируем все модели
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Race)
admin.site.register(models.Register)
admin.site.register(models.Comment)
```
    
## apps.py
Объявляем класс
```python
from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'
    verbose_name = 'Автогонки'
```
    
## forms.py
все формы которые мы можем заполнять и отправлять, т.е. форма логина, регистрации и форма где мы оставляем комментарий
```python
from django import forms
from .models import User, Register, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["type", "rating", "message"]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email",
                  "description", "rating", "team", "car_num", "car_description"]
```
    
## models.py
все сущности которые используются
```python
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    description = models.TextField()
    team = models.CharField(max_length=100)
    rating = models.CharField(max_length=15,
                              choices=(('beginner', 'beginner'), ('middle', 'middle'), ('profy', 'profy')))
    car_num = models.CharField(max_length=30)
    car_description = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Race(models.Model):
    name = models.CharField(max_length=100)
    when = models.DateField()
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Гонка'
        verbose_name_plural = 'Гонки'


class Register(models.Model):
    racer = models.ForeignKey(User, related_name='where_to_drive', on_delete=models.CASCADE)
    race = models.ForeignKey(Race, related_name='who_drive', on_delete=models.CASCADE)
    result = models.IntegerField(blank=True, null=True, )
    time_result = models.FloatField(blank=True, null=True, )

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрации'


class Comment(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, default="collaboration",
                            choices=(('collaboration', 'collaboration'),
                                     ('racing', 'racing'),
                                     ('other', 'other')))
    message = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
```
    
## urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="user_register"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("races/", views.races_list, name="races_list"),
    path("races/<int:race_id>/", views.race_detail, name="race_detail"),
    path("registrations/", views.regs_for_user, name="your_regs"),
    path("registrations/<int:reg_id>/delete", views.reg_delete, name="reg_delete")
]
```
    
## views.py
тут описана вся логика сайта
```python
from django.contrib.auth import login, authenticate, logout
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistrationForm, LoginForm, CommentForm
from .models import Race, Register, Comment


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("user_login")
    else:
        user_form = RegistrationForm()

    return render(request, "register.html", {"user_form": user_form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        username = form.data.get("username")
        password = form.data.get("password")
        user = authenticate(username=username, password=password)

        if user is None:
            return redirect("user_login")

        login(request, user)
        return redirect("races_list")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("user_login")


def races_list(request):
    if request.method != "GET":
        return Http404(f"Method {request.method} not supported")

    races = Race.objects.all()

    return render(
        request,
        "races_list.html",
        {"races": races},
    )


def race_detail(request, race_id):
    race = get_object_or_404(Race, pk=race_id)

    if request.method == "POST":
        if "rating" in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.race = race
                comment.writer = request.user
                comment.save()
        else:
            Register.objects.create(racer=request.user, race=race)

        return redirect("race_detail", race_id)

    else:
        has_reg = Register.objects.filter(
            racer__id=request.user.id, race__id=race_id
        ).exists()

        regs = Register.objects.filter(race=race_id).order_by('result')

        comment_form = CommentForm()
        comments = Comment.objects.filter(race=race_id)

        return render(
            request,
            "race_detail.html",
            {
                "race": race,
                "has_no_reg": not has_reg,
                "user": request.user,
                "regs": regs,
                "comments": comments,
                'comment_form': comment_form,
            },
        )


def regs_for_user(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    regs = Register.objects.filter(racer=request.user)
    return render(request, "regs_of_user.html", {"regs": regs})


def reg_delete(request, reg_id):
    reg = get_object_or_404(Register, id=reg_id, racer=request.user)

    if request.method == "POST":
        reg.delete()
        return redirect("your_regs")
    else:
        return render(
            request,
            "reg_delete.html",
            {"reg": reg},
        )
```