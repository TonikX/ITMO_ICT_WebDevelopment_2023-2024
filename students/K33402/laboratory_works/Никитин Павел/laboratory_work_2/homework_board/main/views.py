from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from .models import Homework
from .forms import SubmittedWorkForm, SubmittedWork
from django.contrib.auth.decorators import login_required

def index(request):
    context = {"dataset": []}
    return render(request, 'main/index.html', context)

@login_required
def homeworks(request):
    if not request.user.is_authenticated: return redirect(request, 'login')

    form = SubmittedWorkForm()
    submitted_works = SubmittedWork.objects.filter(user=request.user)
    homeworks = Homework.objects.all()

    for item in homeworks:
        solution = False
        for item2 in submitted_works:
            if item2.homework == item:
                solution = item2
        item.solution = solution

    context = {
        "homeworks": homeworks,
        "user": request.user,
        "form": form
    }

    return render(request, 'main/homeworks.html', context)

@login_required
def add_solution(request, homework_id):
    if not request.user.is_authenticated: return redirect(request, 'login')

    if request.method == 'POST':
        form = SubmittedWorkForm(request.POST)
        if form.is_valid():
            submittedWork = form.save(commit=False)
            submittedWork.user = request.user
            submittedWork.homework = Homework.objects.get(pk=homework_id)
            submittedWork.save()

    return redirect('homeworks')

@login_required
def marks(request):
    if not request.user.is_authenticated: return redirect(request, 'login')
    submitted_works = SubmittedWork.objects.filter(user=request.user)
    marks_dict = {}
    for homework in submitted_works:
        if not homework.homework.subject in marks_dict and homework.grade:
           marks_dict[homework.homework.subject] = [homework.grade]
        elif homework.grade: marks_dict[homework.homework.subject].append(homework.grade)

    print(marks_dict)
    
    return render(request, 'main/marks.html', {"marks": marks_dict})

class HomeworksList(ListView):
    model = Homework
    template_name = 'main/homeworks.html'