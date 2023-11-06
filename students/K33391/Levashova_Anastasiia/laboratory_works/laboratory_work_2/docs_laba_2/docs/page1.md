# Реализация приложения

## models.py
    from django.contrib.auth.models import User
    from django.db import models


    class RacerCar(models.Model):
        state_number = models.CharField(max_length=15, null=False)
        brand = models.CharField(max_length=30, null=False)
        model = models.CharField(max_length=30, null=False)
        color = models.CharField(max_length=30, null=True)
    
        def __str__(self):
            return f"{self.state_number} {self.brand} {self.model}"


    class Racer(models.Model):
        first_name = models.CharField(max_length=100, null=False)
        last_name = models.CharField(max_length=100, null=False)
        team_name = models.CharField(max_length=100, null=False)
        participant_description = models.TextField(max_length=500, default='Нет описания')
        experience = models.PositiveIntegerField(null=False)
        user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
        car = models.OneToOneField(RacerCar, on_delete=models.CASCADE, null=False)
    
        def __str__(self):
            return f"{self.first_name} {self.last_name} {self.team_name}"
    
    
    class Race(models.Model):
        title = models.CharField(max_length=100, null=False)
        date = models.DateTimeField(null=False)
        location = models.CharField(max_length=100, null=False)
        description = models.CharField(max_length=500, default='Нет описания')
    
        def __str__(self):
            return f"Гонка: {self.title}, {self.date}"
    
    
    class RaceResult(models.Model):
        race = models.ForeignKey(Race, on_delete=models.CASCADE, null=False)
        racer = models.ForeignKey(Racer, on_delete=models.CASCADE, null=False)
        position = models.PositiveIntegerField(null=False)
        lap_time = models.DurationField(null=False)
        top_speed = models.FloatField(null=False)
    
        def __str__(self):
            return f"Результат для {self.racer.last_name} в гонке {self.race.title}, {self.race.date}"
    
    
    class Registration(models.Model):
        racer = models.ForeignKey(Racer, on_delete=models.DO_NOTHING, null=False)
        race = models.ForeignKey(Race, on_delete=models.DO_NOTHING, null=False)
        registration_date = models.DateTimeField(auto_now_add=True, null=False)
    
        def __str__(self):
            return f"{self.race.title}"
    
    
    class Comment(models.Model):
        COMMENT_TYPES = (
            ('Cooperation', 'Question about cooperation'),
            ('Race', 'Question about the race'),
            ('Other', 'Other'),
        )
    
        race = models.ForeignKey(Race, on_delete=models.CASCADE, null=False)
        commentator = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
        comment_date = models.DateTimeField(auto_now_add=True, null=False)
        comment_text = models.TextField(null=False)
        comment_type = models.CharField(max_length=20, choices=COMMENT_TYPES, null=False)
        rating = models.PositiveIntegerField(null=False)
    
        def __str__(self):
            return f"Комментарий от {self.commentator.username} для {self.race.location}"

## forms.py
    
    from django import forms
    from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
    from django.contrib.auth.models import User
    from racing_app.models import Racer, RacerCar, Comment
    
    
    class UserRegistrationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['username', 'password1', 'password2']
    
    
    class UserLoginForm(AuthenticationForm):
        class Meta:
            fields = ['username', 'password']
    
    
    class RacerProfileForm(forms.ModelForm):
        class Meta:
            model = Racer
            fields = ['first_name', 'last_name', 'team_name', 'participant_description', 'experience']
            labels = {
                "first_name": "Имя",
                "last_name": "Фамилия",
                "team_name": "Название команды",
                "participant_description": "Описание",
                "experience": "Опыт (лет)",
            }
    
    
    class RacerCarForm(forms.ModelForm):
        class Meta:
            model = RacerCar
            fields = ['state_number', 'brand', 'model', 'color']
            labels = {
                "state_number": "Номер авто",
                "brand": "Марка авто",
                "model": "Модель авто",
                "color": "Цвет авто",
            }
    
    
    class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ['comment_text', 'comment_type', 'rating']
            labels = {
                "comment_text": "Текст",
                "comment_type": "Тип",
                "rating": "Рейтинг",
            }

## urls.py

    from django.urls import path
    from .views import home, register_user, login_user, race_list, race_detail, registration_list, DeleteRegistration, \
        racer_profile, race_registration, add_comment, custom_logout
    
    urlpatterns = [
        path('', home, name='home'),
        path('register/', register_user, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', custom_logout, name='logout'),
        path('races/', race_list, name='race_list'),
        path('races/race/<int:race_id>/', race_detail, name='race_detail'),
        path('registrations/', registration_list, name='registration_list'),
        path('registrations/registration/delete/<int:pk>', DeleteRegistration.as_view()),
        path('racer_profile/', racer_profile, name='racer_profile'),
        path('race_registration/', race_registration, name='race_registration'),
        path('races/race/add_comment/<int:race_id>/', add_comment, name='add_comment'),
    ]

## views.py

    from django.utils import timezone
    from django.contrib.auth import login, authenticate
    from django.shortcuts import render, redirect, get_object_or_404
    from django.views.generic import DeleteView
    from django.contrib.auth import logout
    from .forms import UserRegistrationForm, UserLoginForm, RacerProfileForm, RacerCarForm, CommentForm
    from django.contrib import messages
    from .models import Race, RaceResult, Registration, Racer, Comment
    
    
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
            Racer.objects.get(user=user)
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

