# urls.py
    from django.urls import path, include
    from rest_framework.authtoken.views import obtain_auth_token
    from .views import *
    from .models import *
    from .serializers import *

## Patterns    
    urlpatterns = [
    
        path('teacher/all/', UniversalListView.as_view(model=Teacher, serializer_class=TeacherSerializer)),
        path('teacher/<int:pk>/', UniversalRetrieveView.as_view(model=Teacher, serializer_class=TeacherSerializer)),
        path('teacher/create/', UniversalCreateView.as_view(model=Teacher, serializer_class=TeacherSerializer)),
        path('teacher/update/<int:pk>/', UniversalUpdateView.as_view(model=Teacher, serializer_class=TeacherSerializer)),
        path('teacher/delete/<int:pk>/', UniversalDeleteView.as_view(model=Teacher, serializer_class=TeacherSerializer)),
    
        path('group/all/', UniversalListView.as_view(model=Group, serializer_class=GroupSerializer)),
        path('group/<int:pk>/', UniversalRetrieveView.as_view(model=Group, serializer_class=GroupSerializer)),
        path('group/create/', UniversalCreateView.as_view(model=Group, serializer_class=GroupSerializer)),
        path('group/update/<int:pk>/', UniversalUpdateView.as_view(model=Group, serializer_class=GroupSerializer)),
        path('group/delete/<int:pk>/', UniversalDeleteView.as_view(model=Group, serializer_class=GroupSerializer)),
    
        path('student/all/', UniversalListView.as_view(model=Student, serializer_class=StudentSerializer)),
        path('student/<int:pk>/', UniversalRetrieveView.as_view(model=Student, serializer_class=StudentSerializer)),
        path('student/create/', UniversalCreateView.as_view(model=Student, serializer_class=CreateStudentSerializer)),
        path('student/update/<int:pk>/', UniversalUpdateView.as_view(model=Student, serializer_class=StudentSerializer)),
        path('student/delete/<int:pk>/', UniversalDeleteView.as_view(model=Student, serializer_class=StudentSerializer)),
    
        path('lesson/all/', UniversalListView.as_view(model=Lesson, serializer_class=LessonSerializer)),
        path('lesson/<int:pk>/', UniversalRetrieveView.as_view(model=Lesson, serializer_class=LessonSerializer)),
        path('lesson/create/', UniversalCreateView.as_view(model=Lesson, serializer_class=LessonSerializer)),
        path('lesson/update/<int:pk>/', UniversalUpdateView.as_view(model=Lesson, serializer_class=LessonSerializer)),
        path('lesson/delete/<int:pk>/', UniversalDeleteView.as_view(model=Lesson, serializer_class=LessonSerializer)),
    
        path('teach/all/', UniversalListView.as_view(model=TeachProcess, serializer_class=TeachProcessSerializer)),
        path('teach/<int:pk>/', UniversalRetrieveView.as_view(model=TeachProcess, serializer_class=TeachProcessSerializer)),
        path('teach/create/', UniversalCreateView.as_view(model=TeachProcess, serializer_class=TeachProcessSerializer)),
        path('teach/update/<int:pk>/',
             UniversalUpdateView.as_view(model=TeachProcess, serializer_class=TeachProcessSerializer)),
        path('teach/delete/<int:pk>/',
             UniversalDeleteView.as_view(model=TeachProcess, serializer_class=TeachProcessSerializer)),
    
        path('subject/all/', UniversalListView.as_view(model=Subject, serializer_class=SubjectSerializer)),
        path('subject/<int:pk>/', UniversalRetrieveView.as_view(model=Subject, serializer_class=SubjectSerializer)),
        path('subject/create/', UniversalCreateView.as_view(model=Subject, serializer_class=SubjectSerializer)),
        path('subject/update/<int:pk>/', UniversalUpdateView.as_view(model=Subject, serializer_class=SubjectSerializer)),
        path('subject/delete/<int:pk>/', UniversalDeleteView.as_view(model=Subject, serializer_class=SubjectSerializer)),
    
        path('grade/all/', UniversalListView.as_view(model=Grade, serializer_class=GradeSerializer)),
        path('grade/<int:pk>/', UniversalRetrieveView.as_view(model=Grade, serializer_class=GradeSerializer)),
        path('grade/create/', UniversalCreateView.as_view(model=Grade, serializer_class=GradeSerializer)),
        path('grade/update/<int:pk>/', UniversalUpdateView.as_view(model=Grade, serializer_class=GradeSerializer)),
        path('grade/delete/<int:pk>/', UniversalDeleteView.as_view(model=Grade, serializer_class=GradeSerializer)),
    
        path('auth/', include('djoser.urls')),
        path('auth/token/', obtain_auth_token),
        path('logout/', Logout.as_view()),
    
    ]
