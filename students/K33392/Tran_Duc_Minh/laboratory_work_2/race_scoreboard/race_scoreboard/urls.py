from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from race import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('race/login/', views.login_view, name='login'),
    path('race/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('race/register/', views.register_user, name='register_user'),
    path('race/race_list/', views.race_list, name='race_list'),
    path('race/<int:race_id>/', views.view_race, name='view_race'),
    path('race/profile/', views.view_profile, name='profile'),
    path('race/race-results/', views.race_result_list, name='race_result_list'),
    path('race/race-results/<int:race_id>/', views.race_result_detail, name='race_result_detail'),
    path('race/unregister-race/<int:race_id>/', views.unregister_from_race, name='unregister_from_race'),
]
