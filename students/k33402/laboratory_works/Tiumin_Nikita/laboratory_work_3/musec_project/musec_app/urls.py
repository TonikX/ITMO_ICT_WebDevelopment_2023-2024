from django.urls import path
from musec_app.views import auth

urlpatterns = [
    #  Auth
    path('register', auth.register, name='auth.register'),
    path('login', auth.login, name='auth.login'),
    path('logout', auth.logout, name='auth.logout'),
]
