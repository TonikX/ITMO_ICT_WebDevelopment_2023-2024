from django.urls import path
from . import views
from .views import (
    home,
    AuthorCreateView,
    AuthorUpdateView,
    RegistrationCreateView,
    RegistrationUpdateView,
    RegistrationDeleteView,
    PresentationCreateView,
    PresentationUpdateView,
    ReviewCreateView,
    ReviewUpdateView,
    conference_authors,
    all_authors,
)
urlpatterns = [

    path('', home, name='home'),
    path('authors/', all_authors, name='all_authors'),
    path('authors/add/', AuthorCreateView.as_view(), name='add_author'),
    path('author/<int:pk>/edit', AuthorUpdateView.as_view(), name='edit_author'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),

    path('registrations/', views.all_registrations, name='all_registrations'),
    path('registrations/add/', RegistrationCreateView.as_view(), name='add_registration'),
    path('registration/<int:pk>/edit', RegistrationUpdateView.as_view(), name='edit_registration'),
    path('registration/<int:registration_id>/', views.registration_detail, name='registration_detail'),
    path('registration/<int:pk>/delete', RegistrationDeleteView.as_view(), name='delete_registration'),

    path('reviews/', views.all_reviews, name='all_reviews'),
    path('reviews/add/', ReviewCreateView.as_view(), name='add_review'),
    path('review/<int:pk>/edit', ReviewUpdateView.as_view(), name='edit_review'),
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),

    path('presentations/', views.all_presentations, name='all_presentations'),
    path('presentations/add/', PresentationCreateView.as_view(), name='add_presentation'),
    path('presentation/<int:pk>/edit', PresentationUpdateView.as_view(), name='edit_presentation'),
    path('presentation/<int:presentation_id>/', views.presentation_detail, name='presentation_detail'),

    path('conferences/', views.all_conferences, name='all_conferences'),
    path('conference/<int:conference_id>/', views.conference_detail, name='conference_detail'),
    path('conference/<int:conference_id>/authors/', conference_authors, name='conference_authors'),
]
