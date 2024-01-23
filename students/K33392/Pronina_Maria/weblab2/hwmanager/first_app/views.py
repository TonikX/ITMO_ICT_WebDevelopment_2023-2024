from django.shortcuts import render
from .forms import TeacherForm, SolutionForm, StudentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from .models import *


def teacher_form_view(request):
    context = {}
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        group = Group.objects.get(name='Teachers')
        user.groups.add(group)
        user.is_staff = True
        user.set_password(form.cleaned_data["password"])
        user.save()
        return HttpResponseRedirect('../teacher/success')
    context['form'] = form
    return render(request, "new_user.html", context)


def teacher_add_success_view(request):
    return render(request, "success_page.html")


def student_form_view(request):
    context = {}
    form = StudentForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        group = Group.objects.get(name='Students')
        user.groups.add(group)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return HttpResponseRedirect('../student/success')
    context['form'] = form
    return render(request, "new_student.html", context)


def student_add_success_view(request):
    return render(request, "student_success_page.html")


def homeworks_view(request):
    hws = dict()
    hws["dataset"] = Homework.objects.all()
    return render(request, "show_all_hws.html", hws)


def solution_form_view(request, hw_id):
    context = {}
    form = SolutionForm(request.POST or None)
    homework = Homework.objects.get(pk=hw_id)

    if form.is_valid():
        solution = form.save(commit=False)
        solution.homework = homework
        solution.save()
        return HttpResponseRedirect('../../solution/success')

    context['form'] = form
    context['homework'] = homework
    return render(request, "new_solution.html", context)


def solution_add_success_view(request):
    return render(request, "solution_success_page.html")


def register_view(request):
    subjects = Subject.objects.all()
    register = []
    students = User.objects.filter(groups__name='Students')
    for student in students:
        student_marks = []
        for subject in subjects:
            solutions = Solution.objects.filter(student=student, homework__subject=subject)
            subj_marks = []
            for solution in solutions:
                if solution.mark is not None:
                    subj_marks.append(solution.mark)
            student_marks.append((subject, subj_marks))
        register.append((student, student_marks))

    context = {
        'student_data': register,
    }

    return render(request, 'show_marks.html', context)
