from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import HomePage, HomeworkPage, AddHomework, EditHomework, DeleteHomework, SubmitHomework, GradeHomework, StudentGrades, GradeStudentHomework
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', login_required(HomePage.as_view()), name='home'),
    path('homework/<int:pk>', login_required(HomeworkPage.as_view()), name='homework-page'),
    path('add_homework/', login_required(AddHomework.as_view()), name='new-homework'),
    path('homework/edit/<int:pk>', login_required(EditHomework.as_view()), name='edit-homework'),
    path('homework/<int:pk>/delete/', login_required(DeleteHomework.as_view()), name='delete-homework'),
    path('homework/<int:pk>/submit/', login_required(SubmitHomework.as_view()), name='submit-homework'),
    path('grade_homework/', login_required(GradeHomework.as_view()), name='grade-homework'),
    path('student_grades/<int:student_id>/', login_required(StudentGrades.as_view()), name='student-grades'),
    path('student_homework/<int:student_id>/<int:submission_id>/', login_required(GradeStudentHomework.as_view()), name='grade-student-homework'),

]
