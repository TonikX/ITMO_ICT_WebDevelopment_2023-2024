from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout
# Create your views here.
def sign_up(request):
    if request.method == 'POST': #cоздается экземпляр формы SignUpForm с данными, полученными из POST-запроса
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_homework')  # перенаправление пользователя на другую страницу после успешной регистрации
    else:
        form = SignUpForm() #создание пустой формы
    return render(request, 'sign_up.html', {'form': form}) # Отображение страницы регистрации с использованием HTML-шаблона 'sign_up.html' и передача формы для использования в шаблоне


def logout_view(request):
    logout(request)
    return redirect('login')