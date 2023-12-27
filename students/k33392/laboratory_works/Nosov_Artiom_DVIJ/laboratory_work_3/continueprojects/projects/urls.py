from django.urls import path
from .views import *


app_name = "projects"


urlpatterns = [
    path('', home, name="home"),

    path('update-user/', updateUser, name="update-user"),
    path('topics/', topicsPage, name="topics"),

    path('activity/', activityPage, name="activity"),

    # path('create-job/', createJob, name="create-job"), TODO
    # path('update-job/<str:pk>/', updateJob, name="update-job"),
    # path('delete-job/<str:pk>/', deleteJob, name="delete-job"),
    # path('delete-message/<str:pk>/', deleteMessage, name="delete-message"),
    # File
    path('file/create/', FileCreateAPIView.as_view()),
    path('file/<str:pk>/', FileListAPIView.as_view()),
    path('file/list/', FileListAPIView.as_view()),
    path('file/delete/<str:pk>/', FileDestroyAPIView.as_view()),
    path('file/update/<str:pk>/', FileUpdateAPIView.as_view()),
    # ProjectTopic
    path('topic/create/', ProjectTopicCreateAPIView.as_view()),
    path('topic/<str:pk>/', ProjectTopicListAPIView.as_view()),
    path('topic/list/', ProjectTopicListAPIView.as_view()),
    path('topic/delete/<str:pk>/', ProjectTopicDestroyAPIView.as_view()),
    path('topic/update/<str:pk>/', ProjectTopicUpdateAPIView.as_view()),
    # Project
    path('create/', ProjectCreateAPIView.as_view()),
    path('<str:pk>/', ProjectListAPIView.as_view()),
    path('list/', ProjectListAPIView.as_view()),
    path('delete/<str:pk>/', ProjectDestroyAPIView.as_view()),
    path('update/<str:pk>/', ProjectUpdateAPIView.as_view()),
    # GradeReport
    path('grade_report/create/', GradeReportCreateAPIView.as_view()),
    path('grade_report/<str:pk>/', GradeReportListAPIView.as_view()),
    path('grade_report/list/', GradeReportListAPIView.as_view()),
    path('grade_report/delete/<str:pk>/', GradeReportDestroyAPIView.as_view()),
    path('grade_report/update/<str:pk>/', GradeReportUpdateAPIView.as_view()),
    # ProjectOfUser
    path('project_of_user/create/', ProjectOfUserCreateAPIView.as_view()),
    path('project_of_user/<str:pk>/', ProjectOfUserListAPIView.as_view()),
    path('project_of_user/list/', ProjectOfUserListAPIView.as_view()),
    path('project_of_user/delete/<str:pk>/', ProjectOfUserDestroyAPIView.as_view()),
    path('project_of_user/update/<str:pk>/', ProjectOfUserUpdateAPIView.as_view()),
    # Teacher
    path('teacher/create/', TeacherCreateAPIView.as_view()),
    path('teacher/<str:pk>/', TeacherListAPIView.as_view()),
    path('teacher/list/', TeacherListAPIView.as_view()),
    path('teacher/delete/<str:pk>/', TeacherDestroyAPIView.as_view()),
    path('teacher/update/<str:pk>/', TeacherUpdateAPIView.as_view()),
    # Student
    path('student/create/', StudentCreateAPIView.as_view()),
    path('student/<str:pk>/', StudentListAPIView.as_view()),
    path('student/list/', StudentListAPIView.as_view()),
    path('student/delete/<str:pk>/', StudentDestroyAPIView.as_view()),
    path('student/update/<str:pk>/', StudentUpdateAPIView.as_view()),
    # Grade
    path('grade/create/', GradeCreateAPIView.as_view()),
    path('grade/<str:pk>/', GradeListAPIView.as_view()),
    path('grade/list/', GradeListAPIView.as_view()),
    path('grade/delete/<str:pk>/', GradeDestroyAPIView.as_view()),
    path('grade/update/<str:pk>/', GradeUpdateAPIView.as_view()),
    # ProjectMeeting
    path('project_meeting/create/', ProjectMeetingCreateAPIView.as_view()),
    path('project_meeting/<str:pk>/', ProjectMeetingListAPIView.as_view()),
    path('project_meeting/list/', ProjectMeetingListAPIView.as_view()),
    path('project_meeting/delete/<str:pk>/', ProjectMeetingDestroyAPIView.as_view()),
    path('project_meeting/update/<str:pk>/', ProjectMeetingUpdateAPIView.as_view()),
    # Meeting
    path('meeting/create/', MeetingCreateAPIView.as_view()),
    path('meeting/<str:pk>/', MeetingListAPIView.as_view()),
    path('meeting/list/', MeetingListAPIView.as_view()),
    path('meeting/delete/<str:pk>/', MeetingDestroyAPIView.as_view()),
    path('meeting/update/<str:pk>/', MeetingUpdateAPIView.as_view()),

]