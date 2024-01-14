from .views import *
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Настройка представлений drf-yasg
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="API documentation for my app electronic_journal_college",
        terms_of_service="https://www.example.com/terms/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("user/role/", UserRoleView.as_view()),
    path("teacher/", TeacherView.as_view(), name="teacher"),
    path("teachers/", TeachersView.as_view(), name="teachers"),
    path("student/", StudentView.as_view(), name="student"),
    path("groups/", GroupsView.as_view(), name="students"),
    path("grade/", GradeView.as_view(), name="grade"),
    path("time_slots/", TimeSlotsView.as_view(), name="time_slots"),
    path("disciplines/", DisciplinesView.as_view(), name="discipline"),
    path("schedule/", ScheduleView.as_view(), name="schedule"),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path('rooms/', AvailableRoomsView.as_view(), name='available_rooms'),
    # Документация Swagger
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
