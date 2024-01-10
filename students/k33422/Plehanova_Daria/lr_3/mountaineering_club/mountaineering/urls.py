from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AlpinistViewSet, ClimbViewSet, ClubViewSet, GroupMemberViewSet, GroupViewSet, GuideViewSet, \
	MountainViewSet, RouteViewSet

router = DefaultRouter()
router.register(r'alpinists', AlpinistViewSet)
router.register(r'guides', GuideViewSet)
router.register(r'mountains', MountainViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'clubs', ClubViewSet)
router.register(r'climbs', ClimbViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'group_members', GroupMemberViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
