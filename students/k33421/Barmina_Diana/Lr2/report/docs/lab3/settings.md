# Настройки

**Все прописанные пути**</br>
</br>Не прописаны только пути для личной страницы пользователя, однако она находится по ссылке http://localhost:8000/alp/auth/users/me/ 
```
urlpatterns = [
    path('alpinists/', AlpinistsAPIView.as_view(), name='alpinists'),

    path('climbings/', ClimbingsListView.as_view(), name='climbings'),
    path('climbings/<int:pk>/', ClimbingsDetailView.as_view(), name='climbing-detail'),

    path('mountains/', MountainsListView.as_view(), name='mountains'),
    path('mountains/<int:pk>/', MountainsDetailView.as_view(), name='mountain-detail'),

    path('participatings/', ParticipationAPIView.as_view({'get': 'list'}), name='participatings'),
    path('userpage/<int:user_id>/participatings/<int:pk>/', ParticipatingDetailView.as_view(), name='users-participation-detail'),
    path('userpage/<int:user_id>/climbings-participation/<int:pk>/create/', ParticipatingCreateView.as_view(), name='users-participation-create'),
    path('userpage/<int:user_id>/participatings/<int:pk>/update/', ParticipatingUpdateView.as_view(), name='users-participating-update'),
    path('userpage/<int:user_id>/participatings/<int:pk>/delete/', ParticipatingDeleteView.as_view(), name='users-participating-delete'),

    path('clubs/', ClubsListView.as_view(), name='clubs'),
    path('clubs/<int:pk>/', ClubDetailView.as_view(), name='club-detail'),

    path('club-memberships/', ClubMemberViewSet.as_view({'get': 'list'}), name='club-memberships'),
    path('userpage/<int:pk>/club-membership/create/', ClubMembershipCreateView.as_view(), name='users-club-membership-create'),
    path('userpage/<int:user_id>/club-membership/<int:pk>/delete/', ClubMembershipDeleteView.as_view(), name='users-club-membership-delete'),

    path('emergency/', EmergencyListView.as_view(), name='emergency-list'),
]
```

