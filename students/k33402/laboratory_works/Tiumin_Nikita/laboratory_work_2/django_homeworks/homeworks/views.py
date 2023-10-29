from homeworks.forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from functools import wraps
from django.db.models.functions import ExtractDay

from homeworks.models import Subject, Homework, HomeworkSubmission, User, HomeworkGrade


def anonymous_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return _wrapped_view


# AUTH
@anonymous_required
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_teacher = False
            new_user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})


@anonymous_required
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)

    return redirect('login')
#  System


def handler404(request, exception):
    return render(request, 'system/404.html', status=404)


#  Student
@login_required
def home(request):
    subjects = Subject.objects.all()

    return render(request, 'home.html', {
        'subjects': subjects,
    })


@login_required
def index_homeworks(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    homeworks = Homework.objects.filter(subject_id=subject_id).all()

    return render(request, 'student/homeworks.index.html', {
        'subject': subject.name,
        'homeworks': homeworks,
    })


@login_required
def show_homeworks(request, hw_id):
    homework = Homework.objects.get(pk=hw_id)

    try:
        submission = HomeworkSubmission.objects.filter(student_id=request.user.id, homework_id=hw_id).get()
    except ObjectDoesNotExist:
        submission = None

    return render(request, 'student/homeworks.show.html', {
        'homework': homework,
        'submission': submission.submission_text if submission else None,
        'is_submitted': submission is not None,
    })


@login_required
def store_submission(request):
    data = request.POST

    submission = HomeworkSubmission(
        submission_text=data['submission_text'],
        homework_id=data['homework_id'],
        student_id=request.user.id,
        submission_date=timezone.now()
    )

    submission.save()

    return redirect(request.META.get('HTTP_REFERER'))


#  Teacher
@login_required
def journal(request):
    if not request.user.is_teacher:
        return redirect('home')

    students = User.objects.filter(is_teacher=False).all()
    subjects = Subject.objects.all()

    for subject in subjects:
        subject.homeworks = subject.homework_set.all()

    for student in students:
        student.grades = {}
        for subject in subjects:
            grades = []
            for homework in subject.homeworks:
                try:
                    submission = HomeworkSubmission.objects.get(student_id=student.id, homework_id=homework.id)

                    try:
                        grades.append({'id': submission.id, 'value': submission.homeworkgrade.grade})
                    except ObjectDoesNotExist:
                        grades.append({'id': submission.id, 'value': 'Не оценено'})
                except ObjectDoesNotExist:
                    grades.append({'id': None, 'value': 'Не сдано'})
            student.grades[subject.id] = grades

    return render(request, 'teacher/journal.html', {
        'students': students,
        'subjects': subjects,
    })


@login_required
def show_submission(request, s_id):
    if not request.user.is_teacher:
        return redirect('home')

    try:
        submission = HomeworkSubmission.objects.get(pk=s_id)
    except ObjectDoesNotExist:
        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'teacher/submissions.show.html', {
        'submission': submission,
    })


@login_required
def store_grade(request):
    if not request.user.is_teacher:
        return redirect('home')

    data = request.POST

    submission = HomeworkSubmission.objects.get(pk=data['submission_id'])

    if submission.submission_date > submission.homework.deadline:
        from datetime import datetime

        d1 = datetime.strptime(str(submission.submission_date), "%Y-%m-%d")
        d2 = datetime.strptime(str(submission.homework.deadline), "%Y-%m-%d")
        days_overdue = (d1 - d2).days

        penalty = submission.homework.penalties * days_overdue

    else:
        penalty = 0

    grade = round(int(data['grade']) - penalty)

    homework_grade = HomeworkGrade(
        homework_submission_id=data['submission_id'],
        grade=grade,
        graded_by=request.user,
        graded_date=timezone.now(),
    )

    homework_grade.save()

    return redirect(request.META.get('HTTP_REFERER'))
