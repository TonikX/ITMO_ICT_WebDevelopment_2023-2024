from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from races_table.forms import LoginForm, RegistrationForm


# Create your views here.

def logout_view(request):
    logout(request)
    return render(request, 'logged_out.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect("login")
    else:
        form = RegistrationForm()

    return render(request, "register.html", {"user_form": form})

def home(request):
    return render(request, "home.html")

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'section': 'dashboard'})

