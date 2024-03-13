from django.urls import path

from apps.user import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('info/', views.UserInfoView.as_view(), name='user_info'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/', views.TeacherListView.as_view(), name='teacher_list'),
    path('students/', views.StudentListView.as_view(), name='students_list'),
]
