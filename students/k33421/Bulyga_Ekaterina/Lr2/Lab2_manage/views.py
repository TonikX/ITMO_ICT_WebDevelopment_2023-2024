from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import SignUpForm


# Create your views here.
def participants(request):
    participants_dict = {}
    conference_list = Conference.objects.all()
    for conference in conference_list:
        performances = Performance.objects.filter(conference=conference)
        participants_list = []
        print(conference.user_registered)
        for performance in performances:
            participants_list.append(str(performance.user))
        participants_dict[conference.name] = participants_list
    print(participants_dict)
    return render(request, 'conferences/participants_table.html', {'participants': participants_dict})


def save_review(request):
    if request.method == 'POST':
        rating = request.POST['rating']
        conf_id = request.POST['conf_id']
        text = request.POST['reviewText']
        user = User.objects.get(username=request.user)
        conf = Conference.objects.get(id=conf_id)
        Review.objects.create(author=user, text=text, conference=conf, rating=rating)
    return redirect('/')


def my_registrations(request):
    conference_to_topic = {}
    user = User.objects.get(username=str(request.user))
    conf_user_registered = Conference.objects.filter(user_registered=user)
    for conference in conf_user_registered:
        performance = Performance.objects.filter(user=user, conference=conference)
        if performance:
            conference_to_topic[conference] = str(performance.get())
    return render(request, 'conferences/my_registrations.html', {'conference_to_topic': conference_to_topic})


def register_user(request):
    try:
        user = request.user
        if str(user) != 'AnonymousUser':
            return redirect('/')
    except:
        pass
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password)
            User.objects.create(username=username, name=name, email=email)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
        return render(request, 'conferences/register.html', {'form': form})

    return render(request, 'conferences/register.html', {'form': form})


def logout_user(request):
    logout(request)
    # list(messages.get_messages(request))
    return redirect('/')


def update_registration(request):
    if request.method == 'POST':
        topic = request.POST['topic']
        conf_id = request.POST['conf_id']
        user = User.objects.get(username=request.user)
        conf = Conference.objects.get(id=conf_id)
        Performance.objects.filter(conference=conf, user=user).update(topic=topic)
    return redirect('/my_registrations')


def save_registration(request):
    if request.method == 'POST':
        topic = request.POST['topic']
        conf_id = request.POST['conf_id']
        user = User.objects.get(username=request.user)
        conf = Conference.objects.get(id=conf_id)
        conf.user_registered.add(user)
        Performance.objects.create(conference=conf, user=user, topic=topic)
    return redirect('/')


def cancel_registration(request):
    print('cancel')
    if request.method == 'POST':
        conf_id = request.POST['conf_id']
        user = User.objects.get(username=request.user)
        conf = Conference.objects.get(id=conf_id)
        conf.user_registered.remove(user)
        Performance.objects.filter(conference=conf, user=user).delete()
    return redirect('/my_registrations')


def conferences(request):
    if request.method == 'POST':
        authenticate_user(request)
        return show_conferences(request)
    else:
        return show_conferences(request)


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Вы успешно авторизованы!")
    else:
        messages.success(request, "Неверная связка логин + пароль")


def show_conferences(request):
    conference_list = Conference.objects.all()
    topics = {}
    reviews = {}
    current_user_conf_registered = []
    conference_dates = {}
    for conference in conference_list:
        reviews_list = []
        topics[conference.id] = []
        conf_user_registered = User.objects.filter(conference__id=conference.id)
        for user_registered in conf_user_registered:
            if str(user_registered.username) == str(request.user):
                current_user_conf_registered.append(conference.id)
            performance = Performance.objects.filter(user=user_registered, conference=conference)
            if performance:
                topics.get(conference.id).append('\"' + str(performance.get()) + '\"')
        reviews_query = Review.objects.filter(conference=conference)

        for review in reviews_query:
            reviews_list.append(review)
        reviews[conference.id] = reviews_list
        conference_dates[conference.id] = conference.date
    print(reviews)
    return render(request, 'conferences/conferences.html',
                  {'conferences': conference_list, 'topics': topics, 'registered': current_user_conf_registered,
                   'reviews': reviews, 'conference_dates': conference_dates})
