from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from hotel_api import views as hotel_views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', hotel_views.register_view, name='register'),
    path('home/', hotel_views.home, name='home'),  
    path('hotel_api/', include('hotel_api.urls')),
    
]
