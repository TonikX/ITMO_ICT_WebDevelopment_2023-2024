from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from races_app.forms import LoginForm

# Create your views here.
#from races_app.forms import RedactedUserCreationForm, RedactedAuthenticationForm

# def RegistrationView(request):
#     if request.method == 'POST':
#         form = RedactedUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = RedactedUserCreationForm()
#     return render(request, 'register.html', {'form': form})
#
#
# def LoginView(request):
#     if request.method == 'POST':
#         form = RedactedAuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('index')
#     else:
#         form = RedactedAuthenticationForm()
#     return render(request, 'login.html', {'form': form})

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



@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'section': 'dashboard'})