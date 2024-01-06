from django.contrib.auth import update_session_auth_hash, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Race, Comment, RaceResult
from django.db.models import Min
from .forms import *
from django.urls import reverse
from django.contrib import messages


def user_register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect("tablo")
        else:
            handle_form_errors(request, user_form)

    else:
        user_form = RegistrationForm()

    return render(request, "user_registration.html", {"user_form": user_form})


def base(request):
    return render(request, "base.html")


@login_required
def tablo(request):
    races = Race.objects.all()
    race_results = []

    for race in races:
        winner_result = race.raceresult_set.filter(team=race.winner).aggregate(min_time=Min('time_taken'))
        min_time = winner_result.get('min_time')
        race_results.append({
            'race': race,
            'min_time': min_time,
        })

    return render(request, "tablo.html", {"race_results": race_results})


@login_required
def comments(request, race_id):
    race = get_object_or_404(Race, id=race_id)
    comments = Comment.objects.filter(race=race)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.race = race
            new_comment.author = request.user
            new_comment.save()
    else:
        form = CommentForm()

    return render(
        request,
        "comments.html",
        {"race": race, "comments": comments, "form": form},
    )


def handle_form_errors(request, form):
    for field, errors in form.errors.items():
        for error in errors:
            messages.error(request, f"{field}: {error}")


def user_logout(request):
    logout(request)
    return redirect(reverse('base'))


@login_required
def profile(request):
    user = request.user  # Get the current user
    form = ProfileUpdateForm(instance=user)
    password_form = PasswordChangeCustomForm(user)

    if request.method == 'POST':
        if 'password_change' in request.POST:
            password_form = PasswordChangeCustomForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Пароль успешно изменен.')
                return redirect('profile')
            else:
                handle_form_errors(request, password_form)
                if not user.has_usable_password():
                    messages.error(request, 'Пароль не может быть изменен.')
        else:
            form = ProfileUpdateForm(request.POST, instance=user)
            if form.is_valid():
                user = form.save()
                try:
                    racer = user.racer
                except Racer.DoesNotExist:
                    racer = Racer(user=user)

                team_id = form.cleaned_data.get('team')
                if team_id:
                    team = Team.objects.get(pk=team_id)
                    racer.team = team
                else:
                    racer.team = None  # If no team is selected

                if 'description' in form.cleaned_data:
                    racer.description = form.cleaned_data['description']
                if 'experience' in form.cleaned_data:
                    racer.experience = form.cleaned_data['experience']
                racer.save()
                messages.success(request, 'Информация о профиле успешно обновлена.')
                return redirect('profile')

    return render(request, 'profile.html', {'form': form, 'password_form': password_form})


def all_race_results(request):
    all_results = RaceResult.objects.all()

    # Сортировка результатов по гонкам и времени прохождения
    sorted_results = sorted(all_results, key=lambda x: (x.race.id, x.time_taken))

    return render(request, "all_race_results.html", {"all_results": sorted_results})
