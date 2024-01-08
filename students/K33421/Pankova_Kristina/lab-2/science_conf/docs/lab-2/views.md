## Views.py

```python
import time

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import Http404, request
from django.template import context

from .models import *
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import UserRegisterForm, AttendanceRegisterForm, CommentsRegisterForm, LecturesRegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect


def list_guests_view(request):
    context = {}
    context["dataset"] = ConferenceGuest.objects.all()
    return render(request, "list_guests.html", context)


def guest_detail_view(request, guest_id):
    try:
        p = ConferenceGuest.objects.get(pk=guest_id)
    except ConferenceGuest.DoesNotExist:
        raise Http404("The guest  does not exist")
    return render(request, 'guest_detail.html', {'guest': p})

def conference_detail_view(request, conference_id):
    try:
        p = Conference.objects.get(pk=conference_id)
    except Conference.DoesNotExist:
        raise Http404("The conference does not exist")
    return render(request, 'conference_detail.html', {'conference': p})


class Conference_guests_list_view(ListView):
    template_name = 'list_conferences_by_guest.html'
    model = Conference
    def get_queryset(self):
        self.queryset = self.model.objects.all()
        guest = self.request.GET.get('guest')
        if guest:
            try:
                guest = int(guest)
                queryset = self.queryset.filter(guests=guest)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset
        return self.queryset

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


class Conference_my_list_view(ListView):
    template_name = 'list_conferences_by_guest.html'
    model = Conference
    def get(self, request):
        guest = request.user.pk
        self.queryset = self.model.objects.all()
       # guest = self.request.GET.get('guest')
        try:
            guest = int(guest)
            self.queryset = self.queryset.filter(guests__pk=guest)

        except (ValueError, TypeError):
            self.queryset = self.model.objects.none()

        context = {'object_list': self.queryset}
        return render(request, self.template_name, context)

class UserRegistration(ListView):
    template_path = 'guest_registration.html'
    form_class = UserRegisterForm
    success_url = '/guests/all/'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_path, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'User created successfully! You are now logged in.')
        context = {'form': form}
        return render(request, self.template_path, context)

class AttendanceRegistration(ListView):
    template_path = 'attendance_registration.html'
    form_class = AttendanceRegisterForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        form.instance.form_author = request.user
        context = {'form': form}
        return render(request, self.template_path, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.form_author = request.user
            form.save()
            messages.success(request, 'You were successfully registered!')
        context = {'form': form}

        return render(request, self.template_path, context)

class AttendanceMyRegistration(ListView):
    template_name = 'list_my_attendance_forms.html'
    model = ConferenceAttendance

    def get(self, request):
        guest = request.user.pk
        self.queryset = self.model.objects.all()
        try:
            guest = int(guest)
            self.queryset = self.queryset.filter(form_author__pk=guest)

        except (ValueError, TypeError):
            self.queryset = self.model.objects.none()

        context = {'object_list': self.queryset}
        return render(request, self.template_name, context)

class LectureRegistration(ListView):
    template_name = 'attendance_registration.html'
    model = ConferenceAttendance
    form_class = LecturesRegisterForm

    def get(self, request, conference_id, *args, **kwargs):
        form = self.form_class()
        form.fields['lecturer'].queryset = ConferenceAttendance.objects.filter(role='SP', conference=conference_id, form_author=request.user)

     #   form.conference = request.user
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, conference_id, *args, **kwargs):
        form = self.form_class(request.POST)
        form.fields['lecturer'].queryset = ConferenceAttendance.objects.filter(role='SP', conference=conference_id, form_author=request.user)
        form.instance.conference = Conference.objects.get(id=conference_id)

        if form.is_valid():
            form.instance.conference = Conference.objects.get(id=conference_id)
            form.save()
            messages.success(request, 'The lecture was successfully registered!')
        context = {'form': form}

        return render(request, self.template_name, context)


class CommentsRegistration(ListView):
    template_path = 'comments_registration.html'
    form_class = CommentsRegisterForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        form.fields['conference'].queryset = Conference.objects.filter(guests=request.user)
        form.form_author = request.user
        context = {'form': form}
        return render(request, self.template_path, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.fields['conference'].queryset = Conference.objects.filter(guests=request.user)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.sent_at = time.time()

            form.save()
            messages.success(request, 'Your comment was successfully posted!')
        context = {'form': form}

        return render(request, self.template_path, context)



class AttendanceDeleteView(DeleteView):
  model = ConferenceAttendance
  success_url = '/attendance/my/'
  template_name = 'attendance_delete.html'


class AttendanceUpdateView(UpdateView):
  model = ConferenceAttendance
  fields = ['conference', 'guest', 'role']
  success_url = '/attendance/my/'
  template_name = 'attendance_edit.html'

def lecture_by_conference_view(request, conference_id):
    try:
        p = ConferenceLectures.objects.filter(conference=conference_id)
    except ConferenceLectures.DoesNotExist:
        raise Http404("The lecture  does not exist")
    return render(request, 'list_lectures_by_conference.html', {'object_list': p})

def comments_by_conference_view(request, conference_id):
    try:
        p = ConferenceComments.objects.filter(conference=conference_id)
    except ConferenceComments.DoesNotExist:
        raise Http404("The comments do not exist")
    return render(request, 'list_comments_by_conference.html', {'object_list': p})


class LectureDeleteView(DeleteView):
  model = ConferenceLectures
  success_url = '/conferences/my/'
  template_name = 'lecture_delete.html'


class LectureUpdateView(UpdateView):
  model = ConferenceLectures
  fields = ['lecturer', 'conference', 'name', 'given_at', 'is_recommended']
  success_url = '/conferences/my/'
  template_name = 'lecture_edit.html'

class CommentDeleteView(DeleteView):
  model = ConferenceComments
  success_url = '/conferences/my/'
  template_name = 'lecture_delete.html'


class CommentUpdateView(UpdateView):
  model = ConferenceComments
  fields = ['text', 'type']
  success_url = '/conferences/my/'
  template_name = 'lecture_edit.html'

```