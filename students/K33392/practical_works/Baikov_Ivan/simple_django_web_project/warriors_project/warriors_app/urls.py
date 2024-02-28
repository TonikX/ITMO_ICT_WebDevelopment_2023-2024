from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = "warriors_app"

router = DefaultRouter()  # found this on StackOverflow for managing ManyToMany
router.register(r'warriors', WarriorViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'skill-of-warriors', SkillOfWarriorViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('warriors/', WarriorList.as_view(), name='warrior-list'),
    path('warriors-professions/', WarriorWithProfessionsView.as_view(), name='warrior-with-professions'),
    path('warriors-skills/', WarriorWithSkillsView.as_view(), name='warrior-with-skills'),

    path('skills/', SkillList.as_view(), name='skill-list'),
    path('skills/<int:pk>/', SkillDetail.as_view(), name='skill-detail'),
    path('professions/', ProfessionList.as_view(), name='profession-list'),
    path('professions/<int:pk>/', ProfessionDetail.as_view(), name='profession-detail'),

    path('warriors/<int:pk>/', WarriorDetail.as_view(), name='warrior-detail'),
    path('warriors/<int:pk>/update/', WarriorUpdate.as_view(), name='warrior-update'),
    path('warriors/<int:pk>/delete/', WarriorDelete.as_view(), name='warrior-delete'),

]
