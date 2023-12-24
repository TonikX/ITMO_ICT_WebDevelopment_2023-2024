from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Race, Comment
from .forms import (
    RegistrationForm,
    RacerForm,
    CommentForm,
    UserUpdateForm,
    RacerUpdateForm,
)


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("login")
    else:
        user_form = RegistrationForm()

    return render(request, "register_user.html", {"user_form": user_form})


def register_racer(request):
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
        "register_racer.html",
        {"user_form": user_form, "racer_form": racer_form},
    )


def home(request):
    return render(request, "home.html")


@login_required
def races_list(request):
    races = Race.objects.all()
    return render(request, "races_list.html", {"races": races})


@login_required
def race_comments(request, race_id):
    race = get_object_or_404(Race, id=race_id)
    comments = Comment.objects.filter(race=race)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.race = race
            comment.author = request.user
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
        racer_form = (
            RacerUpdateForm(instance=getattr(request.user, "racer", None))
            if hasattr(request.user, "racer")
            else None
        )
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
