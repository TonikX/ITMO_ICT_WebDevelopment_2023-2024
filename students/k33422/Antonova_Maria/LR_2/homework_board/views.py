from django.shortcuts import render, redirect  # для перенаправления на др стр
from django.contrib.auth.decorators import \
    login_required  # требует, чтобы пользователь был аутентифицирован, прежде чем иметь доступ к представлению
from .decorators import staff_required  # является ли пользователь сотрудником
from .models import Homework, Answer, JournalRecord
from django.contrib.auth.models import User
from .forms import AnswerForm


@login_required()
def student_homework(request):  # представление, отображающее домашние задания для студентов
    journals = JournalRecord.objects.filter(student=request.user)
    homeworks = Homework.objects.all()

    if request.method == 'POST':
        form = AnswerForm(request.POST)  # создается и проверяется форма
        if form.is_valid():
            instance = form.save(
                commit=False)  # Если форма проходит, создается новый экземпляр ответа (instance), связанный с текущим пользователем (request.user)
            instance.student = request.user
            instance.save()  # сохраняется и происходит перенаправление на страницу student_homework
            return redirect('student_homework')
    else:
        form = AnswerForm()  # выводится пустая форма AnswerForm в шаблоне 'student_homework.html' с переданными данными о домашних заданиях (homework) и формой (form)
    return render(request, 'student_homework.html', {'journals': journals, 'homeworks': homeworks, 'form': form})


@staff_required()
def teacher_answers(request):
    journals = JournalRecord.objects.all()
    return render(request, 'teacher_answers.html', {
        'journals': journals})  # данные передаются в  teacher_answers.html для отображения списка студентов и их оценок
    # берет указанный HTML, заполняет его данными из словаря и возвращает это в виде HTTP-ответа
