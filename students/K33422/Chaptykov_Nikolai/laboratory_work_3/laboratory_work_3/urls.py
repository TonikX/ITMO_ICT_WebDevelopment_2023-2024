"""laboratory_work_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lab_app.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='Conversion, software version 7.0',
      description="Looking at life through the eyes of a tire hub ",
      terms_of_service="Пользуйтесь на здоровье",
      contact=openapi.Contact(email="Не пишите, но если уже начали - не прекращайте, nick.chaptykov@gmail.com"),
      license=openapi.License(name="Лицензия на продажу рыболовных снастей"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('group/', GroupList.as_view()),
    path('group/<int:pk>', GroupDetail.as_view()),
    path('group/<int:pk1>/<int:pk>', StudentDetail.as_view()),
    path('tutor/', TutorList.as_view()),
    path('tutor/<int:pk>', TutorDetail.as_view()),
    path('group/<int:pk>/tutors', GroupTutorsList.as_view()),
    path('group/<int:pk>/cnt', CountStudents.as_view()),
    path('group/timetable/<int:pk1>/<int:pk>', GetTimetable.as_view()),
    path('group/timetable/<int:pk2>/<int:pk1>/<int:pk>', GetTimetableDeeper.as_view()),
    path('tutor/groups/<int:pk1>/<int:pk>', GroupByTutor.as_view()),
    path('group/list_lessons/<int:pk>', ListGroupLessons.as_view()),
    path('group/list_lessons/<int:pk1>/<int:pk>', GroupLessonDetail.as_view()),
    path('group/list_lessons/schedule/<int:pk>', ScheduleGroupLesson.as_view()),
    path('group/list_lessons/create', CreateGroupLesson.as_view()),
    path('student/performance/<int:pk>', StudentPerformance.as_view()),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
