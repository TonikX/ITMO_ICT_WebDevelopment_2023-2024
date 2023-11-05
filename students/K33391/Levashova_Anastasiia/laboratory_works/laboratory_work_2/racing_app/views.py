from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView
from django.contrib.auth import logout
from .forms import UserRegistrationForm, UserLoginForm, RacerProfileForm, RacerCarForm, CommentForm
from django.contrib import messages

from .models import Race, RaceResult, Registration, Racer, RacerCar, Comment


def home(request):
    return render(request, 'home.html')


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'authorization/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль. Попробуйте снова.')
    else:
        form = UserLoginForm()
    return render(request, 'authorization/login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('/')


def race_list(request):
    races = Race.objects.all()
    context = {
        'races': races,
    }
    return render(request, 'races/race_list.html', context)


def race_detail(request, race_id):
    race = get_object_or_404(Race, pk=race_id)
    current_datetime = timezone.now()
    comments = Comment.objects.filter(race=race)

    if race.date <= current_datetime:
        race_results = RaceResult.objects.filter(race=race)
        context = {
            'race': race,
            'race_results': race_results,
            'comments': comments,
        }
    else:
        registrations = Registration.objects.filter(race=race)
        context = {
            'race': race,
            'registrations': registrations,
            'comments': comments,
        }

    return render(request, 'races/race_detail.html', context)


def registration_list(request):
    user = request.user
    current_datetime = timezone.now()

    if request.method == 'POST':
        registration_id = request.POST.get('registration_id')
        registration = get_object_or_404(Registration, pk=registration_id)

        if registration.race.date > current_datetime:
            return redirect(f'/registrations/registration/delete/{registration_id}')

    registrations = Registration.objects.filter(racer__user=user)

    context = {
        'registrations': registrations,
        'current_datetime': current_datetime
    }
    return render(request, 'registrations/registration_list.html', context)


class DeleteRegistration(DeleteView):
    model = Registration
    template_name = "registrations/registration_delete.html"
    success_url = "/registrations"


# def racer_profile(request):
#     user = request.user
#
#     try:
#         racer = Racer.objects.get(user=user)
#         racer_car = RacerCar.objects.get(racer=racer)
#     except Racer.DoesNotExist:
#         racer = None
#         racer_car = None
#
#     if request.method == 'POST':
#         if racer:
#             car_form = RacerCarForm(request.POST, instance=racer_car)
#             profile_form = RacerProfileForm(request.POST, instance=racer)
#         else:
#             car_form = RacerCarForm(request.POST)
#             profile_form = RacerProfileForm(request.POST)
#
#         if profile_form.is_valid() and car_form.is_valid():
#             if not racer:
#                 racer = profile_form.save(commit=False)
#                 racer.user = user
#             profile_form.save()
#             car_form.instance = racer
#             car_form.save()
#             return redirect('racer_profile')
#
#     else:
#         if racer:
#             profile_form = RacerProfileForm(instance=racer)
#             car_form = RacerCarForm(instance=racer_car)
#         else:
#             profile_form = RacerProfileForm()
#             car_form = RacerCarForm()
#
#     context = {
#         'profile_form': profile_form,
#         'car_form': car_form,
#     }
#
#     return render(request, 'profile/racer_profile.html', context)

def racer_profile(request):
    user = request.user

    try:
        racer = Racer.objects.get(user=user)
    except Racer.DoesNotExist:
        racer = None

    if request.method == 'POST':
        if racer:
            car_form = RacerCarForm(request.POST, instance=racer.car)
            profile_form = RacerProfileForm(request.POST, instance=racer)
        else:
            car_form = RacerCarForm(request.POST)
            profile_form = RacerProfileForm(request.POST)

        if profile_form.is_valid() and car_form.is_valid():
            if not racer:
                racer = profile_form.save(commit=False)
                racer.user = user
                racer.car = car_form.save()
                racer.save()
            else:
                profile_form.save()
                car_form.save()

            return redirect('racer_profile')

    else:
        if racer:
            profile_form = RacerProfileForm(instance=racer)
            car_form = RacerCarForm(instance=racer.car)
        else:
            profile_form = RacerProfileForm()
            car_form = RacerCarForm()

    context = {
        'profile_form': profile_form,
        'car_form': car_form,
    }

    return render(request, 'profile/racer_profile.html', context)


def race_registration(request):
    user = request.user
    current_datetime = timezone.now()

    try:
        racer = Racer.objects.get(user=user)
    except Racer.DoesNotExist:
        return redirect('racer_profile')

    upcoming_races = Race.objects.filter(date__gte=current_datetime).exclude(registration__racer__user=user)

    if request.method == 'POST':
        race_id = request.POST.get('race_id')
        race = get_object_or_404(Race, pk=race_id)
        racer = Racer.objects.get(user=user)

        if race.date >= current_datetime:
            registration, created = Registration.objects.get_or_create(racer=racer, race=race)
            if created:
                registration.save()

    context = {
        'upcoming_races': upcoming_races,
        'current_datetime': current_datetime
    }

    return render(request, 'registrations/race_registration.html', context)


def add_comment(request, race_id):
    race = Race.objects.get(pk=race_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.race = race
            comment.commentator = request.user
            comment.save()
            return redirect('race_detail', race_id=race.id)

    else:
        form = CommentForm()

    context = {
        'race': race,
        'form': form,
    }

    return render(request, 'comments/add_comment.html', context)
