from django.urls import path
from .views import (
    ConferenceListView,
    ConferenceDetailView,
    RegisterAuthorView,
    WriteCommentView,
    RegistrationView,
    LoginView,
    UpdateRegistrationView,
    DeleteRegistrationView,
    logout_view
)

urlpatterns = [
    path('conferences/', ConferenceListView.as_view(), name='conference_list'),
    path('conferences/<int:pk>/', ConferenceDetailView.as_view(), name='conference_detail'),
    path('conferences/<int:pk>/comment/', WriteCommentView.as_view(), name='write_comment'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('conferences/<int:pk>/register/', RegisterAuthorView.as_view(), name='register_author'),
    path('conferences/<int:pk>/register/update/', UpdateRegistrationView.as_view(), name='update_registration'),
    path('conferences/<int:pk>/register/delete/', DeleteRegistrationView.as_view(), name='delete_registration'),
]
