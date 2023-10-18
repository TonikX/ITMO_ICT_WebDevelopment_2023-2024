from django.shortcuts import render
from intestines.models import Student, Teacher, Homework, AssignedHomework, StudentGrade, StudentPerformance, Post, SchoolGroup
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from intestines.forms import UserCreateForm


class HomeworkListView(ListView):
    model = Homework
    queryset = model.objects.all()
    template_name = 'list_view.html'


class AssignHomework(CreateView):
    model = AssignedHomework
    success_url = '/homework'
    fields = ['task']
    template_name = 'post_homework.html'

    def form_valid(self, form):
        work_object = get_object_or_404(Homework, id=self.kwargs['work_object'])
        form.instance.work_object = work_object
        form.instance.user = self.request.user
        return super().form_valid(form)


class GroupGrades(LoginRequiredMixin, ListView):
    model = StudentPerformance
    fields = ['student_object', 'discipline_object', 'grades']
    template_name = 'table.html'


def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/homework')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user[0])
            # print(user)
            return redirect('/homework')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
