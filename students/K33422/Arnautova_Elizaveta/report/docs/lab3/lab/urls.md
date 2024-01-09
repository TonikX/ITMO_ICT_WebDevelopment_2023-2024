**Urls:** 


**mountaineering_club**
```
urlpatterns = [
    path("admin/", admin.site.urls),
    path('alp/', include('mountaineeringclub_app.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
```

**mountaineering_app**
```
urlpatterns = [
    path('climbers/<int:pk>/', ClimberDetail.as_view(), name='climber-detail'),
    path('climbers/', ClimberList.as_view(), name='climber'),

    path('ascensions/', AscensionListView.as_view(), name='ascensions'),
    path('userpage/<int:user_id>/ascensions/<int:pk>/', AscensionDetailView.as_view(), name='ascension-detail'),
    path('ascensions/<int:pk>/', AscensionDetailView.as_view(), name='ascension-detail'),

    path('participations/', AscentParticipationAPIView.as_view({'get': 'list'}), name='ascent-participation'),
    path('participations/<int:pk>/', AscentParticipationDetailView.as_view(), name='ascent-participation-detail'),

    path('mountains/', MountainsListView.as_view(), name='mountains'),
    path('mountains/<int:pk>/', MountainDetailView.as_view(), name='mountain-detail'),

    path('clubs/', ClubsListView.as_view(), name='clubs'),
    path('clubs/<int:pk>/', ClubDetailView.as_view(), name='club-detail'),

    path('groups/', GroupsListView.as_view(), name='groups'),
    path('userpage/<int:user_id>/groups/<int:pk>/', GroupsDetailView.as_view(), name='groups-detail'),
    path('groups/<int:pk>/', GroupsDetailView.as_view(), name='groups-detail'),
]
```
ну и по /auth/users/me/ можно получить иинформацию по пользователю











