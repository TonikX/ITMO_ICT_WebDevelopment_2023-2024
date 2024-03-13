from django.urls import path

from apps.homework import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<int:pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('homeworks/<int:pk>/submit/', views.SubmissionCreateView.as_view(), name='submission_create'),
    path('my-submissions/', views.StudentSubmissionsView.as_view(), name='student_submissions'),
]
