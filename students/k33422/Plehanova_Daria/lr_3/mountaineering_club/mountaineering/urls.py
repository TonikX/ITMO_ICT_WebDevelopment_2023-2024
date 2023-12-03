from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AlpinistViewSet, GuideViewSet, MountainViewSet, RouteViewSet, ClubViewSet

router = DefaultRouter()
router.register(r'alpinists', AlpinistViewSet)
router.register(r'guides', GuideViewSet)
router.register(r'mountains', MountainViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'clubs', ClubViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
