from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Comment, Race
from .forms import (
    CommentForm,
    RacerForm,
    RacerUpdateForm,
    RegistrationForm,
    UserUpdateForm,
)

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        racer_form = RacerForm(request.POST)
        if user_form.is_valid() and racer_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            racer = racer_form.save(commit=False)
            racer.user = user
            racer.save()
            return redirect("login")
    else:
        user_form = RegistrationForm()
        racer_form = RacerForm()

    return render(
        request,
        "register.html",
        {"user_form": user_form, "racer_form": racer_form},
    )

def base(request):
    return render(request, "base.html")

@login_required
def scoreboard(request):
    races = Race.objects.all()
    return render(request, "scoreboard.html", {"races": races})

@login_required
def race_comments(request, race_id):
    race = get_object_or_404(Race, id=race_id)
    comments = Comment.objects.filter(race=race)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.race = race
            comment.poster = request.user
            comment.save()
    else:
        form = CommentForm()
    return render(
        request,
        "race_comments.html",
        {"race": race, "comments": comments, "form": form},
    )

@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)

        if "email" in request.POST and user_form.is_valid():
            user_form.save()
        elif "old_password" in request.POST and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
        elif hasattr(request.user, "racer"):
            racer_form = RacerUpdateForm(request.POST, instance=request.user.racer)
            if "team" in request.POST and racer_form.is_valid():
                racer_form.save()
        return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        racer_form = RacerUpdateForm(instance=getattr(request.user, "racer", None))
        password_form = PasswordChangeForm(request.user)

    return render(
        request,
        "profile.html",
        {
            "user_form": user_form,
            "racer_form": racer_form,
            "password_form": password_form,
        },
    )

@login_required
def delete_profile(request):
    if request.method == "POST":
        request.user.delete()
        return redirect("home")
    return render(request, "delete_profile.html")

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("base"))