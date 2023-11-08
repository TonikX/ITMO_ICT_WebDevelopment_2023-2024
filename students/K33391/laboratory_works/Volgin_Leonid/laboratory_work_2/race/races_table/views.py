from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from races_table.forms import LoginForm, RegistrationForm, RacerForm, UserUpdateForm, CommentForm, RaceConnectionForm

# Create your views here.
from races_table.models import Race, Comment, RaceConnection


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
    return render(request, 'dashboard.html', {'section': 'dashboard', 'has_racer': hasattr(request.user,'racer')})

@login_required
def register_racer(request):
    user = request.user
    print(user.has_racer)
    if hasattr(request.user, "racer"):
        return HttpResponse("You have already got a racer")
    else:
        if request.method == "POST":

            racer_form = RacerForm(request.POST)
            if  racer_form.is_valid():
                print(user)
                racer = racer_form.save(commit=False)
                racer.user = user
                racer.save()
                user.has_racer = True
                user.save()
                return redirect("dashboard")
        else:
            racer_form = RacerForm()

    return render(request,"register_racer.html", {"racer_form": racer_form})

@login_required
def redact_user(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('dashboard')
    else:
        user_form = UserUpdateForm(instance=request.user)
    return render(request, "redact_user.html", {"user_form": user_form},)

@login_required
def change_password(request):
    if request.method == "POST":
        password_form = PasswordChangeForm(request.user, request.POST)

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            return redirect("dashboard")
    else:
        password_form = PasswordChangeForm(request.user)
    return render(request,"change_password.html",{"password_form": password_form,})
@login_required()
def redact_racer(request):
    if request.method == "POST":
        racer_form = RacerForm(request.POST, instance=request.user.racer)
        if racer_form.is_valid():
            racer_form.save()
            return redirect("dashboard")
    else:
        if hasattr(request.user, "racer"):
            racer_form = RacerForm(instance=getattr(request.user, "racer", None))
        else:
            racer_form = None
    return render(request,"redact_racer.html",{"racer_form": racer_form,})

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
    return render(request,"race_comments.html",{"race": race, "comments": comments, "form": form})

@login_required
def races_list(request):
    races = Race.objects.all()
    race_connections = RaceConnection.objects.filter(racer=request.user.racer).values("race")
    #print(race_connections)
    racer_races = []
    for race_connection in race_connections:
        racer_races.append(race_connection['race'])
    #print(racer_races)
    return render(request, "races_list.html", {"races": races, "race_connections": racer_races})

@login_required
def delete_user(request):
    if request.method == "POST":
        request.user.delete()
        return redirect("home")
    return render(request, "delete_user.html")

@login_required
def create_race_connection(request,race_id):
    user = request.user
    if not(hasattr(user, "racer")):
        return HttpResponse("You have not got a racer")
    else:
            try:
                    race_connection = RaceConnection()
                    race = Race.objects.get(pk = race_id)
                    race_connection.race = race
                    race_connection.racer = user.racer
                    race_connection.save()
            except Exception as ex:
                    print(ex)
                    return HttpResponse('You have already registrated')
            return redirect("races_list")
    return redirect("races_list")
