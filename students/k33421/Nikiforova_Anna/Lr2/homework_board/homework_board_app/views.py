from statistics import mean
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
import pandas as pd
from django.core.paginator import Paginator
from django.db.models import Avg
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm

ITEMS_PER_PAGE = 3


def index(request):
    if request.user.is_authenticated:
        return homepage(request)
    return login_request(request)


def register_request(request):  # регистрироваться могут ТОЛЬКО ученики, учитель - админ
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация успешна.")
            return redirect("homepage")
        messages.error(request, list(form.errors.items())[0][1])
    else:
        form = StudentRegistrationForm()
    return render(request, 'homework_board_app/login_related/register.html', {'register_form': form})


@login_required
def update_user_profile(request, user_id):
    if request.user.id == user_id:
        user = get_object_or_404(Student, id=user_id)
        if user and not user.is_superuser:
            if request.method == 'POST':
                form = UserProfileUpdateForm(request.POST, instance=user)
                print(form.errors)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Информация обновлена!")
                    return redirect("user_profile", user_id)
                messages.error(request, list(form.errors.items())[0][1])
            else:
                form = UserProfileUpdateForm(instance=user)
            return render(request, 'homework_board_app/student/update_user_profile.html',
                          {'register_form': form, 'user_id': user_id})
    return HttpResponseNotFound()


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Вы вошли в систему как {username}.")
                return redirect("homepage")
            else:
                messages.error(request, list(form.errors.items())[0][1])
        else:
            messages.error(request, list(form.errors.items())[0][1])
    form = AuthenticationForm()
    return render(request, "homework_board_app/login_related/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Вы успешно вышли из системы.")
    return redirect("index")


@login_required
def homepage(request):
    if request.user.is_superuser:
        classes = Class.objects.all()
        subjects = ', '.join(sorted([item.__str__() for item in Subject.objects.all()]))
        return render(request, 'homework_board_app/teacher/homepage.html',
                      context={'classes': classes, 'subjects': subjects})
    return student_homeworks(request)


def get_class_info_df(class_id):
    target_class = Class.objects.get(id=class_id)
    students = Student.objects.filter(student_class=target_class)
    subjects = Subject.objects.all()
    data = {'Student': []}
    for subject in subjects:
        data[subject.name] = []
    for student in students:
        data['Student'].append(student.fio)
        for subject in subjects:
            mean_score = HomeworkSubmission.objects.filter(
                student=student, homework__subject=subject
            ).aggregate(mean_score=Avg('grade'))['mean_score']
            data[subject.name].append(mean_score)
    df = pd.DataFrame(data).fillna('-')
    df.set_index('Student', inplace=True)
    df.insert(0, 'ФИО', df.index)
    df = df.rename(columns={df.columns[0]: 'ФИО\\Предмет'})
    return df


@login_required
def class_info(request, class_id):
    # Only teacher has access to classes
    if request.user.is_superuser:
        class_ = get_object_or_404(Class, id=class_id)
        class_name = class_.name
        df = get_class_info_df(class_id)
        pandas_table = df.to_html(index=False,
                                  classes='***', justify='left').replace("dataframe ***", "table mb-0")
        return render(request, 'homework_board_app/teacher/class_info.html', context={'class_name': class_name,
                                                                                      'pandas_table': pandas_table})
    else:
        return HttpResponseNotFound()


@login_required
def user_profile(request, user_id):
    # Ensure that the user is trying to access their own profile
    if request.user.id == user_id:
        user = get_object_or_404(Student, id=user_id)
        context = {'user': user}
        if user.is_superuser:
            return render(request, 'homework_board_app/teacher/user_profile.html', context)
        return render(request, 'homework_board_app/student/user_profile.html', context)
    else:
        return HttpResponseNotFound()


