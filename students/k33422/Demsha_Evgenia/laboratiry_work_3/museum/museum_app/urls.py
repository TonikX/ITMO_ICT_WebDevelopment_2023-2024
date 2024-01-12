from django.urls import path, include

from .views import *

urlpatterns = [
    path('foundations/list', FoundationListView.as_view()),
    path('card/list', CardListView.as_view()),
    path('card/create/', CardCreateAPIView.as_view()),
    path('item/list', ItemListView.as_view()),
    path('item/create/', ItemCreateAPIView.as_view()),
    path('foundations/exhibitions/', FoundationExhibitionCountView.as_view()),
    path('card/items/', CardItemCountView.as_view()),
    path('foundations/ratio/', FoundationRatioView.as_view()),
    path('item/exhibitions/<int:pk>', ItemCommonExhibitionsView.as_view()),

]

