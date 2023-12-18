from django.contrib import admin
from django.urls import path, include
from hotel_api import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(), name='login'),  
    path('register/', views.register_view, name='register'),  
    path('home/', views.home, name='home'),  
    path('hotel_api/', include('hotel_api.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
]
