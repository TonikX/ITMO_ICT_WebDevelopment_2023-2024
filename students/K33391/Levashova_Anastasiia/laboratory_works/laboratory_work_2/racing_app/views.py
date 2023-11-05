from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView

from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
from .models import Race, RaceResult, Registration


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


def race_list(request):
    races = Race.objects.all()
    context = {
        'races': races,
    }
    return render(request, 'races/race_list.html', context)


def race_detail(request, race_id):
    race = get_object_or_404(Race, pk=race_id)
    current_datetime = timezone.now()

    if race.date <= current_datetime:
        race_results = RaceResult.objects.filter(race=race)
        context = {
            'race': race,
            'race_results': race_results,
        }
    else:
        registrations = Registration.objects.filter(race=race)
        context = {
            'race': race,
            'registrations': registrations,
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

