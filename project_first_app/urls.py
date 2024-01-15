from django.urls import path

from project_first_app import views
from project_first_app.views import AutoUpdateView, AutoList, AutoRetrieveView, AutoCreateView, AutoDeleteView, \
    OwnerCreateView

urlpatterns = [
    path('owner/<int:owner_id>', views.auto_owner, name='owner'),
    path('time/', views.display_time, name='time'),
    path('auto/', views.AutoDetail.as_view(), name='auto-detail'),
    path('auto/<int:pk>/', AutoRetrieveView.as_view()),
    path('auto/list/', AutoList.as_view()),
    path('auto/<int:pk>/update/', AutoUpdateView.as_view()),
    path('auto/create/', AutoCreateView.as_view()),
    path('auto/<int:pk>/delete/', AutoDeleteView.as_view()),
    path('owner/create/', OwnerCreateView.as_view())
]