## Urls.py

```
from django.urls import path
from . import views

urlpatterns = [
    path('guests/all/', views.list_guests_view),
    path('guests/<int:guest_id>/', views.guest_detail_view),
    path('guests/register/', views.UserRegistration.as_view()),
    path('guests/sign_in/', views.UserRegistration.as_view()),
    path('conferences/list/', views.Conference_guests_list_view.as_view()),
    path('conferences/<int:conference_id>/', views.conference_detail_view),
    path('conferences/my/', views.Conference_my_list_view.as_view(), name='home'),
    path('attendance/register/', views.AttendanceRegistration.as_view()),
    path('attendance/my/', views.AttendanceMyRegistration.as_view()),
    path('attendance/edit/<int:pk>/', views.AttendanceUpdateView.as_view()),
    path('attendance/delete/<int:pk>/', views.AttendanceDeleteView.as_view()),
    path('lectures/<int:conference_id>/', views.lecture_by_conference_view),
    path('lectures/<int:conference_id>/add/', views.LectureRegistration.as_view()),
    path('lectures/<int:pk>/edit/', views.LectureUpdateView.as_view()),
    path('lectures/<int:pk>/delete/', views.LectureDeleteView.as_view()),
    path('comments/<int:conference_id>/', views.comments_by_conference_view),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view()),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view()),
    path('comments/create/', views.CommentsRegistration.as_view()),
    path('logout/', views.logout_view),
    path('login/', views.login_view),

]
```