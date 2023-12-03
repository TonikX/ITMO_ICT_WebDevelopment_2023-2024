# urls.py


Файл `urls.py` в Django используется для определения маршрутов (URL-путей) в вашем веб-приложении. Он связывает URL-пути с функциями (или классами) представлений, которые обрабатывают запросы пользователя.

В началя я импортирую модули для создания путей, а также представления из файла `views.py`.
```
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
```

Далее я прописываю пути к каждой странице: для этого я указываю путь, используемый класс или функцию из представления, а также даю имя для обращения к файлу.
```
urlpatterns = [

    # Главная страница
    path('', home, name='home'),

    # Страница со всеми авторами
    path('authors/', all_authors, name='all_authors'),

    # Добавление нового автора
    path('authors/add/', AuthorCreateView.as_view(), name='add_author'),

    # Редактирование существующего автора по его идентификатору
    path('author/<int:pk>/edit', AuthorUpdateView.as_view(), name='edit_author'),

    # Детали конкретного автора по его идентификатору
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),

    # Страница со всеми регистрациями
    path('registrations/', views.all_registrations, name='all_registrations'),

    # Добавление новой регистрации
    path('registrations/add/', RegistrationCreateView.as_view(), name='add_registration'),

    # Редактирование существующей регистрации по ее идентификатору
    path('registration/<int:pk>/edit', RegistrationUpdateView.as_view(), name='edit_registration'),

    # Детали конкретной регистрации по ее идентификатору
    path('registration/<int:registration_id>/', views.registration_detail, name='registration_detail'),

    # Удаление существующей регистрации по ее идентификатору
    path('registration/<int:pk>/delete', RegistrationDeleteView.as_view(), name='delete_registration'),

    # Страница со всеми отзывами
    path('reviews/', views.all_reviews, name='all_reviews'),

    # Добавление нового отзыва
    path('reviews/add/', ReviewCreateView.as_view(), name='add_review'),

    # Редактирование существующего отзыва по его идентификатору
    path('review/<int:pk>/edit', ReviewUpdateView.as_view(), name='edit_review'),

    # Детали конкретного отзыва по его идентификатору
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),

    # Страница со всеми презентациями
    path('presentations/', views.all_presentations, name='all_presentations'),

    # Добавление новой презентации
    path('presentations/add/', PresentationCreateView.as_view(), name='add_presentation'),

    # Редактирование существующей презентации по ее идентификатору
    path('presentation/<int:pk>/edit', PresentationUpdateView.as_view(), name='edit_presentation'),

    # Детали конкретной презентации по ее идентификатору
    path('presentation/<int:presentation_id>/', views.presentation_detail, name='presentation_detail'),

    # Страница со всеми конференциями
    path('conferences/', views.all_conferences, name='all_conferences'),

    # Детали конкретной конференции по ее идентификатору
    path('conference/<int:conference_id>/', views.conference_detail, name='conference_detail'),

    # Страница с авторами, зарегистрированными на конференции по ее идентификатору
    path('conference/<int:conference_id>/authors/', conference_authors, name='conference_authors'),
]
```