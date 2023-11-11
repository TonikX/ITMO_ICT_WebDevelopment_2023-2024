from django.contrib.auth import views as auth_view
from django.urls import path

from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),  # для регистрации нового пользователя

    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login')
    # используется встроенное представление LoginView, которое предоставляет стандартную форму входа
]
