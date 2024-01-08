from django.http import Http404
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, LoginForm, CommentForm
from .models import User, Race, Register, Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.crypto import get_random_string
from django.db.models import Q


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
