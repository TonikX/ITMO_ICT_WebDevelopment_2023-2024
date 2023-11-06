from django.shortcuts import render, redirect
from .models import Homework, User, Grade, Submission
from django.contrib.auth.forms import UserCreationForm, authenticate
from django.contrib.auth import login, logout
from django.contrib import messages

def view_journal(request):
    homework_list = Homework.objects.all()
    submissions = Submission.objects.all()
    grades = Grade.objects.all()

    context = {
        'homework_list': homework_list,
        'submissions': submissions,
        'grades': grades,
    }

    return render(request, 'journal.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if username == 'Teacher' and password == 'Uchis5252':
            return redirect('/admin/')
        if user is not None:
            login(request, user)
            return redirect('/journal/')  # Перенаправление на вашу основную страницу после входа
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login/')


