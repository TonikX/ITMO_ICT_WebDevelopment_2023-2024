from django.urls import path
from .views import *


app_name = "lms_app"


urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/create/', UserCreate.as_view()),
    path('users/detail/<int:pk>', UserDetail.as_view()),
    path('users/update/<int:pk>', UserUpdate.as_view()),
    path('users/delete/<int:pk>', UserDelete.as_view()),

    path('courses/', CourseList.as_view()),
    path('courses/create/', CourseCreate.as_view()),
    path('courses/detail/<int:pk>', CourseDetail.as_view()),
    path('courses/update/<int:pk>', CourseUpdate.as_view()),
    path('courses/delete/<int:pk>', CourseDelete.as_view()),

    path('courses/students/', CoursesStudents.as_view()),
    path('courses/teachers/', CoursesTeachers.as_view()),
    path('courses/addstudent/', CourseStudentCreate.as_view()),
    path('courses/addteacher/', CourseTeacherCreate.as_view()),
    path('courses/removestudent/<int:pk>', CourseStudentDelete.as_view()),
    path('courses/removeteacher/<int:pk>', CourseTeacherDelete.as_view()),

    path('subjects/', SubjectList.as_view()),
    path('subjects/create/', SubjectCreate.as_view()),
    path('subjects/detail/<int:pk>', SubjectDetail.as_view()),
    path('subjects/update/<int:pk>', SubjectUpdate.as_view()),
    path('subjects/delete/<int:pk>', SubjectDelete.as_view()),

    path('lessons/', LessonList.as_view()),
    path('lessons/create/', LessonCreate.as_view()),
    path('lessons/detail/<int:pk>', LessonDetail.as_view()),
    path('lessons/update/<int:pk>', LessonUpdate.as_view()),
    path('lessons/delete/<int:pk>', LessonDelete.as_view()),

    path('applications/', ApplicationList.as_view()),
    path('applications/create/', ApplicationCreate.as_view()),
    path('applications/review/<int:pk>', ApplicationReview.as_view()),
    path('applications/detail/<int:pk>', ApplicationDetail.as_view()),
    path('applications/update/<int:pk>', ApplicationUpdate.as_view()),
    path('applications/delete/<int:pk>', ApplicationDelete.as_view()),
]