from django.urls import path
from projectFirst_app import views

urlpatterns = [
    path('vault/', views.CapsuleListView.as_view(), name='vault_list'),
    path('vault/create', views.CapsuleCreateView.as_view(), name='vault_new'),
    path('vault/<int:pk>/', views.CapsuleDetailView.as_view(), name='vault_detail'),
    path('vault/<int:pk>/update', views.CapsuleUpdateView.as_view(), name='vault_update'),
    path('vault/<int:vault_pk>/file', views.CapsuleFileListView.as_view(), name='vault_file_list'),
    path('vault/<int:vault_pk>/file/create', views.CapsuleFileCreateView.as_view(), name='vault_file_new'),
    path('vault/<int:vault_pk>/comments/', views.CapsuleCommentsView.as_view(), name='vault_comments_list'),
    path('vault/<int:vault_pk>/comments/<int:comment_pk>', views.CapsuleCommentsView.as_view(), name='vault_comments_sub'),
    path('vault/<int:vault_pk>/comments/create', views.CapsuleCommentCreateView.as_view(), name='vault_comments_new'),
    path('vault/<int:vault_pk>/access', views.CapsuleAccessListView.as_view(), name='vault_access_list'),
    path('vault/<int:vault_pk>/access/add', views.CapsuleAccessCreateView.as_view(), name='vault_access_new'),
    path('person/', views.PeopleListView.as_view(), name='people_list'),
    path('person/<int:pk>/', views.PersonDetailView.as_view(), name='person_detail'),
    path('person/<int:pk>/friends/add', views.PeopleFriendShipView.as_view(), name='people_friends_add'),
]