@login_required
def student_homeworks(request):
    global ITEMS_PER_PAGE

    student = request.user
    class_id = student.student_class

    homeworks = Homework.objects.filter(class_it_is_assigned_to=class_id)

    subject_filter = request.GET.get('subject')
    scores = []

    if subject_filter and subject_filter != 'any':
        homeworks = homeworks.filter(subject__name=subject_filter)

    for homework in homeworks:
        subs = HomeworkSubmission.objects.filter(homework=homework, student=student).first()
        if subs and subs.grade:
            scores.append(subs.grade)
    avg_score = mean(scores) if len(scores) else 0

    done_filter = request.GET.get('notdone')

    if done_filter == 'notdone':
        homeworks = homeworks.exclude(students_who_submitted_it=student)

    search_query = request.GET.get('q')

    if search_query:
        homeworks = homeworks.filter(
            Q(name__icontains=search_query) |
            Q(assignment_text__icontains=search_query)
        )

    submissions = HomeworkSubmission.objects.filter(student=student)
    homework_displays = []

    for homework in homeworks:
        submission = submissions.filter(homework=homework).first()
        homework_display = HomeworkDisplay(homework, submission)
        homework_displays.append(homework_display)

    subject_list = Subject.objects.all()
    per_page = ITEMS_PER_PAGE

    paginator = Paginator(homework_displays, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    page_obj.subject_filter = subject_filter
    page_obj.done_filter = done_filter
    page_obj.search_query = search_query

    return render(request, 'homework_board_app/student/homepage.html',
                  {'page_obj': page_obj, 'subject_list': subject_list, 'avg_score': avg_score})


@login_required
def homework_detail(request, pk):
    homework = get_object_or_404(Homework, pk=pk)
    class_id = request.user.student_class
    if homework.class_it_is_assigned_to != class_id:  # нельзя посмотреть дз не своего класса
        return HttpResponseNotFound()

    submission = HomeworkSubmission.objects.filter(homework=homework).filter(student=request.user).first()
    homework_display = HomeworkDisplay(homework, submission)

    if submission:
        # If a submission exists, update it
        initial_data = {'submission_text': submission.submission_text}
        if request.method == 'POST':
            form = HomeworkSubmissionForm(request.POST, instance=submission, initial=initial_data)
            if form.is_valid():
                form.save()
                messages.success(request, "Ответ записан!")
                return redirect('student_homeworks')
        else:
            # Pass existing submission text as initial data to the form
            form = HomeworkSubmissionForm(instance=submission, initial=initial_data)
    else:
        if request.method == 'POST':
            form = HomeworkSubmissionForm(request.POST)
            if form.is_valid():
                new_submission = form.save(commit=False)
                new_submission.student = request.user
                new_submission.homework = homework
                new_submission.save()
                messages.success(request, "Ответ записан!")
                return redirect('student_homeworks')
        else:
            form = HomeworkSubmissionForm()

    return render(request, 'homework_board_app/student/homework_detail.html',
                  {'homework_display': homework_display, 'form': form})


@login_required
def add_homework(request):
    if not request.user.is_superuser:
        return HttpResponseNotFound()

    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            homework = form.save()
            messages.success(request, "Задание создано!")
            return redirect('teacher_homework_detail', pk=homework.pk)
    else:
        form = HomeworkForm()

    return render(request, 'homework_board_app/teacher/add_homework.html', {'form': form})


@login_required
def update_homework(request, pk):
    homework = get_object_or_404(Homework, pk=pk)

    if not request.user.is_superuser:
        return HttpResponseNotFound()

    if request.method == 'POST':
        form = HomeworkForm(request.POST, instance=homework)
        if form.is_valid():
            form.save()
            messages.success(request, "Задание обновлено!")
            return redirect('all_homeworks')
    else:
        form = HomeworkForm(instance=homework)

    return render(request, 'homework_board_app/teacher/update_homework.html', {'form': form, 'homework': homework,
                                                                               'subjects': Subject.objects.all(),
                                                                               'classes': Class.objects.filter(
                                                                                   date_to__gte=date.today())})


@login_required
def delete_homework(request, pk):
    homework = get_object_or_404(Homework, pk=pk)
    if not request.user.is_superuser:
        return HttpResponseNotFound()
    if request.method == 'POST':
        homework.delete()
    messages.success(request, "Задание удалено!")
    return redirect('all_homeworks')


@login_required
def teacher_homework_detail(request, pk):
    if not request.user.is_superuser:
        return HttpResponseNotFound()
    homework = get_object_or_404(Homework, pk=pk)
    submissions = HomeworkSubmission.objects.filter(homework=homework).all()
    homework.submitted_num = len(submissions)
    homework.not_checked_num = len(submissions.filter(grade=None))
    return render(request, 'homework_board_app/teacher/homework_detail.html', {'homework': homework})


@login_required
def all_homeworks(request):
    global ITEMS_PER_PAGE

    if not request.user.is_superuser:
        return HttpResponseNotFound()

    homeworks = Homework.objects.all()

    subject_filter = request.GET.get('subject')
    if subject_filter and subject_filter != 'any':
        homeworks = homeworks.filter(subject__name=subject_filter)

    class_filter = request.GET.get('class')
    if class_filter and class_filter != 'any':
        homeworks = homeworks.filter(class_it_is_assigned_to__name=class_filter)

    search_query = request.GET.get('q')
    if search_query:
        homeworks = homeworks.filter(
            Q(name__icontains=search_query) |
            Q(assignment_text__icontains=search_query)
        )

    done_filter = request.GET.get('notdone')
    submissions = HomeworkSubmission.objects.all()

    homeworks_to_show = []
    for i, homework in enumerate(homeworks):
        subs = submissions.filter(homework=homework).all()
        homework.submitted_num = len(subs)
        homework.not_checked_num = len(subs.filter(grade=None))
        if done_filter == 'notdone' and homework.not_checked_num or done_filter != 'notdone':
            homeworks_to_show.append(homework)

    subject_list = Subject.objects.all()
    class_list = Class.objects.all()

    per_page = ITEMS_PER_PAGE
    paginator = Paginator(homeworks_to_show, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    page_obj.subject_filter = subject_filter
    page_obj.class_filter = class_filter
    page_obj.search_query = search_query
    page_obj.done_filter = done_filter

    return render(request, 'homework_board_app/teacher/all_homeworks.html',
                  {'page_obj': page_obj, 'subject_list': subject_list, 'class_list': class_list})


@login_required
def submitted_homeworks(request, pk):
    global ITEMS_PER_PAGE

    if not request.user.is_superuser:
        return HttpResponseNotFound()

    homework = get_object_or_404(Homework, pk=pk)
    submissions = HomeworkSubmission.objects.filter(homework=homework)

    search_text = request.GET.get('search_text', '')
    if search_text:
        submissions = submissions.filter(
            Q(submission_text__icontains=search_text) | Q(student__fio__icontains=search_text))

    done_filter = request.GET.get('notdone')
    if done_filter == 'notdone':
        submissions = submissions.filter(grade__isnull=True)

    per_page = ITEMS_PER_PAGE
    paginator = Paginator(submissions, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    page_obj.done_filter = done_filter
    page_obj.search_query = search_text

    return render(request, 'homework_board_app/teacher/submitted_homeworks.html', {
        'page_obj': page_obj,
        'homework': homework,
        'search_text': search_text
    })


@login_required
def submitted_homework_detail(request, pk):
    if not request.user.is_superuser:
        return HttpResponseNotFound()
    submission = get_object_or_404(HomeworkSubmission, pk=pk)
    if request.method == 'POST':
        grade = request.POST.get('grade')
        if grade:
            submission.grade = grade
            submission.save()
            messages.success(request, 'Работа отправлена!')
            return submitted_homeworks(request, pk=submission.homework.id)
    return render(request, 'homework_board_app/teacher/submitted_homework_detail.html', {'submission': submission})
