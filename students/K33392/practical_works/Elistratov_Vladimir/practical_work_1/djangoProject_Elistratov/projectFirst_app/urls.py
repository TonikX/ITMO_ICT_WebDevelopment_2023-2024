from django.urls import path
from .views import *

urlpatterns = [
    path('owner/', CarOwnersList),
    path('car/', CarListView.as_view()),
    path('car/<int:pk>/', CarDetailView.as_view()),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
    path('owner/new/', CreateCarOwner),
    path('car/new/', CarCreateView.as_view()),
    path('owner/<int:carOwnerId>/', CarOwnersDetail)
    #path('book/list/', BookListView.as_view()),
    #path('time/', views.exp),
]